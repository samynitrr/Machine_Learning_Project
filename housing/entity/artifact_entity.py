from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact", ["schema_file_path","report_file_path","report_page_file_path","is_validated","is_data_drift_found", "message"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact", [])

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",[])

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact", [])

ModelPusherArtifact = namedtuple("ModelPusherArtifact",[])

TrainingPipelineArtifact = namedtuple("TrainingPipelineArtifact",[])