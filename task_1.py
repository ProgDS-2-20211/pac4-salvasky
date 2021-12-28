# Importem llibreries
import pandas as pd
from trax import read_data as rd

# Executem el mòdul per descomprimir els fitxers:
rd.import_zip('data/data.zip')

# Transformem els fitxers a dataframes:
artists = pd.read_csv('csv_files/artists_norm.csv', sep=';', converters={"name": lambda x: x.title()})
tracks = pd.read_csv('csv_files/tracks_norm.csv', sep=';')
albums = pd.read_csv('csv_files/albums_norm.csv', sep=';')

# Mostrem els criteris d'acceptació
print("The dataset contains {} tracks".format(rd.count_tracks(tracks)))
print("There were {} tracks in the set that had no popularity score".format(tracks['popularity'].isna().sum()))

# Imputem els valors buits del dataset tracks:
rd.impute(tracks, 'popularity')

# Unim els datasets tracks i albums:
left_merge = pd.merge(tracks, albums, how='left', on=['album_id', 'artist_id'], suffixes=("_track", "_album"))

# Hi afegim el dataset artists:
all_merge = pd.merge(left_merge, artists, how='left', on='artist_id', suffixes=(" ", '_artist'))
all_merge.rename(columns = {'total_tracks':'album_total_tracks', 'name':'artist_name', 'popularity':'artist_popularity',
                            'followers':'artist_followers', 'total_albums':'artist_total_albums'}, inplace = True)

# Exportem el nou fitxer desnormalitzat a csv:
all_merge.to_csv(path_or_buf='data/tracks.csv', sep=';', index=False)
