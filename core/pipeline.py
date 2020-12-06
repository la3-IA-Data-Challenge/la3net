from .clustering import generate_clusters, get_closest_cluster
from .duplicate_search import search_duplicates_mn, search_duplicates_hash, search_duplicates_orb
import numpy as np


def method1(input_paths, filenames, feature_path):
    outputs = []
    for input_path in input_paths:
        imgs_features = pickle.load(open(feature_path, "rb"))
        centroids, labels = generate_clusters(imgs_features, n_clusters=5)
        clust = get_closest_cluster(input_path, centroids)
        indexes = np.where(labels == clust)[0]
        duplicates, _ = search_duplicates_mn(input_path, indexes, imgs_features)
        outputs += duplicates
    outputs = set(outputs)
    return [filenames[output] for output in outputs]


def method2(input_paths, filenames, feature_path):
    outputs = []
    for input_path in input_paths:
        imgs_features = pickle.load(open(feature_path, "rb"))
        centroids, labels = generate_clusters(imgs_features, n_clusters=5)
        clust = get_closest_cluster(input_path, centroids)
        indexes = np.where(labels == clust)[0]
        duplicates, _ = search_duplicates_hash(input_path, indexes, filenames, mode="phash")
        outputs += duplicates
    outputs = set(outputs)
    return [filenames[output] for output in outputs]


def method3(input_paths, filenames, feature_path):
    outputs = []
    for input_path in input_paths:
        imgs_features = pickle.load(open(feature_path, "rb"))
        centroids, labels = generate_clusters(imgs_features, n_clusters=5)
        clust = get_closest_cluster(input_path, centroids)
        indexes = np.where(labels == clust)[0]
        duplicates, _ = search_duplicates_orb(input_path, indexes, filenames)
        outputs += duplicates
    outputs = set(outputs)
    return [filenames[output] for output in outputs]