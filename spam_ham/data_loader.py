from common import *
import csv
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

from numpy.random import RandomState
from sklearn.cross_validation import train_test_split

class DataLoader():
    def __init__(self, filename):
        self.corpus_path = filename    # In future, we can normalize paths
        self.full_set = None
        self.read_file()
        # or scan for directories
        x1, x2, y1, y2 = train_test_split(self.full_set, np.array(self.labels), test_size=0.3, random_state=RandomState())
        self.test_set = x1, y1
        self.train_set = x2, y2
        self.validate_set = None
        pass

    def train(self):
        return self.train_set

    def test(self):
        return self.test_set

    def validate(self):
        return self.validate_set

    def read_file(self):
        self.raw_data = []
        self.labels = []
        with open(self.corpus_path, 'r', encoding='cp1252') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) < 2:
                    continue
                # These are data-specific preprocessing solutions
                self.raw_data.append(", ".join(row[:-1]))
                self.labels.append(1 if row[-1:][0] == 'spam' else 0)
        vm = CountVectorizer()
        vm.fit(self.raw_data)
        data = vm.transform(self.raw_data).toarray()
        self.full_set = data
        self.dictionary = vm.get_feature_names()
        self.data = pd.DataFrame(vm.transform(self.raw_data).toarray(),
                         columns=self.dictionary)
        #print (self.data)
        return self.data

if __name__ == '__main__':
    # testing text loading
    dl = DataLoader(data_file)