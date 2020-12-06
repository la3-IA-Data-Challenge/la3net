# Imports
import os
from imagededup.methods import CNN
from sklearn_extra.cluster import KMedoids
from sklearn.metrics.pairwise import euclidean_distances
from .utils.extractors import Encoder
import numpy as np
import pickle


def generate_clusters(features, n_clusters=5):
    kmedoids = KMedoids(n_clusters=n_clusters, random_state=0).fit(features)
    return kmedoids.cluster_centers_, kmedoids.labels_


def get_closest_cluster(input_path, centroids):
    encoder = Encoder(encoding="mobilenet")
    features = encoder(input_path)
    dis = (np.inf, -1)
    for i in range(centroids.shape[0]) :
        a = euclidean_distances(features, centroids[i].reshape(1, -1))
        if dis[0] > a :
            dis = (a, i)
    return dis[1]


def eval_clustering(centroids, labels, data):
    total_acc = 0.0
    for clust in range(centroids.shape[0]):
        ids = np.random.choice(np.where(labels == clust)[0], 5)
        acc = 0.0
        for id_ in ids:
            targets = data.duplicates.iloc[id_]
            tmp_acc = 0
            for target in targets:
                if target in np.where(labels == clust)[0]:
                    tmp_acc += 1
            tmp_acc = tmp_acc/len(targets)
            acc += tmp_acc
            print(f"Cluster {clust} - image n°{id_} - Acc: {tmp_acc}")
        acc = acc/len(ids)
        print(f"Cluster {clust} - Acc: {acc}")
        total_acc += acc
    
    return total_acc/5