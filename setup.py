from setuptools import setup, find_packages
from typing import List



# Declaring variables for setup function
PROJECT_NAME="housing-price-predictor"
VERSION="0.0.3"
AUTHOR="Sameer Shekhar"
DESCRIPTION="This is a housing price predictor machine learning Project."
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()-> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file.

    return: This function is going to return a list which will contain
    the name of libraries mentioned in the requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()

setup(
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

