from trax import read_data as rd
import matplotlib.pyplot as plt

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

xs = [2135, 68, 35574]
ys_pandas, ys_csv = [], []

ys_pandas.append(pandas_albums[0])
ys_csv.append(csv_albums[0])
ys_pandas.append(pandas_artists[0])
ys_csv.append(csv_artists[0])
ys_pandas.append(pandas_tracks[0])
ys_csv.append(csv_tracks[0])

plt.figure()
plt.plot(xs, ys_pandas, xs, ys_csv)
plt.legend(["Set", "List"])
plt.xlabel('$n$')
plt.ylabel('$t(n)$')
plt.title("Execution time of membership test")
plt.show()

#print(ys_pandas, ys_csv)