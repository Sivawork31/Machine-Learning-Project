from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_validation import Datavalidation
from mlproject import logger


STAGE_NAME = "Data Validation stage"

class DatavalidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = Datavalidation(config = data_validation_config)
        data_validation.validate_all_columns()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DatavalidationTrainingPipeline
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<<\n\nx========x")

    except Exception as e:
        logger.exception(e)
        raise e