from common import *
import csv
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

from numpy.random import RandomState
from sklearn.cross_validation import train_test_split

class DataLoader():
    def __init__(self, filename):
        df = pd.read_csv(data_file)
        users = pd.read_csv(labels_file)
        codes = pd.read_csv(features1_file, encoding='cp1251')
        types = pd.read_csv(features2_file, delimiter=';')
        user_genders = users.as_matrix()
        #users = users.set_index('customer_id')
        # users.ix[33486286].gender

        mat = df.as_matrix()    # (6849346, 6) # UID, DT, MCC, type, amount
        user_gender_dict = {i[0]: i[1] for i in user_genders[:, 1:]}
        ulabels = [2 if not i in user_gender_dict.keys() else user_gender_dict[i] for i in mat[:, 0]]
        validate_mask = [1 if i > 1 else 0 for i in ulabels]

        user_tr_mcc_list = sorted(set(mat[:, 2]))
        user_tr_type_list = sorted(set(mat[:, 3]))
        user_list = sorted(set(mat[:, 0]))

        # Verifying we have all features named
        missed = [str(i) for i in user_tr_mcc_list if i not in np.intersect1d(codes.as_matrix()[:, 0], user_tr_mcc_list)]
        if(len(missed) > 0):
            print ("Missed transaction codes, cannot find them in dictionary: " + ", ".join(missed))

        missed = [str(i) for i in user_tr_type_list if i not in np.intersect1d(types.as_matrix()[:, 0], user_tr_type_list)]
        if (len(missed) > 0):
            print ("Missed transaction types, cannot find them in dictionary: " + ", ".join(missed))

        test_users = [str(i) for i in user_list if i not in np.intersect1d(user_genders[:, 0], user_list)]
        print ("Users for testing: " + ", ".join(missed))

        self.full_set = None
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


if __name__ == '__main__':
    # testing loading
    dl = DataLoader()