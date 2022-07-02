import yaml
from housing.exception import HousingException
import os,sys
def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise HousingException(e,sys) from e

# def generate_schema_file(self,file_path:str)->dict:
#         """
#         Reads a data file and returns the schema as a dictionary.
#         file_path: str
#         """
#         try:
#             df = pd.read_csv(file_path)
#             columns = df.columns
#             data_types = list(map(lambda x:str(x).replace("dtype('","").replace("')",""), df.dtypes.values))
#             schema = {"columns": dict(zip(columns,data_types))}
#             return schema 
#         except Exception as e:
#             raise HousingException(e,sys) from e



