from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact", [])

DataTransformationArtifact = namedtuple("DataTransformationArtifact", [])

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",[])

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact", [])

ModelPusherArtifact = namedtuple("ModelPusherArtifact",[])

TrainingPipelineArtifact = namedtuple("TrainingPipelineArtifact",[])