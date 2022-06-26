from housing.entity.config_entity import ModelPusherConfig
from housing.entity.artifact_entity import ModelPusherArtifact
from housing.exception import HousingException
from housing.logger import logging
import os,sys

class ModelPusher:

    def __init__(self,
    model_pusher_config:ModelPusherConfig):        
        try:
            logging.info(f"{'='*20}Model Pusher log started.{'='*20}")
            self.model_pusher_config= model_pusher_config
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_model_push(self)-> ModelPusherArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e