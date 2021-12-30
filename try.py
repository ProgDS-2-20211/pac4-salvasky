import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('data/tracks.csv', sep=';')
ad = df[(df['artist_name'] == 'Adele') | (df['artist_name'] == 'Extremoduro')]
sns.displot(ad, x='energy', hue='artist_name', stat= 'density', kde=True)
plt.show()
