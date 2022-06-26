import os, sys

from housing.logger import logging
from housing.exception import HousingException

from housing.config.configuration import Configuration

from housing.entity.artifact_entity import *
from housing.entity.config_entity import *

from housing.component.data_ingestion import DataIngestion
from housing.component.data_validation import DataValidation
from housing.component.data_transformation import DataTransformation
from housing.component.model_trainer import ModelTrainer
from housing.component.model_evaluation import ModelEvaluation
from housing.component.model_pusher import ModelPusher

class Pipeline:

    def __init__(self, config: Configuration = Configuration)-> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
             
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_validation(self)-> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config())
            return data_validation.initiate_data_validation()
             
        except Exception as e:
            raise HousingException(e, sys) from e


    def start_data_transformation(self)-> DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(data_transformation_config=self.config.get_data_transformation_config())
            return data_transformation.initiate_data_transformation()
             
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_model_training(self)-> ModelTrainerArtifact:
        try:
            model_training = ModelTrainer(model_trainer_config=self.config.get_model_trainer_config())
            return model_training.initiate_model_training()
             
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_model_evaluation(self)-> ModelEvaluationArtifact:
        try:
            model_evaluation = ModelEvaluation(model_evaluation_config=self.config.get_model_evaluation_config())
            return model_evaluation.initiate_model_evaluation()
             
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_model_push(self)-> ModelPusherArtifact:
        try:
            model_push = ModelPusher(model_pusher_config=self.config.get_model_pusher_config())
            return model_push.initiate_model_push()
             
        except Exception as e:
            raise HousingException(e, sys) from e


    def run_pipeline(self)-> TrainingPipelineArtifact:
        try:
            #data ingestion
            logging.info(f"Data Ingested")
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation()
            data_transformation_artifact = self.start_data_transformation()

            model_train_artifact = self.start_model_training()
            model_evaluation_artifact = self.start_model_evaluation()
            model_push_artifact = self.start_model_push()
            pass
        except Exception as e:
            raise HousingException(e, sys) from e