import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from trax import read_data as rd
from trax import distances as ds


Metallica = rd.audio_f_list('data/tracks.csv', 'Metallica')
AC_DC = rd.audio_f_list('data/tracks.csv', 'Ac/Dc')
Extremoduro = rd.audio_f_list('data/tracks.csv', 'Extremoduro')
Hans_Zimmer = rd.audio_f_list('data/tracks.csv', 'Hans Zimmer')

coords = [Metallica, AC_DC, Extremoduro, Hans_Zimmer]

euclid = ds.distances(coords, 'euclidean')
cosine = ds.distances(coords, 'cosine')

column_names = ['Metallica', 'AC/DC', 'Extremoduro', 'Hans Zimmer']
euclid_distance = pd.DataFrame(euclid, columns=column_names, index=column_names)
cosine_distance = pd.DataFrame(cosine, columns=column_names, index=column_names)

print(euclid_distance)
print(cosine_distance)

fig, ax = plt.subplots(1,2)
mask = np.zeros_like(euclid_distance, dtype=bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(euclid_distance, mask=mask, cmap='Reds', ax=ax[0])
sns.heatmap(cosine_distance, mask=mask, cmap='Blues', ax=ax[1])
ax[0].set_title('Euclid distance')
ax[1].set_title('Cosine Distance')
plt.show()
