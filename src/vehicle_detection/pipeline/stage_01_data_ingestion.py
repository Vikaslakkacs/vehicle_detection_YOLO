from vehicle_detection.components.data_ingestion import DataIngestion
from vehicle_detection.config import ConfigurationManager
from vehicle_detection import logger

STAGE_NAME= "Data ingestion stage"

def main():
    config= ConfigurationManager()
    data_ingestion_config= config.get_data_ingestion_config()
    data_ingestion= DataIngestion(config= data_ingestion_config)
    data_ingestion.copy_dataset_destination(data_ingestion_config.dataset_source, data_ingestion_config.unzip_dir)
    data_ingestion.unzip_and_clean()



if __name__=='__main__':
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<\n\n x===========x")

    except Exception as e:
        logger.exception(e)
        raise e 