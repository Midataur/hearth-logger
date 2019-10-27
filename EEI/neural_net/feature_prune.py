from numpy import genfromtxt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import VarianceThreshold

print('Generating array from text...')
training = genfromtxt('training.csv',delimiter=',',dtype=int)
testing = genfromtxt('testing.csv',delimiter=',',dtype=int)

names = list(range(len(training[0])))
print('Pruning...')

sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel = sel.fit(training)
print('Fitting...')
training = sel.transform(training)
testing = sel.transform(testing)
print('Saving...')
training = [list(x) for x in training]
testing = [list(x) for x in testing]
open("pruned(tr).csv","w").write('')
open("pruned(te).csv","w").write('')
for x in training:
    open("pruned(tr).csv","a").write(str(x)[1:-1]+'\n')
for x in testing:
    open("pruned(te).csv","a").write(str(x)[1:-1]+'\n')

print('Done!')