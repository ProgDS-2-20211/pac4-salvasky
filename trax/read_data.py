import zipfile as zf
import pandas as pd

def import_zip(path):
    """

    :rtype: info
    """
    with zf.ZipFile(path, 'r') as zip_f:
       # Get a list of all archived file names from the zip
       file_list = zip_f.namelist()
       print(zip_f.printdir())
       # Iterate over the file names
       for fileName in file_list:
           # Check filename endswith csv
           if fileName.endswith('.csv'):
               # Extract a single file from zip
               zip_f.extract(fileName, 'csv_files')