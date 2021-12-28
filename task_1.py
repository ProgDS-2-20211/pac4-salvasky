import pandas as pd

from trax import read_data as rd

rd.import_zip('data/data.zip')

artists = pd.read_csv('csv_files/artists_norm.csv', sep=';', converters={"name": lambda x: x.title()})
tracks = pd.read_csv('csv_files/tracks_norm.csv', sep=';')
albums = pd.read_csv('csv_files/albums_norm.csv', sep=';')

index_t = tracks.index
number_of_tracks = len(index_t)
empty = tracks['popularity'].isna().sum()

print(f"The dataset contains {number_of_tracks} tracks")
print(f"There were {empty} tracks in the set that have no popularity score")

right_merge = pd.merge(tracks, albums, on='album_id', suffixes=("_track", "_album"))
aa = right_merge

index_m = aa.index
merged_number = len(index_m)

print(merged_number)


#print(aa_merge.to_string())