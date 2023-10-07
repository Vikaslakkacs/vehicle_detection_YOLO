from vehicle_detection.constants import *
from vehicle_detection.utils.common import read_yaml, create_directories
from vehicle_detection.entity import DataIngestionConfig
from vehicle_detection.entity.config_entity import PrepareBaseModelConfig
from vehicle_detection import logger
class ConfigurationManager:
    def __init__(self,
                 config_filepath= CONFIG_FILE_PATH,
                 params_filepath= PARAMS_FILE_PATH,
                 yolo_v_5s_filepath= YOLO_V_5S_FILE_PATH,
                 yolo_params_filepath= YOLO_PARAMS_FILE_PATH):
        """
        Creating artifact directories from config.yaml file
        """
        self.config= read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)
        self.yolo_v_5s= read_yaml(yolo_v_5s_filepath)
        self.yolo_params= read_yaml(yolo_params_filepath)
        ##Creating Directories
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Creating directory for data ingestion from config.yaml file.

        Returns:
            DataIngestionConfig: Dataingestion data
        """
        config= self.config.data_ingestion
        params= self.params
        ##Create directory that are required for data ingestion(taken from config.yaml)
        create_directories([config.root_dir])

        data_ingestion_config= DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir,
            zip_file_dir= config.zip_file_dir,
            dataset_source= config.dataset_source,
            coordinates_path= config.coordinates_path,
            yolo_conversion_image_size= params.IMAGE_SIZE,
            yolo_voc_bbx= params.VOC_BBX,
            coordinates_target_path= config.coordinates_target_path
        )
        return data_ingestion_config


    ###Prepare basemodel Config
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """Get all the details that are required to download yolo version

        Returns:
            PrepareBaseModelConfig: PrepareBaseModelConfig
        """
        config= self.config.prepare_base_model
        params= self.params
        logger.info("base model parameters loaded")
        ##Create root directory for preparebasemodel
        create_directories([config.root_dir])
        logger.info(f"Root directory: {config.root_dir} has created")

        prepare_base_model_config= PrepareBaseModelConfig(
            root_dir= config.root_dir,
            base_model_link= config.base_model_link,
            base_model_path= config.base_model_path,
            params_image_size= params.IMAGE,
            params_batch= params.BATCH,
            params_epochs= params.EPOCHS,
            params_classes= params.NAMES
            
        )
        return prepare_base_model_config

