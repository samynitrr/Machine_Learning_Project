
from tkinter import E
from housing.constant import SCHEMA_FILE_PATH
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_validation import DataValidation
from housing.component.data_ingestion import DataIngestion
from housing.util.util import read_yaml_file, generate_and_save_schema_file
import pandas as pd
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # print(Configuration().get_data_transformation_config())
        # raw_file_path = "/Users/sameershekhar/Documents/Machine_Learning_Projects/MLE2EProject/Machine_Learning_Project/housing/artifact/data_ingestion/2022-06-26 12:36:57/raw_data/housing.csv"
        # target_column_name = "median_house_vlaue"
        # generate_and_save_schema_file(data_file_path = raw_file_path, target_column_name=target_column_name)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

# def main():
#     try:
#         # self = DataValidation()
#         validation_status = False
#         # Read Schema information
#         schema_info = read_yaml_file(SCHEMA_FILE_PATH)
#         schema_columns = list(schema_info["columns"].keys())
#         schema_domain_values = list(schema_info["domain_value"]["ocean_proximity"])
#         print(type(schema_domain_values), schema_domain_values)
#         schema_number_of_columns = len(schema_columns)

#         # Read Train and Test file
#         df_train = pd.read_csv('/Users/sameershekhar/Documents/Machine_Learning_Projects/MLE2EProject/Machine_Learning_Project/housing/artifact/data_ingestion/2022-07-02 13:54:51/ingested_data/train/housing.csv')
#         df_test = pd.read_csv('/Users/sameershekhar/Documents/Machine_Learning_Projects/MLE2EProject/Machine_Learning_Project/housing/artifact/data_ingestion/2022-07-02 13:54:51/ingested_data/test/housing.csv')

#         # Read Train File information
#         train_columns = list(df_train.columns)
#         train_no_of_columns = len(train_columns)
#         train_domain_values = list(df_train["ocean_proximity"].value_counts().index)
#         print(type(train_domain_values), train_domain_values)

#         # Read Test file information
#         test_columns = list(df_test.columns)
#         test_no_of_columns = len(test_columns)
#         test_domain_values = list(df_test["ocean_proximity"].value_counts().index)
#         print(type(test_domain_values), test_domain_values)

#         # 1. Number of Columns            
#         is_number_of_columns_match = (schema_number_of_columns == train_no_of_columns)\
#                                         and \
#                                     (schema_number_of_columns == test_no_of_columns)
                    

#         # 2. Name of Columns
#         schema_columns.sort()
#         train_columns.sort()
#         test_columns.sort()
#         if (schema_columns == train_columns) and (schema_columns == test_columns):
#             is_name_of_columns_match = True
#         else:
#             is_name_of_columns_match = False

#         # 3. Ocean_proximity values
#         schema_domain_values.sort()
#         train_domain_values.sort()
#         test_domain_values.sort()
#         if (schema_domain_values == train_domain_values) and (schema_domain_values == test_domain_values):
#             is_domain_value_match = True
#         else:
#             is_domain_value_match = False
#         if not is_domain_value_match:
#             pass           


#         validation_status = is_number_of_columns_match and is_name_of_columns_match and is_domain_value_match
#         print(validation_status)
#         return validation_status
#     except Exception as e:
#         logging.error(e)
#         print(e)

if __name__ == "__main__":
    main()