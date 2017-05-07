
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)


# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:538,0:8]
Y = dataset[:538,8]
tx=dataset[538:,0:8]
ty=dataset[538:,8]
# create model
model = Sequential()
model.add(Dense(15, input_dim=8, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X, Y, epochs=150, batch_size=10)


scores = model.evaluate(tx, ty)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
