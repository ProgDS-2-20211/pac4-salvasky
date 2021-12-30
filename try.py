import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('data/tracks.csv', sep=';')
art = df[df['artist_name'] == 'Ed Sheeran']

sns.displot(art, x='acousticness', stat= 'probability').set(title='Ed')
plt.show()