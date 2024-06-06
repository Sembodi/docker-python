import csv
import os
from typing import List

def write_csv_file(file_name: str, headers: List[str], rows: List[List[str]], additional_path: str = "") -> None:
    """ This function writes the specified headers and rows of data to a csv file.

    Args:
        file_name (str): Name of the csv file.
        headers (List[str]): Headers of the columns.
        rows (List[List[str]]): Rows containing the data of the specified headers.
    """
    folder_path = "./data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    with open("./data/" + additional_path + file_name + ".csv", mode='w' ,newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(headers)
        
        writer.writerows(rows)