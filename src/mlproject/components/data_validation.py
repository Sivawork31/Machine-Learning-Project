import os
from mlproject import logger
from mlproject.entity.config_entity import DatavalidationConfig
import pandas as pd



class Datavalidation:
    def __init__(self, config:DatavalidationConfig):
        self.config = config


    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()


            for col in all_cols:
                if col  not in  all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")


            
            with open(self.config.STATUS_FILE,'w') as f:
                    f.write(f"Validation status: {validation_status}")
                        
            return  validation_status
        
        
        
        except Exception as e:
            raise e