
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)


# load pima indians dataset
dataset = numpy.genfromtxt("cs-training.csv", delimiter=",",skip_header=1)
# split into input (X) and output (Y) variables
X = dataset[:10500,2:12]
Y = dataset[:10500,1]
tx=dataset[10500:,2:12]
ty=dataset[10500:,1]
# create model
model = Sequential()
model.add(Dense(10, input_dim=10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(40, activation='relu'))

model.add(Dense(1, activation='sigmoid'))



model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X, Y, epochs=10, batch_size=100)


scores = model.evaluate(tx, ty)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
