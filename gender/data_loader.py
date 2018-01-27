from common import *
import csv
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

from numpy.random import RandomState
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler

class DataLoader():
    def __init__(self):
        # file names moved to common
        self.full_set = self.featurize(self.read_data())
        self.scale_data()
        x1, x2, y1, y2 = train_test_split(self.full_set, self.y_train, 
            test_size=0.3, random_state=RandomState())
        self.train_set = x1, y1
        self.test_set = x2, y2
        self.validate_set = None

    def scale_data(self):
        mcc_scaler = MinMaxScaler()
        type_scaler = MinMaxScaler()
        mcc_scaler.fit(self.X_train[:, :len(self.user_tr_mcc_list)])
        type_scaler.fit(self.X_train[:, len(self.user_tr_mcc_list):self.feat_sz])
        mcc_scaler.transform(self.X_train[:, :len(self.user_tr_mcc_list)])
        type_scaler.transform(self.X_train[:, len(self.user_tr_mcc_list):self.feat_sz])    

    def featurize(self, mat):
        self.feat_sz = len(self.user_tr_mcc_list) + len(self.user_tr_type_list) 
        self.X_train = np.zeros([len(self.user_train), self.feat_sz], dtype='int')
        self.X_test = np.zeros([len(self.user_test), self.feat_sz], dtype='int')
        self.y_train = [self.user_gender_dict[i] for i in self.user_train]        
        ud = {v: k for k, v in enumerate(self.user_train)}
        ut = {v: k for k, v in enumerate(self.user_test)}
        td = {v: k for k, v in enumerate(self.user_tr_type_list)}
        mccd = {v: k for k, v in enumerate(self.user_tr_mcc_list)}
        # counters
        for t in mat:
            try:
                self.X_train[ud[t[0]], mccd[t[2]]] += t[4] * -1
                self.X_train[ud[t[0]], len(self.user_tr_mcc_list) + td[t[3]]] += t[4] * -1
            except:
                pass
                #self.X_test[ut[t[0]], mccd[t[2]]] += 1
                #self.X_test[ut[t[0]], len(self.user_tr_mcc_list) + td[t[3]]] += 1       
        return self.X_train 

    def read_data(self):
        df = pd.read_csv(data_file)
        self.users = pd.read_csv(labels_file)
        self.codes = pd.read_csv(features1_file, encoding='cp1251')
        self.types = pd.read_csv(features2_file, delimiter=';')
        user_genders = self.users.as_matrix()
        self.data_labels = list(self.codes.as_matrix()[:, 1]) + list(self.types.as_matrix()[:, 1])
        #users = users.set_index('customer_id')

        mat = df.as_matrix()
        self.user_gender_dict = {i[0]: i[1] for i in user_genders[:, 1:]}
        ulabels = [2 if not i in self.user_gender_dict.keys() else self.user_gender_dict[i] for i in mat[:, 0]]
        validate_mask = [1 if i > 1 else 0 for i in ulabels]
        self.user_tr_mcc_list = sorted(set(mat[:, 2]))
        self.user_tr_type_list = sorted(set(mat[:, 3]))
        self.user_list = sorted(set(mat[:, 0]))
        self.user_train = [i for i in self.user_list if i in self.user_gender_dict.keys()]

        # Verifying we have all features named
        missed = [str(i) for i in self.user_tr_mcc_list if i not in 
            np.intersect1d(self.codes.as_matrix()[:, 0], self.user_tr_mcc_list)]
        if(len(missed) > 0):
            print ("Missed transaction codes, cannot find them in dictionary: " 
                + ", ".join(missed))

        missed = [str(i) for i in self.user_tr_type_list if i not in 
            np.intersect1d(self.types.as_matrix()[:, 0], self.user_tr_type_list)]
        if (len(missed) > 0):
            print ("Missed transaction types, cannot find them in dictionary: " 
                + ", ".join(missed))

        self.user_test = [str(i) for i in self.user_list if i not in 
            np.intersect1d(user_genders[:, 0], self.user_list)]
        return mat

    def train(self):
        return self.train_set

    def test(self):
        return self.test_set

    def validate(self):
        return self.validate_set


if __name__ == '__main__':
    # testing loading
    dl = DataLoader()