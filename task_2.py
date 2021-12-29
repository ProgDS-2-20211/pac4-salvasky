from trax import read_data as rd

id_album = rd.get_column_pandas('csv_files/albums_norm.csv', 'album_id')
id_artist = rd.get_column_pandas('csv_files/artists_norm.csv', 'artist_id')
id_tracks = rd.get_column_pandas('csv_files/tracks_norm.csv', 'track_id')

