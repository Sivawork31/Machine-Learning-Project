from src.mlproject import logger

from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from mlproject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e








STAGE_NAME = "Data validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>>")
    data_ingestion = DatavalidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e


