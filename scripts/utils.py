from tkinter import Tk, simpledialog

import numpy as np
from scipy.interpolate import CubicSpline

import mne

  
def interpolate_pulse_cubic_spline(eeg_data, events_array, interpolate_from, interpolate_to, out_file):
    """Interpolates TMS pulse artifacts with a cubic spline, channel-by-channel. 

    Parameters:
    eeg_data -- continuous EEG data with artifacts to interpolate (type: mne.Raw object)
    events_array -- an array of events. Event times are in column 0 (type: NumPy array)
    interpolate_from -- the start time of the interpolation window, in seconds (type: float)
    interpolate_to -- the end time of the interpolation window, in seconds (type: float)

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

    post_interpolation_eeg_data = mne.io.RawArray(data=raw_eeg_time_series,
                                                  info=eeg_data.info)
    post_interpolation_eeg_data.save(fname=out_file, 
                                     overwrite=True)
    return post_interpolation_eeg_data

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