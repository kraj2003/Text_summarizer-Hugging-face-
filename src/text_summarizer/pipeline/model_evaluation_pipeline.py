from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_evaluation import ModelEvaluation
from src.text_summarizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation= ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()