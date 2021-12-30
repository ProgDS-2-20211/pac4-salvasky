import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def basic_stats(path, feature, artist, sep=';'):
    """
    Returns max, min and mean values
    from specific feature on given artist
    :param path: path to dataset file
    :param feature: feature to extract
    :param artist: artist name
    :param sep: default separator of csv file
    :return: min, max and mean values
    """
    global min, max, sum
    df = pd.read_csv(path, sep=sep)
    art = df[df['artist_name'] == artist]
    col = art[feature].to_list()
    min = min(col)
    max = max(col)
    sum = sum(col)
    length = len(col)
    mean = sum / length

    return min, max, mean


def stat_by_album(path, feature, artist, sep=';'):
    """
    Creates a graph of mean values of feature
    from one artist grouped by album
    :param path: path to dataset file
    :param feature: feature to extract
    :param artist: artist name
    :param sep: default separator of csv file
    :return: dataframe and horizontal bar plot
    """
    df = pd.read_csv(path, sep=sep)
    art = df[df['artist_name'] == artist]
    dance = art.groupby('name_album', as_index=False)[feature].mean()
    dance.plot.barh(x='name_album', y=feature, title=artist+': Danceability by album')
    plt.show()
    print(dance)
    return dance


def density_hist(path, feature, artist, sep=';', bins=15, kde=True):
    """
    Draws a density histogram from given
    feature and given artist
    :param path: path to dataset file
    :param feature: feature to extract
    :param artist: artist name
    :param sep: default sepatator of csv file
    :param bins: default number of bins
    :param kde: default density line
    :return: density histogram plot
    """
    df = pd.read_csv(path, sep=sep)
    art = df[df['artist_name'] == artist]
    sns.displot(art, x=feature, stat='density', kde=kde, bins=bins).set(title=artist+'\'s tracks')
    plt.show()

