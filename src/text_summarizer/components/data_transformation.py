import os
from src.text_summarizer.logging.logger import logging
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.text_summarizer.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config=DataTransformationConfig):
        self.config=config
        self.tokennizer=AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        input_encoding=self.tokennizer(example_batch['dialogue'],max_length=1024,truncation=True)

        with self.tokennizer.as_target_tokenizer():
            target_encodings=self.tokennizer(example_batch['summary'],max_length=128,truncation=True)

        return {
            'input_ids':input_encoding['input_ids'],
            "attention_mask":input_encoding['attention_mask'],
            "labels":target_encodings['input_ids']
        }
    def convert(self):
        dataset_samsum= load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))
