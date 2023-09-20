### Setting up the basic structure of the project like name, repo name author etc.,
import setuptools
##Get the description of project from readme.
with open("README.md", 'r', encoding="utf-8") as readme:
    long_description= readme.read()

__version__="0.0.0"##Whenever we run or u pload the changes into cloud then the version has to be changed

REPO_NAME="vehicle_detection_yolo"
AUTHOR_USER_NAME="vikaslakkacs"
SRC_REPO= "vehicle_detection"
AUTHOR_EMAIL="vikaslakkacs@gmail.com"


##Setup tools
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "Detection vehicles(mostly cars from video)",
    Long_description= long_description,
    Long_description_content='text/markdown',
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src")
)