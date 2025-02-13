import os
import logging
import sys

logging_str="['%(asctime)s - %(name)s - %(levelname)s - %(message)s']"

log_dir="logs"

log_filepath=os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("Text_summarizer")