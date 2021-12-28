import pandas as pd

from trax import read_data as rd

rd.import_zip('data/data.zip')

artists = pd.read_csv('csv_files/artists_norm.csv', sep=';', converters={"name": lambda x: x.title()})

print(artists.to_string())
