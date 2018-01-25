from common import *
from data_loader import DataLoader
import matplotlib.pyplot as plt
import numpy as np
import operator
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_curve, auc
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
import sys

class METHOD:
    gaussian, multinomial, bernoulli, tree = range(4)

method = METHOD.multinomial

iterations = 40
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


dl = DataLoader(data_file )

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if 'gauss' in sys.argv[1]:
            method = METHOD.gaussian
            print("Using GAUSSIAN Bayesian model")
        elif 'bern' in sys.argv[1]:
            method = METHOD.bernoulli
            print("Using BERNOULLI-distributed Bayesian model")
        else:
            print("Using MULTINOMIAL Bayesian model")

    for i in range(iterations):
        X_train, y_train = dl.train_set
        X_test, y_test = dl.test_set

        if method == METHOD.gaussian:
        # Is not rly worth, since word features are not continuous
        # <= not Gaussian distribution mix, they are percentages. This might be better
        # for statistical features, like counts of digits/capital letters/etc.
            clf = GaussianNB()

        elif method == METHOD.multinomial:
            clf = MultinomialNB()		# best option for our features
        elif method == METHOD.tree:
            clf = DecisionTreeClassifier(criterion="entropy")

        elif method == METHOD.bernoulli:
            clf = BernoulliNB(binarize=0.31)    # binarize found via cross validation

        clf.fit(X_train, y_train)
        scores.append(clf.score(X_test, y_test))

        fpr, tpr, _ = roc_curve(y_test, clf.predict_proba(X_test)[:, 1])
        roc_auc.append(auc(fpr, tpr))

    display_auc(y_test, clf.predict_proba(X_test)[:, 1])

    print('Accuracy:  Mean: %0.5f, Std: %0.5f' % (np.mean(scores), np.std(scores)))
    print('AUC:       Mean: %0.5f, Std: %0.5f' % (np.mean(roc_auc), np.std(roc_auc)))
    if method == METHOD.gaussian:
        weights = clf.theta_
    else:
        weights = np.exp(clf.feature_log_prob_)

    print('Top %d features:' % k)
    print(top_k_features(k, weights[0, :]))
    print(top_k_features(k, weights[1, :]))