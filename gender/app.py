from data_loader import DataLoader
from sklearn.grid_search import GridSearchCV
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import numpy as np
import operator

from common import *

dl = DataLoader()

from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_curve, auc
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
import sys
from numpy.random import RandomState
import matplotlib.pyplot as plt

class METHOD:
    gaussian, multinomial, bernoulli, tree = range(4)

method = METHOD.bernoulli

iterations = 60
k = 8

scores = []
roc_auc = []
weights = []

def display_auc(y_true, y_score):
    fpr, tpr, _ = roc_curve(y_true, y_score)
    auc_func = auc(fpr, tpr)
    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc_func)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.01])
    plt.ylim([0.0, 1.06])
    plt.xlabel('FP Rate')
    plt.ylabel('TP Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc='lower right')
    plt.show()

def top_k_features(k, weights):
    return sorted(zip(dl.dictionary, weights), reverse=True, key=operator.itemgetter(1))[:k]


X_Train, Y_Train = dl.train_set
X_Test, Y_Test = dl.test_set

for i in range(iterations):

    if method == METHOD.gaussian:
        clf = GaussianNB()

    elif method == METHOD.multinomial:
        clf = MultinomialNB()		# best option for our features
    elif method == METHOD.tree:
        clf = DecisionTreeClassifier(criterion="entropy")

    elif method == METHOD.bernoulli:
        clf = BernoulliNB(binarize=0.31)    # binarize found via cross validation

    clf.fit(X_Train, Y_Train)
    scores.append(clf.score(X_Test, Y_Test))

    fpr, tpr, _ = roc_curve(Y_Test, clf.predict_proba(X_Test)[:, 1])
    roc_auc.append(auc(fpr, tpr))

display_auc(Y_Test, clf.predict_proba(X_Test)[:, 1])

print('Accuracy:  Mean: %0.5f, Std: %0.5f' % (np.mean(scores), np.std(scores)))
print('AUC:       Mean: %0.5f, Std: %0.5f' % (np.mean(roc_auc), np.std(roc_auc)))
if method == METHOD.gaussian:
    weights = clf.theta_
else:
    weights = np.exp(clf.feature_log_prob_)