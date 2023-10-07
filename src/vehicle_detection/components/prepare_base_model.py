from git import Repo
from vehicle_detection.entity.config_entity import PrepareBaseModelConfig
from vehicle_detection import logger




class PrepareBaseModel:
    """Download model from yolo and get all the details that are required for training
    """
    def __init__(self, config: PrepareBaseModelConfig):
        self.config= config
    
    ##Get the base model
    def get_base_model(self):
        config= self.config
        ##Download base model from github
        Repo.clone_from(config.base_model_link, config.base_model_path)
        logger.info(f"repository cloned in {config.base_model_path}")