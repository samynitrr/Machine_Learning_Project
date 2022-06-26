from housing.entity.config_entity import DataTransformationConfig
from housing.entity.artifact_entity import DataTransformationArtifact
from housing.exception import HousingException
from housing.logger import logging
import os,sys

class DataTransformation:

    def __init__(self,
    data_transformation_config:DataTransformationConfig):        
        try:
            logging.info(f"{'='*20}Data Transformation log started.{'='*20}")
            self.data_transformation_config= data_transformation_config
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Transformation log completed.{'='*20}")