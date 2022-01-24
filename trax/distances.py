from scipy.spatial import distance


def distances(feature_list, metric):
    """
    Calculates distance between pairs
    of collections
    :param feature_list: input list of numbers
    :param metric: distance metric
    :return: array
    """
    dist = 1 - distance.cdist(feature_list, feature_list, metric)
    return dist
