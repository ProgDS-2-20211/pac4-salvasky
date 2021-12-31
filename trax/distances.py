from scipy.spatial import distance

def distances(list, metric):
    dist = 1 - distance.cdist(list, list, metric)
    return dist



