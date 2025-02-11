from pathlib import Path

from pandas import read_csv

PATH_OBJ_TO_TEST_DATA = Path(__file__).parent/"test_data"

def get_test_dataframe(filename: str):
    path_to_file = str(PATH_OBJ_TO_TEST_DATA/filename)
    result = read_csv(path_to_file)
    return result