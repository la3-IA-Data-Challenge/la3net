from imagededup.methods import CNN, PHash, AHash, DHash, WHash
from sklearn.metrics.pairwise import cosine_similarity
import cv2


class Encoder():
    """ TODO
    """
    def __init__(self, encoding: str = "mobilenet"):
        self.encoding = encoding
        if self.encoding == "mobilenet":
            self.encoder = CNN()
            self.metric = cosine_similarity
            self.out_features = 1024
        elif self.encoding == "orb":
            self.encoder = Orb()
            self.metric = self.encoder.score
            self.out_features = 0
        elif self.encoding == "phash":
            self.encoder = PHash()
            self.metric = self.encoder.hamming_distance
        elif self.encoding == "ahash":
            self.encoder = AHash()
            self.metric = self.encoder.hamming_distance
        elif self.encoding == "dhash":
            self.encoder = DHash()
            self.metric = self.encoder.hamming_distance
        elif self.encoding == "whash":
            self.encoder = WHash()
            self.metric = self.encoder.hamming_distance
    
    def __call__(self, path):
        return self.encoder.encode_image(image_file=path)




class Orb():
    """ TODO
    """
    def __init__(self):
        self.sift = cv2.ORB_create(nfeatures=500)

    def encode_image(self, image_file: str):
        img = cv2.imread(image_file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (512, 512))
        _, descriptor = self.sift.detectAndCompute(gray, None)
        return descriptor
    
    def score(self, descriptor_1, descriptor_2):
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descriptor_1, descriptor_2, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.85*n.distance:
                good.append([m])
        return len(good)
