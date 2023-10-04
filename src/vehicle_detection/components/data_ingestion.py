from collections import namedtuple
import os
from vehicle_detection import logger
from zipfile import ZipFile
import shutil
from vehicle_detection.entity import DataIngestionConfig
from pathlib import Path

## Data Ingestion component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config= config
    def _preprocess(self, zf: ZipFile, f:str, working_dir:str):
        """places all files into target folder
           ignores files which has size of zero

        Args:
            zf (ZipFile): Zip file
            f (str): file name with path
            working_dir (str): targer working directory
        """
        target_filepath= os.path.join(working_dir, f)
        dir_name= os.path.dirname(target_filepath)
        #print(f"filepath: {f}")
        
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)##Create file folder
        print(f"target file path: {target_filepath}")
        
        
        
        ##If the folder has size of zero then delete.
        if os.path.getsize(target_filepath)==0:
            os.remove(target_filepath)
    def copy_dataset_destination(self, source: Path, destination: Path):
        ###Copy dataset into Data ingestion folder
        shutil.copy2(source, destination)
        
    def unzip_and_clean(self):
        """unzip the dataset and clean the files 
           which has zero size
        """
        ##print(self.config.local_data_file)
        with ZipFile(file= self.config.local_data_file, mode="r") as zf:
            ##Getting the list of files available.
            list_of_files= zf.namelist()
            zf.extractall(self.config.unzip_dir)

            ##extracting files that has only filename dataset
            '''for f in list_of_files:
                self._preprocess(zf, f, self.config.unzip_dir)'''