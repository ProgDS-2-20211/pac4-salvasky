import zipfile as zf

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
        # Iterate over the file names
        for fileName in top:
            # Check filename endswith csv
            if fileName.endswith('.csv'):
                # Extract a single file from zip
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
