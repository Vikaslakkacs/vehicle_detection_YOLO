from vehicle_detection.constants import *
from vehicle_detection.utils.common import read_yaml, create_directories
from vehicle_detection.entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self,
                 config_filepath= CONFIG_FILE_PATH,
                 params_filepath= PARAMS_FILE_PATH):
        """
        Creating artifact directories from config.yaml file
        """
        self.config= read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)
        ##Creating Directories
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Creating directory for data ingestion from config.yaml file.

        Returns:
            DataIngestionConfig: Dataingestion data
        """
        config= self.config.data_ingestion
        ##Create directory that are required for data ingestion(taken from config.yaml)
        create_directories([config.root_dir])

        data_ingestion_config= DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir,
            zip_file_dir= config.zip_file_dir,
            dataset_source= config.dataset_source
        )
        return data_ingestion_config

