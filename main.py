from src.text_summarizer.logging.logger import logging

from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_ingestion import DataIngestion
from src.text_summarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logging.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logging.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logging.exception(e)
    raise e