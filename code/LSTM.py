import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import h5py

data_directory = os.path.join('..', 'data')

def load_data():
    for file in os.listdir(data_directory):
        with open(os.path.join(data_directory, file), 'r') as f:
            return f.read(), file


def output_result(result):
    with open(os.path.join('..', 'out', f_name), 'w') as f:
        f.write(result)


# setup data
training_data, f_name = load_data()
training_data.lower()
chars = np.unique(list(training_data))
data_size, alphabet_size = len(training_data), len(chars)
print('%d characters, %d unique' % (data_size, alphabet_size))
char_to_ix = {ch: i for i, ch in enumerate(chars)}
ix_to_char = {i: ch for i, ch in enumerate(chars)}
seq_length = 100
raw_X = []
raw_y = []
for i in range(0, data_size - seq_length, 1):
    seq_X = training_data[i:i+seq_length]
    seq_y = training_data[i+seq_length]
    raw_X.append([char_to_ix[c] for c in seq_X])
    raw_y.append(char_to_ix[seq_y])

# standardize
n_patterns = len(raw_X)
X = np.reshape(raw_X, (n_patterns, seq_length, 1))
X = np_utils.to_categorical(X)
y = np_utils.to_categorical(raw_y)

# setup model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.25))
model.add(LSTM(256))
model.add(Dropout(0.25))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# find best weights all epocs
filename = "weights.best.hdf5"
# checkpoint = ModelCheckpoint(filename, monitor='loss', verbose=1, save_best_only=True, mode='min')
# callbacks_list = [checkpoint]

# fit the model
# model.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)

# load best
with h5py.File(filename, 'r') as f:
    model.load_weights(filename)

# pick a random seed
start = np.random.randint(0, len(X) - 1)
pattern = X[start]

# generate characters
result = ''
for i in range(1000):
    x = np.reshape(pattern, (1, len(pattern), len(pattern[1])))
    prediction = model.predict_proba(x, verbose=0)[0,:]
    rnd_idx = np.random.choice(len(prediction), p=prediction)
    result += ix_to_char[rnd_idx]
    seq_in = [ix_to_char[value] for value in np.argmax(pattern, axis=1)]
    add = np.zeros((1,len(pattern[1])))
    add[0][rnd_idx] = 1
    pattern = np.append(pattern, add, axis=0)
    pattern = pattern[1:len(pattern)]
output_result(result)