from housing.entity.config_entity import ModelTrainerConfig
from housing.entity.artifact_entity import ModelTrainerArtifact
from housing.exception import HousingException
from housing.logger import logging
import os,sys

class ModelTrainer:

    def __init__(self,
    model_trainer_config:ModelTrainerConfig):        
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20}")
            self.model_trainer_config= model_trainer_config
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_model_training(self)-> ModelTrainerArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e