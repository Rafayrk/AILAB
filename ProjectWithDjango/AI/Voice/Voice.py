from keras.models import Sequential
from keras.layers import Dense
import numpy

numpy.random.seed(7)

dataset = numpy.genfromtxt("voice.csv", delimiter=",",skip_header=1)


X = dataset[:2220,0:20]
Y = dataset[:2220,20]
tx = dataset[2220:,0:20]
ty = dataset[2220:,20]

model = Sequential()
model.add(Dense(12, input_dim=20, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X, Y, epochs=150, batch_size=10)


scores = model.evaluate(tx, ty)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))



prediction=model.predict(tx[0::2220])
print(prediction)