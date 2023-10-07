from vehicle_detection import logger
from vehicle_detection.components.prepare_base_model import PrepareBaseModel
from vehicle_detection.config.configuration import ConfigurationManager

try:
    modelconfig= ConfigurationManager()
    prepare_base_model_config= modelconfig.get_prepare_base_model_config()
    prepare_base_model= PrepareBaseModel(prepare_base_model_config)
    prepare_base_model.get_base_model()

except Exception as e:
    e