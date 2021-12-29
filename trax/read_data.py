import zipfile as zf
import pandas as pd
import csv
import time

def import_zip(path):
    """
    Decompresses zip files
    only from top level of directory,
    skipping subdirectories.
    Creates a new folder to host
    the files.
    :param path: location of the zip folder
    """
    with zf.ZipFile(path, 'r') as zip_f:
        top = {item.split('/')[0] for item in zip_f.namelist()}
        # Iterem sobre els fitxers:
        for fileName in top:
            # Localitzem fitxers amb extensió csv
            if fileName.endswith('.csv'):
                # Descomprimim els fitxers:
                zip_f.extract(fileName, 'csv_files')


def count_tracks(df):
    """
    Counts number of entries in dataset
    :param df: name of dataset
    :return: int
    """
    index_df = df.index
    number_of_tracks = len(index_df)
    return number_of_tracks


def impute(dataframe, column):
    """
    Imputes empty values using column mean value
    :param dataframe: dataset to impute
    :param column: column name to impute
    """
    dataframe[column] = dataframe[column].fillna(dataframe[column].mean())


def get_column_pandas(path, column):
    """
    :param path:
    :param column:
    :rtype: list
    """
    start_time = time.time()
    col_df = pd.read_csv(path , sep=';', usecols=[column])
    col_l = col_df[column].to_list()
    stop_time = time.time()
    execution_time = stop_time - start_time
    return execution_time, len(col_l), col_l

def get_column_csv(path, column):
    start_time = time.time()
    with open(path, 'r') as file:
        list_c = list(i[column] for i in csv.DictReader(file, delimiter=';'))
    stop_time = time.time()
    execution_time = stop_time - start_time
    return execution_time, len(list_c), list_c
