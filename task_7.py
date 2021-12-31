import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy.spatial import distance

df = pd.read_csv('data/tracks.csv', sep=';')
vec = df.groupby('artist_name', as_index=False)[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
                                                 'acousticness', 'instrumentalness', 'liveness', 'valence',
                                                 'tempo', 'time_signature']].mean()

met_vec = vec[vec['artist_name'] == 'Metallica']
AC_vec = vec[vec['artist_name'] == 'Ac/Dc']
ext_vec = vec[vec['artist_name'] == 'Extremoduro']
hans_vec = vec[vec['artist_name'] == 'Hans Zimmer']
datas = [met_vec, AC_vec, ext_vec, hans_vec]

turn = vec.T
names = turn.rename(columns=turn.iloc[0])
matrix_ready = names.drop('artist_name', axis=0)

met = met_vec.drop('artist_name', axis=1)
AC = AC_vec.drop('artist_name', axis=1)
ext = ext_vec.drop('artist_name', axis=1)
hans = hans_vec.drop('artist_name', axis=1)

Metallica = met.values.tolist()[0]
AC_DC = AC.values.tolist()[0]
Extremoduro = ext.values.tolist()[0]
Hans_Zimmer = hans.values.tolist()[0]





print(Metallica)
print(AC_DC)
print(Extremoduro)
print(Hans_Zimmer)

print(distance.euclidean(Metallica, AC_DC))

coords = [Metallica, AC_DC, Extremoduro, Hans_Zimmer]

euclid = distance.cdist(coords, coords, 'euclidean')

print(euclid)
column_names = ['Metallica', 'AC/DC', 'Extremoduro', 'Hans Zimmer']
euclid_distance = pd.DataFrame(euclid, columns=column_names, index=column_names)

print(euclid_distance)


mask = np.zeros_like(euclid_distance, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(euclid_distance, mask=mask, cmap='Blues')
plt.title('Euclid distance')
plt.show()


"""

frame = pd.concat(datas)
artist_frame = frame.set_index('artist_name')

matrix = scipy.spatial.distance_matrix(met_vec, AC_vec, ext_vec, hans_vec)
print(matrix)
"""

