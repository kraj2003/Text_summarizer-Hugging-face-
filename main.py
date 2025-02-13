from src.text_summarizer.logging.logger import logging

from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_ingestion import DataIngestion

config=ConfigurationManager()
data_ingestion_config=config.get_data_ingestion_config()
data_ingestion=DataIngestion(config=data_ingestion_config)

data_ingestion.download_file()
data_ingestion.extract_zip_file()