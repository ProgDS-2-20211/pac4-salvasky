import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('data/tracks.csv', sep=';')
vec = df.groupby('artist_name', as_index=False)[['energy', 'key', 'loudness']].mean()
#met_vec = vec.loc['Metallica', : ]
#AC_vec = vec.loc['Ac/Dc', :]
met_vec = vec[vec['artist_name'] == 'Metallica']
AC_vec = vec[vec['artist_name'] == 'Ac/Dc']
datas = [met_vec, AC_vec]

frame = pd.concat(datas)
artist_frame = frame.set_index('artist_name')

print(artist_frame)

