from trax import subset as ss

radiohead = ss.artist_name('data/tracks.csv', 'Radiohead')

police = ss.title_word('data/tracks.csv', 'police|Police')

year = ss.release_year('data/tracks.csv', 1990)

pop = ss.popular_last('data/tracks.csv', 10)

print(f"There are {radiohead} tracks from artist Radiohead")

print(f"There are {police} track titles with the word \'police\' in them")

print(f"There are {year} tracks from albums published in the nineties")

print(pop)