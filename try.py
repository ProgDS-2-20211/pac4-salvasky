import pandas as pd
from datetime import date

tracks = pd.read_csv('data/tracks.csv', sep=';')

years = 10
current_date = date.today()
current_year = current_date.year
year_span = tracks[tracks['release_year'].between(current_year-years, current_year)]
max_p = year_span['popularity_track'].idxmin()
max_pop = year_span.iloc[year_span['popularity_track'].idxmin()]

print(max_pop)


