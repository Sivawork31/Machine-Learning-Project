from src.mlproject import logger

from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from mlproject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline


from mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

from mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


# Data ingestion stage :

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e


# Data validation stage:



STAGE_NAME = "Data validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>>")
    data_ingestion = DatavalidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>\n\nx============x")

except Exception as e:
        logger.exception(e)
        raise e




#Data Transformation:



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<< \n\n x==========x")


except Exception as e:
        logger.exception(e)
        raise e


# Model Training:


STAGE_NAME = "Model Trainer Stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<< \n\n x==========x")
    

except Exception as e:
        logger.exception(e)
        raise e
