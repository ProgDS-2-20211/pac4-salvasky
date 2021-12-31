# Importem mòdul:
from trax import times as t

# Creem dues llistes buides:
pandas_list = []
csv_list = []

# Utilitzem mòdul per extreure una columna de cada dataset amb pandas:
pandas_albums = t.get_column_pandas('csv_files/albums_norm.csv', 'album_id')
pandas_artists = t.get_column_pandas('csv_files/artists_norm.csv', 'artist_id')
pandas_tracks = t.get_column_pandas('csv_files/tracks_norm.csv', 'track_id')

# Fem el mateix amb read.csv:
csv_albums = t.get_column_csv('csv_files/albums_norm.csv', 'album_id')
csv_artists = t.get_column_csv('csv_files/artists_norm.csv', 'artist_id')
csv_tracks = t.get_column_csv('csv_files/tracks_norm.csv', 'track_id')

# Afegim només els temps i mida de l'arxiu a les llistes:
# (No mostrem les llistes per pantalla)
pandas_list.append([pandas_artists[:2], pandas_albums[:2], pandas_tracks[:2]])
csv_list.append([csv_artists[:2], csv_albums[:2], csv_tracks[:2]])

# Mostrem els valors:
print(pandas_list)
print(csv_list)

# Mostrem el gràfic:
t.plot_times(pandas_list, csv_list)
