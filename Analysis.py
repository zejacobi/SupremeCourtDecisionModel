__author__ = 'zach'

from pandas import DataFrame as Df
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from numpy import array


def error(pred, real):
    wrong = 0.0
    for index, guess in enumerate(pred):
        if labels[index] != guess:
            wrong += 1.0
    err = wrong/len(real)
    print err

supreme_court_decisions = Df.from_csv('./Supreme Court.txt', sep='\t')

data = supreme_court_decisions.drop('Provincial Government', axis=1, inplace=False)
data.drop('Assenting Justices', axis=1, inplace=True)
data.drop('Dissenting Justices', axis=1, inplace=True)
data.drop('Tag1', axis=1, inplace=True)
data.drop('Tag2', axis=1, inplace=True)

features = data.drop('Constitutional Challenge Succeeded', axis=1, inplace=False)
labels = data['Constitutional Challenge Succeeded']

rf = RandomForestClassifier(n_estimators=10,
                            criterion='gini', max_features='auto',
                            max_depth=None, min_samples_split=2,
                            min_samples_leaf=1)
rf.fit(features, labels)

supp = svm.SVC(kernel='rbf', C=1.0, degree=3, gamma=0.0, coef0=0.0)
supp.fit(features, labels)

# predicted_rf = list(rf.predict(features))
# error(predicted_rf, labels)
#
# predicted_svm = list(supp.predict(features))
# error(predicted_svm, labels)

# 34% Error seems to be about what we're getting

# Case array for Constitutional
con = array([1, 1, 0, 0])

# Case array for International
inter = array([1, 0, 0, 1])

print 'Constitutional Challenge Success'
print supp.predict(con)  # Predicts failure
print rf.predict(con)  # Predicts success

print supp.predict(inter)  # Predicts failure
print rf.predict(inter)  # Predicts failure