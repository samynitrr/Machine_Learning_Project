from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path",
                                                            "is_ingested","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact", ["schema_file_path",
                                                                "report_file_path",
                                                                "report_page_file_path",
                                                                "is_validated",
                                                                "is_data_drift_found",
                                                                 "message"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",["is_transformed","message",
                                                                "transformed_train_file_path",
                                                                "transformed_test_file_path",
                                                                "preprocessed_object_file_path"])

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",["is_trained"])

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact", [])

ModelPusherArtifact = namedtuple("ModelPusherArtifact",[])

TrainingPipelineArtifact = namedtuple("TrainingPipelineArtifact",[])