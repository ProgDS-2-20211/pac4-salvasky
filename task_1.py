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

left_merge = pd.merge(tracks, albums, how='left', on=['album_id', 'artist_id'], suffixes=("_track", "_album"))
al = left_merge

all_merge = pd.merge(left_merge, artists, how='left', on='artist_id', suffixes=(" ", '_artist'))
all_merge.rename(columns = {'name':'artist_name', 'popularity':'artist_popularity','followers':'artist_followers',
                            'total_albums':'artist_total_albums'}, inplace = True)
all_m = all_merge


index_l = al.index
merged_l = len(index_l)
index_a = all_merge.index
merged_all = len(index_a)
print(merged_l, merged_all)


#print(aa_merge.to_string())