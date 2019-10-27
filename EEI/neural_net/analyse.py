from numpy import genfromtxt
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.callbacks import EarlyStopping
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import VarianceThreshold

#inputs: coin, turn, opclass, cards played, last three cards played

print('Generating features array...')
training = genfromtxt('training.csv',delimiter=',',dtype=int)
testing = genfromtxt('testing.csv',delimiter=',',dtype=int)
#sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
#dataset = sel.fit_transform(dataset)

print('Generating answers array...')
tr_answers = genfromtxt('tr_answers.csv',delimiter=',',dtype=int)
te_answers = genfromtxt('te_answers.csv',delimiter=',',dtype=int)

print('Building module...')
model = Sequential()
model.add(Dense(673,input_dim=len(training[0]),activation='relu'))
model.add(Dense(700, activation='relu'))
model.add(Dense(400, activation='relu'))
model.add(Dense(331, activation='softmax'))

print('Compiling...')
# compile the keras model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

es_callback = EarlyStopping(monitor='loss', patience=3)

print('Training...')
# fit the keras model on the dataset
model.fit(training, tr_answers, epochs=30, batch_size=10,callbacks=[es_callback])

# evaluate the keras model
_, accuracy = model.evaluate(testing, te_answers, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))
