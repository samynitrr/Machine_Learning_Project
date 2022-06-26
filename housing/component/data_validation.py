from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataValidationArtifact
from housing.exception import HousingException
from housing.logger import logging
import os,sys
import pandas as pd

from housing.util.util import read_yaml_file

class DataValidation:

    def __init__(self,
    data_validation_config:DataValidationConfig):        
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20}")
            self.data_validation_config= data_validation_config
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
    def train_file_exists(self)-> bool:
        pass
    def test_file_exists(self)-> bool:
        pass
    
    def generate_schema_file(self,file_path:str)->dict:
        """
        Reads a data file and returns the schema as a dictionary.
        file_path: str
        """
        try:
            df = pd.read_csv(file_path)
            columns = df.columns
            data_types = list(map(lambda x:str(x).replace("dtype('","").replace("')",""), df.dtypes))
            schema = {"columns": dict(zip(columns,data_types))}
            return schema 
        except Exception as e:
            raise HousingException(e,sys) from e

    def read_existing_schema_file(self):
        read_yaml_file()
        pass

    def schema_match(self):
        pass

    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Validation log completed.{'='*20}")