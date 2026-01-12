from pathlib import Path                            
from tkinter import Tk, simpledialog

import numpy as np                                 
import matplotlib                                   
matplotlib.use('Qt5Agg')                            

import mne                                          

from scipy.interpolate import CubicSpline


data_dir = Path("data")
subject_and_condition = "S02C1_M1"

file_of_interest = list(data_dir.glob(pattern=f"{subject_and_condition}.vhdr"))
eeg_data = mne.io.read_raw_brainvision(vhdr_fname=file_of_interest[0])

channels_to_drop = []
for channel_name in eeg_data.ch_names:
    try:
        int(channel_name[-1])
    except ValueError:
        if channel_name[-1] != "z": 
            channels_to_drop.append(channel_name)
print(f"Channels to drop: {channels_to_drop}")
eeg_data = eeg_data.drop_channels(ch_names=channels_to_drop)

easycap_m1_montage = mne.channels.make_standard_montage(kind="easycap-M1")
eeg_data.set_montage(montage=easycap_m1_montage,
                     on_missing="ignore")

eeg_data.plot()

events_from_annotations, events_dict = mne.events_from_annotations(raw=eeg_data)
events_from_annotations = events_from_annotations[2:]

raw_eeg_time_series = eeg_data.copy().get_data().astype("float32")
number_of_channels = raw_eeg_time_series.shape[0]
time_indices = np.arange(raw_eeg_time_series.shape[1])
prestim_points = int(0.002*eeg_data.info["sfreq"])
poststim_points = int(0.005*eeg_data.info["sfreq"])

for event_number, event in enumerate(events_from_annotations):
        print(f"Processing event {event_number}...")
        event_time = int(event[0])
        artifact_window_min = event_time - prestim_points
        artifact_window_max = event_time + poststim_points
        artifact_mask = np.ones(shape=raw_eeg_time_series.shape[1], 
                                dtype=bool)
        artifact_mask[artifact_window_min:artifact_window_max] = False
        indices_of_interest = time_indices[artifact_mask]
        for channel in range(number_of_channels):
            print(f"Working on channel {channel}...")
            data_of_interest = raw_eeg_time_series[channel, artifact_mask]
            cubic_spline = CubicSpline(x=indices_of_interest,
                                        y=data_of_interest)
            new_indices = np.arange(start=artifact_window_min,
                                    stop=artifact_window_max)
            interpolated_pulse = cubic_spline(new_indices)
            raw_eeg_time_series[channel, artifact_window_min:artifact_window_max] = interpolated_pulse 

post_interpolation_eeg = mne.io.RawArray(data=raw_eeg_time_series,
                                         info=eeg_data.info)
post_filtering_eeg = mne.filter.filter_data(data=post_interpolation_eeg.get_data(),
                                            sfreq=post_interpolation_eeg.info["sfreq"],
                                            l_freq=0.1,
                                            h_freq=None,
                                            method="iir",
                                            iir_params=None,
                                            copy=True,
                                            phase="zero")
post_filtering_eeg = mne.io.RawArray(data=post_filtering_eeg,
                                     info=post_interpolation_eeg.info)
post_filtering_epochs = mne.Epochs(raw=post_filtering_eeg,
                                   events=events_from_annotations,
                                   tmin=-1.1,
                                   tmax=0.5,
                                   baseline=None)
ica = mne.preprocessing.ICA(random_state=0)
ica.fit(post_filtering_epochs)
ica.plot_components(inst=post_filtering_epochs, picks=range(30))
ica.plot_sources(inst=post_filtering_epochs)

root_window = Tk()
root_window.withdraw()
dialog_title = "IC rejection"
dialog_prompt = "Which components do you reject? Insert tab-separated indices (e.g., 1 2 3). Leave blank to reject no components"
components = simpledialog.askstring(title=dialog_title, 
                                    prompt=dialog_prompt)
try:
    components_list = components.split(" ")
    components_list = [int(item) for item in components_list]
except ValueError:
    components_list = []

ica.exclude = components_list
ica.apply(post_filtering_epochs.load_data())
post_ica_epochs = post_filtering_epochs

post_ica_epochs.plot()

low_pass_filtered_data = mne.filter.filter_data(data=post_ica_epochs.get_data(),
                                                sfreq=post_ica_epochs.info["sfreq"],
                                                l_freq=None,
                                                h_freq=70.0,
                                                method="iir",
                                                iir_params=None,
                                                copy=True,
                                                phase="zero")
low_pass_filtered_epochs = mne.EpochsArray(data=low_pass_filtered_data,
                                           info=post_ica_epochs.info,
                                           baseline=None)

rereferenced_epochs, reference = mne.set_eeg_reference(inst=low_pass_filtered_epochs,
                                                       ref_channels="average") 

baseline_corrected_epochs = rereferenced_epochs.apply_baseline(baseline=(1.1-0.100, 1.1-0.002))

final_epochs = baseline_corrected_epochs.crop(tmin=1.0,
                                              tmax=1.6,
                                              include_tmax=True)
final_tep = final_epochs.average()
final_tep.plot();