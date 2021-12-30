from trax import subset as ss

# Definim variables utilitzant el mòdul subset:
radiohead = ss.artist_name('data/tracks.csv', 'Radiohead')

police = ss.title_word('data/tracks.csv', 'police|Police')

year = ss.release_year('data/tracks.csv', 1990)

pop = ss.popular_last('data/tracks.csv', 10)

# Trobem artistes amb tracks a cada dàcada:
a_60 = ss.decade_artists('data/tracks.csv', 1960)
a_70 = ss.decade_artists('data/tracks.csv', 1970)
a_80 = ss.decade_artists('data/tracks.csv', 1980)
a_90 = ss.decade_artists('data/tracks.csv', 1990)
a_00 = ss.decade_artists('data/tracks.csv', 2000)
a_10 = ss.decade_artists('data/tracks.csv', 2010)
a_20 = ss.decade_artists('data/tracks.csv', 2020)

# Reduïm a un sol set dels artistes presents
# a totes les dècades:
intergeneration_artist = a_60.intersection(a_70, a_80, a_90, a_00, a_10, a_20)

# Mostrem tots els resultats per pantalla:
print(f"There are {radiohead} tracks from artist Radiohead")

print(f"There are {police} track titles with the word \'police\' in them")

print(f"There are {year} tracks from albums published in the nineties")

print(f"The most popular track in the last 10 years is {pop[0]}, by {pop[1]}")

print(f"The artists whose tracks are published in every decade since 1960 are: {intergeneration_artist}")
