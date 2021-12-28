import zipfile as zf
import os
import pandas as pd

def import_zip(path):
    """

    :rtype: info
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
    index_df = df.index
    number_of_tracks = len(index_df)
    return number_of_tracks

