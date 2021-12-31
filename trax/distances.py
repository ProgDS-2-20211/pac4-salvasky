from scipy.spatial import distance

def distances(list, metric):
    """
    Calculates distance between pairs
    of collections.
    :param list: input list of numbers
    :param metric: distance metric
    :return: array
    """
    dist = 1 - distance.cdist(list, list, metric)
    return dist
