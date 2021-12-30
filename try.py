import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/tracks.csv', sep=';')
art = df[df['artist_name'] == 'Coldplay']
dance = art.groupby('name_album', as_index=False)['danceability'].mean()
print(dance)
print(type(dance))

dance.plot.barh(x='name_album', y= 'danceability', title= 'Coldplay: Danceability by album')

plt.show()