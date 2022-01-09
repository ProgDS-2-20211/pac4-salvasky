
from trax import api

artist = ['radiohead', 'david bowie', 'maneskin']

data_a = api.api_r(artist)
print(data_a)

# La resta de codi té com a objectiu ampliar el dataframe amb tots
# els artistes del dataset artists_norm.csv
# de moment aquest codi resulta en error, no he desxifrat el perquè:

"""

list_artists = ss.all_artists('csv_files/artists_norm.csv')

print(list_artists)
lower_list = []
for i in (list_artists):
    unaccented = unidecode.unidecode(i)
    lower_list.append(unaccented.lower().replace('&', 'and').replace('. ','.').replace(' y ', ' y los '))

print(lower_list)
data_b = api.api_r(lower_list)
print(data_b)

"""