import pandas as pd

from trax import read_data as rd

rd.import_zip('data/data.zip')

artists = pd.read_csv('csv_files/artists_norm.csv', sep=';', converters={"name": lambda x: x.title()})
tracks = pd.read_csv('csv_files/tracks_norm.csv', sep=';')
albums = pd.read_csv('csv_files/albums_norm.csv', sep=';')

print("The dataset contains {} tracks".format(rd.count_tracks(tracks)))
print("There were {} tracks in the set that had no popularity score".format(tracks['popularity'].isna().sum()))

tracks['popularity'] = tracks['popularity'].fillna(tracks['popularity'].mean())

left_merge = pd.merge(tracks, albums, how='left', on=['album_id', 'artist_id'], suffixes=("_track", "_album"))
al = left_merge

all_merge = pd.merge(left_merge, artists, how='left', on='artist_id', suffixes=(" ", '_artist'))
all_merge.rename(columns = {'name':'artist_name', 'popularity':'artist_popularity','followers':'artist_followers',
                            'total_albums':'artist_total_albums'}, inplace = True)
all_m = all_merge

all_m.to_csv(path_or_buf='data/tracks.csv', sep=';', index=False)

index_l = al.index
merged_l = len(index_l)
index_a = all_merge.index
merged_all = len(index_a)
print(merged_l, merged_all)


#print(aa_merge.to_string())