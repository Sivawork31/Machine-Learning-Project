import os
from mlproject import logger
from sklearn.model_selection import train_test_split
from mlproject.entity.config_entity import DataTransformationConfig
import pandas as pd




class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config

                  #  Note; you can add different data transformation techniques such as scaler, PCA and all
                  #  You can perform all kinds of EDS in ML cycle here before passing this data to the model
                  #  I am only one adding train_test_splitting bcz this data is already cleaned up.....


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets...( 0.75 , 0.25)

        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index= False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)


        logger.info(" Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print( train.shape)
        print( test.shape)
    