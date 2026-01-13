subjects_list = ["S02C1_M1"]
data_dir = "data"
preprocessed_dir = "preprocessed"
output_filenames = {"interpolation": "post_interpolation_eeg.fif",
                    "high_pass_filter": "post_hp_filtering_eeg.fif",
                    "ica": "post_ica_epo.fif",
                    "low_pass_filter": "post_lp_filtering_epo.fif",
                    "final": "final_epo.fif"}


montage = "easycap-M1"

high_pass_from = 0.1
high_pass_to = None
low_pass_from = None
low_pass_to = 70.0

first_event = 2
INTERPOLATE_FROM = 0.002    # seconds before pulse
INTERPOLATE_TO = 0.005      # seconds after pulse
EPOCH_FROM = -1.1           # seconds before pulse
EPOCH_TO = 0.5              # seconds before pulse
TIME_OF_EVENT = 1.1         # seconds within epoch   
CROP_EPOCHS_FROM = 1.0      # seconds within epoch
CROP_EPOCHS_TO = 1.6        # seconds within epoch

new_reference = "average"

baseline_window_start = TIME_OF_EVENT - 0.100   # seconds
baseline_window_end = TIME_OF_EVENT - 0.002     # seconds
