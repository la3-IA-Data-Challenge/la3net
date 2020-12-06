# Imports
import os

from .utils.extractors import Encoder
from .utils.evaluator import Evaluator

from sklearn_extra.cluster import KMedoids
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd

import pickle

def search_duplicates_mn(input_path, indexes, imgs_features):
    encoder = Encoder(encoding="mobilenet")
    target_features = encoder(input_path)
    duplicates = []
    closest = [-1, -1]
    for i in indexes:
        similarity = cosine_similarity(target_features, imgs_features[i].reshape(1, -1))
        if similarity > 0.85:
            duplicates.append(i)
        elif closest[0] < similarity:
            closest[0] = similarity
            closest[1] = i

    return duplicates, closest[1]


def search_duplicates_hash(input_path, indexes, filenames, mode="phash"):
    encoder = Encoder(encoding=mode)
    encoded_target = encoder(input_path)
    duplicates = []
    closest = [np.inf, -1]
    for i in indexes:
        distance = encoder.metric(encoded_target, encoder(filenames[i]))
        if distance <= 12:
            duplicates.append(i)
        elif closest[0] > distance:
            closest[0] = distance
            closest[1] = i
    
    return duplicates, closest[1]


def search_duplicates_orb(input_path, indexes, filenames):
    encoder = Encoder(encoding="orb")
    encoded_target = encoder(input_path)
    duplicates = []
    closest = [0, -1]
    for i in indexes:
        score = encoder.metric(encoded_target, encoder(filenames[i]))
        if score >= 50:
            duplicates.append(i)
        elif closest[0] < score:
            closest[0] = score
            closest[1] = i
    
    return duplicates, closest[1]


def performance(filenames, encoding, ids, indexes, evaluator, imgs_features=None):
    total_precision = 0.0
    total_recall = 0.0
    # perf = {
    #     "model":[encoding]*(len(ids)),
    #     "cluster":[i for i in range(ids)],
    #     "precision": [-1 for i in range(ids)],
    #     "recall": []
    # }
    for i in range(len(ids)):
        index = indexes[i]
        id_ = ids[i]
        input_path = filenames[id_]
        if encoding == "mobilenet":
            duplicates, closest = search_duplicates_mn(input_path, index, imgs_features)
        elif encoding in ["phash", "ahash", "dhash", "whash"]:
            duplicates, closest = search_duplicates_hash(input_path, index, filenames, mode=encoding)
        elif encoding == "orb":
            duplicates, closest = search_duplicates_orb(input_path, index, filenames)
        precision, recall, _ = evaluator.eval(id_, duplicates, index)
        print(f"Cluster {i} - image n°{id_} - {duplicates} as duplicates - Precision: {precision} - Recall: {recall}")
        total_precision += precision
        total_recall += recall
    total_precision = total_precision/5
    total_recall = total_recall/5
    f1_score = 2*((total_precision*total_recall)/(total_precision+total_recall))
    return total_precision, total_recall, f1_score