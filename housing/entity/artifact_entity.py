from collections import namedtuple

from housing.entity.config_entity import DataTransformationConfig, ModelEvaluationConfig


DataIngestionArtifact = namedtuple("DataIngestionArtifact",[])

DataValidationArtifact = namedtuple("DataValidationArtifact", [])

DataTransformationArtifact = namedtuple("DataTransformationArtifact", [])

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",[])

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact", [])

ModelPusherArtifact = namedtuple("ModelPusherArtifact",[])