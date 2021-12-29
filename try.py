import pandas as pd
from datetime import date

tracks = pd.read_csv('data/tracks.csv', sep=';')

la = tracks[tracks['artist_name']=='Louis Armstrong']

print(la)


