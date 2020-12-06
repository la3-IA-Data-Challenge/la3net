import os
from .utils.extractors import Encoder
import numpy as np
import pickle

def extract_features(encoder, dirname):
    nb_images = len(os.listdir(dirname))
    nb_features = encoder.out_features
    features = np.zeros((nb_images, nb_features))
    i = 0
    for filename in os.listdir(dirname):
        path = os.path.join(dirname, filename)
        encoding = encoder(path)
        features[i] = encoding.flatten()
        i+= 1
    return features


