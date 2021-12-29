import pandas as pd
from datetime import date

def artist_name(path, name_artist, sep=';'):
    df = pd.read_csv(path, sep=sep)
    name_count = df[df['artist_name'] == name_artist]

    return len(name_count)


def title_word(path, word, sep=';'):
    df = pd.read_csv(path, sep=sep)
    title = df[df['name_track'].str.contains(word)]

    return len(title)

def release_year(path, decade, sep=';'):
    df = pd.read_csv(path, sep=sep)
    year = df[df['release_year'].between(decade, decade+9)]

    return len(year)


def popular_last(path, years, sep=';'):
    df = pd.read_csv(path, sep=sep)
    current_date = date.today()
    current_year = current_date.year
    year_span = df[df['release_year'].between(current_year-years, current_year)]
    year_span['popularity_track'].idxmax()
    max_pop = year_span.loc[year_span['popularity_track'].idxmax()]
    return max_pop['name_track'], max_pop['artist_name']


def decade_artists(path, decade, sep=';'):
    df = pd.read_csv(path, sep=sep)
    year = df[df['release_year'].between(decade, decade + 9)]
    artists = set(year['artist_name'].to_list())
    return artists