### Creating skeletons of projcet.
import os
from pathlib import Path ## helps in creating paths (manages forward and backward slashes while creating folders)
##logging
import logging
##Defining logging configuration
logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: [%(message)s]')
project_name= "vehicle_detection"

##Create llist of files
list_of_files=[
    ".github/workflows/.gitkeep",##For CI/CD pipelines
    ###Src (Script folder)
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",## Data version control pipeline
    "params.yaml",
    "init_setup.sh", # Helps in create environment and install required packages
    "requirements.txt",
    "requirements_dev.txt", ## For development purpose
    "setup.py",
    "setup.cfg",
    "pyproject.toml",## For Python package creation
    "tox.ini",##Testing project locally
    "reseearch/stage_01.ipynb"##Jupyter notebook
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

]

##Create files
for filepath in list_of_files:
    filepath= Path(filepath)
    ##Extracting folder path from entire path
    file_dir, filename=os.path.split(filepath)
    print(filepath, file_dir)
    ## When there is not file directory which means it is a file name then do not create directory
    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory:  {file_dir} for file: {filename}")
    
    ##Creating files inside directory
    if not(os.path.exists(filepath)) or (os.path.getsize==0):
        with open(filepath, "w") as f:
            logging.info("Create empty file for {filename}")
            pass
    else:
        logging.info(f"{filename} already exists")