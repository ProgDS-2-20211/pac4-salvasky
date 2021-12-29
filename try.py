from trax import timing as t
from trax import read_data as rd


time_albums_pandas = t.timing_call(rd.get_column_pandas('csv_files/albums_norm.csv', 'album_id'))
time_artists_pandas = t.timing_call(rd.get_column_pandas('csv_files/artists_norm.csv', 'artist_id'))
time_tracks_pandas = t.timing_call(rd.get_column_pandas('csv_files/tracks_norm.csv', 'track_id'))


time_albums_csv = t.timing_call(rd.get_column_csv('csv_files/artists_norm.csv', 'artist_id'))
time_artists_csv = t.timing_call(rd.get_column_csv('csv_files/artists_norm.csv', 'artist_id'))
time_tracks_csv = t.timing_call(rd.get_column_csv('csv_files/artists_norm.csv', 'artist_id'))

print(f"The execution time for the pandas function on artists is {time_artist_csv}")
print(f"The execution time for the csv function on artists is {time_artist_csv}")

print(f"The execution time for the pandas function on artists is {time_artist_csv}")
print(f"The execution time for the csv function on artists is {time_artist_csv}")

print(f"The execution time for the pandas function on artists is {time_artist_csv}")
print(f"The execution time for the csv function on artists is {time_artist_csv}")
