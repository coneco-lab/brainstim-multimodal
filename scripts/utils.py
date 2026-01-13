from pathlib import Path
from tkinter import Tk, simpledialog

import matplotlib
import matplotlib .pyplot as plt                                 
matplotlib.use('Qt5Agg') 
import numpy as np 
from scipy.interpolate import CubicSpline

import mne


def make_directories(directories_to_make):
    """Given a list of pathnames, creates one directory each.
    
    Parameters:
    directories_to_make -- the pathnames (list of str)
    """

    for directory in directories_to_make:
        directory_object = Path(directory)
        try:
            directory_object.mkdir()
        except FileExistsError:
            print(f"Did not create directory {directory} because it already existed")
            pass
            
def load_data(data_dir, file_type, subject_id):
    data_dir = Path(data_dir)
    if file_type == "brainvision":
        file_of_interest = list(data_dir.glob(pattern=f"{subject_id}.vhdr"))
        eeg_data = mne.io.read_raw_brainvision(vhdr_fname=file_of_interest[0])
    elif file_type == "eeglab":
        file_of_interest = list(data_dir.glob(pattern=f"{subject_id}.set"))
        eeg_data = mne.io.read_raw_eeglab(input_fname=file_of_interest[0])
    elif file_type == "edf":
        file_of_interest = list(data_dir.glob(pattern=f"{subject_id}.edf"))
        eeg_data = mne.io.read_raw_edf(input_fname=file_of_interest[0], preload=True)
    return eeg_data

def drop_channels_set_montage(eeg_data, desired_montage):
    channels_to_drop = []
    for channel_name in eeg_data.ch_names:
        try:
            int(channel_name[-1])
        except ValueError:
            if channel_name[-1] != "z": 
                channels_to_drop.append(channel_name)
    print(f"Channels to drop: {channels_to_drop}")
    eeg_data = eeg_data.drop_channels(ch_names=channels_to_drop)
    easycap_m1_montage = mne.channels.make_standard_montage(kind=desired_montage)
    eeg_data.set_montage(montage=easycap_m1_montage,
                        on_missing="ignore")
    return eeg_data

def inspect_eeg_data(eeg_data):
    eeg_data.plot()
    plt.show()
  
def interpolate_pulse_cubic_spline(eeg_data, events_array, interpolate_from, interpolate_to, out_file=None):
    """Interpolates TMS pulse artifacts with a cubic spline, channel-by-channel. 

    Parameters:
    eeg_data -- continuous EEG data with artifacts to interpolate (type: mne.Raw object)
    events_array -- an array of events. Event times are in column 0 (type: NumPy array)
    interpolate_from -- the start time of the interpolation window, in seconds (type: float)
    interpolate_to -- the end time of the interpolation window, in seconds (type: float)
    out_file -- the name of the output file (type: str) (default: None)

    Returns:
    post_interpolation_eeg_data -- continuous EEG data with no more artefacts (type: mne.Raw object)
    """
    
    raw_eeg_time_series = eeg_data.copy().get_data().astype("float32")
    number_of_channels = raw_eeg_time_series.shape[0]
    time_indices = np.arange(raw_eeg_time_series.shape[1])
    prestim_points = int(interpolate_from*eeg_data.info["sfreq"])
    poststim_points = int(interpolate_to*eeg_data.info["sfreq"])

    for event_number, event in enumerate(events_array):
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
    if out_file:
        post_interpolation_eeg.save(fname=out_file, 
                                         overwrite=True)
    return post_interpolation_eeg

def iir_filter_zero_phase(eeg_data, low, high, out_file):
    post_filtering_eeg = mne.filter.filter_data(data=eeg_data.get_data(),
                                                sfreq=eeg_data.info["sfreq"],
                                                l_freq=low,
                                                h_freq=high,
                                                method="iir",
                                                iir_params=None,
                                                copy=True,
                                                phase="zero")
    post_filtering_eeg = mne.io.RawArray(data=post_filtering_eeg,
                                         info=eeg_data.info)
    if out_file:
        post_filtering_eeg.save(fname=out_file, 
                                overwrite=True)
    return post_filtering_eeg

def select_items(item_type):
    """Opens an interactive pop-up window where the user can insert 
    independent component numbers for rejection or bad channel
    names for interpolation.
        
    Parameters:
    item_type -- insert "ica" for component rejection, "bads" for
    bad channel interpolation
    """
    root_window = Tk()
    root_window.withdraw()
    if item_type == "ica":
        dialog_title = "IC rejection"
        dialog_prompt = "Which components do you reject? Insert tab-separated indices (e.g., 1 2 3). Leave blank to reject no components"
        items = simpledialog.askstring(title=dialog_title,
                                       prompt=dialog_prompt)
        try:
            items_list = items.split(" ")
            items_list = [int(item) for item in items_list]
        except ValueError:
            items_list = []
    elif item_type == "bads":
        dialog_title = "Bad channels interpolation"
        dialog_prompt = "Which channels do you want to interpolate? Insert tab-separated names. Leave blank to interpolate no channels"
        items = simpledialog.askstring(title=dialog_title,
                                       prompt=dialog_prompt)
        if items == "":
            items_list = []    
        else:
            items_list = items.split(" ")
    return items_list

def run_and_apply_ica(epochs_to_decompose, plotted_components=30, out_file=None):
    ica = mne.preprocessing.ICA(random_state=0)
    ica.fit(epochs_to_decompose)
    ica.plot_components(inst=epochs_to_decompose, picks=range(plotted_components))
    ica.plot_sources(inst=epochs_to_decompose)
    components_to_reject = select_items(item_type="ica")
    ica.exclude = components_to_reject
    ica.apply(epochs_to_decompose.load_data())
    post_ica_epochs = epochs_to_decompose
    if out_file:
        post_ica_epochs.save(fname=out_file, 
                             overwrite=True)
    return post_ica_epochs