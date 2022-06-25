from housing.entity.config_entity import DataValidationConfig,DataValidationArtifact
from housing.exception import HousingException
from housing.logger import logging
import os,sys

class DataValidation:

    def __init__(self,
    data_validation_config:DataValidationConfig):        
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20}")
            self.data_validation_config= data_validation_config
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e