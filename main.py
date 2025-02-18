from src.text_summarizer.logging.logger import logging

from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_ingestion import DataIngestion
from src.text_summarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logging.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logging.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"

try:
    logging.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationTrainingPipeline()
    data_transformation_pipeline.inititate_data_transformation()
    logging.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME="Model Trainer Stage"

try:
    logging.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logging.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logging.exception(e)
    raise e