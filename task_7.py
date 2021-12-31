import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from trax import read_data as rd
from trax import distances as ds

# Calculem les mitjanes de cada audio feature per cada artista
# i emmagatzem els resultats en llistes
Metallica = rd.audio_f_list('data/tracks.csv', 'Metallica')
AC_DC = rd.audio_f_list('data/tracks.csv', 'Ac/Dc')
Extremoduro = rd.audio_f_list('data/tracks.csv', 'Extremoduro')
Hans_Zimmer = rd.audio_f_list('data/tracks.csv', 'Hans Zimmer')

# Creem una llista de llistes:
coords = [Metallica, AC_DC, Extremoduro, Hans_Zimmer]

# Calculem distàncies a partir de les llistes.
# El resultat és un array en cada cas:
euclid = ds.distances(coords, 'euclidean')
cosine = ds.distances(coords, 'cosine')

# Transformem els arrays en dataframes:
column_names = ['Metallica', 'AC/DC', 'Extremoduro', 'Hans Zimmer']
euclid_distance = pd.DataFrame(euclid, columns=column_names, index=column_names)
cosine_distance = pd.DataFrame(cosine, columns=column_names, index=column_names)

# Mostrem els dos dataframes per pantalla:
print(euclid_distance)
print(cosine_distance)

# Elaborem els gràfics:
fig, ax = plt.subplots(1,2)
mask = np.zeros_like(euclid_distance, dtype=bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(euclid_distance, mask=mask, cmap='Reds', ax=ax[0])
sns.heatmap(cosine_distance, mask=mask, cmap='Blues', ax=ax[1])
ax[0].set_title('Similarity: Euclidean')
ax[1].set_title('Similarity: Cosine')
plt.show()
