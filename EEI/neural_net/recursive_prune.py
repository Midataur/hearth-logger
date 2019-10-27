from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from numpy import genfromtxt
# load data

training = genfromtxt('training.csv',delimiter=',',dtype=int)
tr_answers = genfromtxt('tr_answers.csv',delimiter=',',dtype=int)
names = list(range(len(training[0])))

# feature extraction
model = LogisticRegression(solver='lbfgs')
rfe = RFE(model, 3)
fit = rfe.fit(training, tr_answers)
print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)