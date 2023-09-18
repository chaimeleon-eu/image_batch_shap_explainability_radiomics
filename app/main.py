import os
import pickle
import numpy as np
import configparser
from tab_shap import SHAPAnalysis

def read_config_file(file_path):
    """Parse a config file and return a configparser.ConfigParser object."""

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")

    # Instantiate a ConfigParser object and read the config file
    config = configparser.ConfigParser()
    config.read(file_path)

    return config

def load_data(file_path):
    """Load a data file and return its content."""

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")

    # Load the file content
    data = np.load(file_path)

    return data

def main():
    """Main function to load model, test data, compute and plot SHAP values."""

    # Read and parse the config file
    config = read_config_file('config.ini')

    # Extract values from the config file
    # The .get() method provides a way to specify a default value in case the key is not present
    model_filename = config.get("DEFAULT", "model_filename", fallback=None)
    test_data_preprocess = config.get("DEFAULT", "test_data_preprocess", fallback=None)
    save_dir_for_plots = config.get("DEFAULT", "save_dir_for_plots", fallback=None)
    local_plt_indices_list = [int(x) for x in config.get("DEFAULT", "local_plt_indices_list", fallback="").split(",")]
    top_n_dependence_plots = int(config.get("DEFAULT", "top_n_dependence_plots", fallback=0))
    top_n_dependence_interactions = int(config.get("DEFAULT", "top_n_dependence_interactions", fallback=0))
    feature_names = config.get("DEFAULT", "feature_names", fallback=0).split(",")

    # Load the trained model
    model = pickle.load(open(model_filename, 'rb'))

    # Load the test data
    test_data = load_data(test_data_preprocess)

    # check if the dimension match between the feature names and the data
    if len(feature_names) != np.squeeze(test_data).shape[-1]:
        feature_names = None

    # Initialize SHAPAnalysis with the trained model and compute SHAP values
    shap_analysis_svm = SHAPAnalysis(model, save_dir_for_plots, feature_names=feature_names)
    shap_analysis_svm.compute(test_data)

    # Generate and save plots
    
    shap_analysis_svm.global_summary_plot()
    shap_analysis_svm.local_plot(local_plt_indices_list)
    shap_analysis_svm.shap_dependence_plot(top_n_dependence_plots, no_of_interactions=top_n_dependence_interactions)

if __name__ == "__main__":
    main()
