import pandas as pd

class Evaluator():
    def __init__(self, file_path):
        self.path = file_path
        data = pd.read_csv(file_path)
        self.data = pd.DataFrame({
            "duplicates": data.duplicates.apply(lambda x: [int(elt) for elt in x.split(" ")])
        })
    
    def eval(self, image_id, inputs, clusters):
        targets = self.data.duplicates.iloc[image_id]
        inputs = inputs
        count = 0
        for i in range(len(targets)):
            if targets[i] in inputs or targets[i] not in clusters:
                count += 1
        
        precision = count/len(inputs)
        recall = count/len(targets)
        f1_score = 2*((precision*recall)/(precision+recall))
        return precision, recall, f1_score
