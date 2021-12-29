from trax import read_data as rd

pandas_albums = rd.get_column_pandas('csv_files/albums_norm.csv', 'album_id')
pandas_artists = rd.get_column_pandas('csv_files/artists_norm.csv', 'artist_id')
pandas_tracks = rd.get_column_pandas('csv_files/tracks_norm.csv', 'track_id')

csv_albums = rd.get_column_csv('csv_files/albums_norm.csv', 'album_id')
csv_artists = rd.get_column_csv('csv_files/artists_norm.csv', 'artist_id')
csv_tracks = rd.get_column_csv('csv_files/tracks_norm.csv', 'track_id')

print(pandas_albums[:2])
print(csv_albums[:2])
print(pandas_artists[:2])
print(csv_artists[:2])
print(pandas_tracks[:2])
print(csv_tracks[:2])

