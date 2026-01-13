import matplotlib                                   
matplotlib.use('Qt5Agg')                            

import mne                                          

import config
import utils


utils.make_directories(directories_to_make=[config.preprocessed_dir])

for subject in config.subjects_list:
    raw_eeg_data = utils.load_data(data_dir=config.data_dir,
                                   subject_id=subject,
                                   file_type="brainvision")

    eeg_data = utils.drop_channels_set_montage(eeg_data=raw_eeg_data, 
                                               desired_montage=config.montage) 
    eeg_data.plot()

    events_from_annotations, events_dict = mne.events_from_annotations(raw=eeg_data)
    events_from_annotations = events_from_annotations[config.first_event:]
    post_interpolation_eeg = utils.interpolate_pulse_cubic_spline(eeg_data=eeg_data,
                                                                  events_array=events_from_annotations,
                                                                  interpolate_from=config.INTERPOLATE_FROM,
                                                                  interpolate_to=config.INTERPOLATE_TO,
                                                                  out_file=config.preprocessed_dir + config.output_filenames["interpolation"])

    post_hp_filter_eeg = utils.iir_filter_zero_phase(eeg_data=post_interpolation_eeg,
                                                     low=config.high_pass_from,
                                                     high=config.high_pass_to,
                                                     out_file=config.preprocessed_dir + config.output_filenames["high_pass_filter"])
    post_hp_filter_epochs = mne.Epochs(raw=post_hp_filter_eeg,
                                       events=events_from_annotations,
                                       tmin=config.EPOCH_FROM,
                                       tmax=config.EPOCH_TO,
                                       baseline=None)

    post_ica_epochs = utils.run_and_apply_ica(epochs_to_decompose=post_hp_filter_epochs,
                                              out_file=config.preprocessed_dir + config.output_filenames["ica"])

    post_lp_filter_eeg = utils.iir_filter_zero_phase(eeg_data=post_ica_epochs.get_data(),
                                                     low=config.low_pass_from,
                                                     high=config.low_pass_to,
                                                     out_file=None)
    post_lp_filter_epochs = mne.EpochsArray(data=post_lp_filter_eeg,
                                            info=post_ica_epochs.info,
                                            baseline=None)

    rereferenced_epochs, reference = mne.set_eeg_reference(inst=post_lp_filter_epochs,
                                                           ref_channels=config.new_reference) 
    
    baseline_corrected_epochs = rereferenced_epochs.apply_baseline(baseline=(config.baseline_window_start, config.baseline_window_end))

    final_epochs = baseline_corrected_epochs.crop(tmin=config.CROP_EPOCHS_FROM,
                                                  tmax=config.CROP_EPOCHS_TO,
                                                  include_tmax=True)
    final_tep = final_epochs.average()
    final_tep.plot();