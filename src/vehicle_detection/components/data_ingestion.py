from collections import namedtuple
import os
from vehicle_detection import logger
from zipfile import ZipFile
import shutil
from vehicle_detection.entity import DataIngestionConfig
from pathlib import Path
##Co-ordinate conversion
import pybboxes as pbx
import pandas as pd

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

    def boundingbox_conversion_YOLO(self):
        """conversion of normal co-ordinates 
            to coordinates that yolo understands"""
        config= self.config
        ## Read the coordinates for conversion
        ##Load data with pandas
        dataresult= pd.read_csv(config.coordinates_path)
        logger.info("co-ordinates file has opened")
        ##Getting coordinates of each pic and convert
        logger.info("looping around co-ordinates")
        for dfrow in range(len(dataresult)):
            ## Text to list conversion
            #coordinates= coordinates.split(',')
            ## Looping around co-ordinates for conversion
            image_name= dataresult['image'][dfrow]
            logger.info(f"finding co-ordinates for image: {image_name}")
            object_code=0## default to 0 as there is only one detector
            object_coordinates= [dataresult['xmin'][dfrow], dataresult['ymin'][dfrow],
                          dataresult['xmax'][dfrow], dataresult['ymax'][dfrow] ]
            ##Creating new text file with image file name and adding the coordinates
            image_path= os.path.join(config.coordinates_target_path, image_name.replace('.jpg', '.txt'))
            ## If the file exists then append(when there are multiple detections) the coordinates else create new file
            if os.path.exists(image_path):
                write_mode='a'
            else:
                write_mode='w'
            ## IF there are multiple coordinates in an image then append
            ## 0 means car in this case. If there are multiple detectors then the number changes accordingly
            if os.path.exists(image_path):
                classification_code= '\n0 '
            else:
                classification_code='0 '
            ##Write the coordinates into file
            with open(image_path, write_mode) as imagefile:
                ##Conversion of coordinates from string to number
                ## Last coordinates has \n so trimming it using rstrip
                #str_to_val_coordinates= [float(num.rstrip('\n')) for num in object_coordinates]
                str_to_val_coordinates= [float(num) for num in object_coordinates]
                yolo_coordinates= pbx.convert_bbox(str_to_val_coordinates, from_type='voc', to_type='yolo', image_size= config.yolo_conversion_image_size)
                logger.info(f"yolo co-ordinates for image:{image_name} are {yolo_coordinates}")
                imagefile.write(classification_code)
                imagefile.write(' '.join([str(num) for num in yolo_coordinates]))