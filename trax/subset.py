import pandas as pd
from datetime import date


def artist_name(path, name_artist, sep=';'):
    """
    Finds tracks from specific artist
    :param path: path to dataset file
    :param name_artist: name of the artist
    :param sep: separator in csv file
    :return: amount of tracks by artist
    """
    df = pd.read_csv(path, sep=sep)
    name_count = df[df['artist_name'] == name_artist]

    return len(name_count)


def title_word(path, word, sep=';'):
    """
    Finds titles containing specific substring
    :param path: path to dataset file
    :param word: substring to search
    :param sep: separator in csv file
    :return: amount of tracks containing substring
    """
    df = pd.read_csv(path, sep=sep)
    title = df[df['name_track'].str.contains(word)]

    return len(title)


def release_year(path, decade, sep=';'):
    """
    Finds tracks in specific decade.
    Defines decade as 10 years starting from
    any given year.
    :param path: path to dataset file
    :param decade: single year that starts decade
    :param sep: separator in csv file
    :return: amount of tracks in year
    """
    df = pd.read_csv(path, sep=sep)
    year = df[df['release_year'].between(decade, decade + 9)]

    return len(year)


def popular_last(path, years, sep=';'):
    """
    Finds most popular artist in a span of past years,
    starting from current date.
    :param path: path to dataset file
    :param years: amount of years to delimit search
    :param sep: separator in csv file
    :return: name of track and artist
    """
    df = pd.read_csv(path, sep=sep)
    current_date = date.today()
    current_year = current_date.year
    year_span = df[df['release_year'].between(current_year - years, current_year)]
    year_span['popularity_track'].idxmax()
    max_pop = year_span.loc[year_span['popularity_track'].idxmax()]
    return max_pop['name_track'], max_pop['artist_name']


def decade_artists(path, decade, sep=';'):
    """
    Finds artists with tracks in specific decade.
    Defines decade as 10 years starting from
    any given year.
    :param path: path to dataset file
    :param decade: single year that starts decade
    :param sep: separator in csv file
    :return: set of artists names
    """
    df = pd.read_csv(path, sep=sep)
    year = df[df['release_year'].between(decade, decade + 9)]
    artists = set(year['artist_name'].to_list())
    return artists
