import argparse
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


def load_data(filename):
    with open(os.path.join('..', 'data', filename), 'r') as f:
        return f.read()


def output_result(result):
    with open(os.path.join('..', 'out', filename), 'w') as f:
        f.write(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-tr', '--training', required=True)

    io_args = parser.parse_args()
    training = io_args.training

    # setup data
    training_data = load_data(training).lower()
    chars = list(set(training_data))
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
    X = X / float(alphabet_size)
    y = np_utils.to_categorical(raw_y)

    # setup model
    model = Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(256))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # find best weights all epocs
    filename = "weights.best.hdf5"
    checkpoint = ModelCheckpoint(filename, monitor='loss', verbose=1, save_best_only=True, mode='min')

    callbacks_list = [checkpoint]

    # fit the model
    model.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)

    # load best
    model.load_weights(filename)

    # pick a random seed
    start = np.random.randint(0, len(raw_X) - 1)
    pattern = raw_X[start]

    # generate characters
    result = ''
    for i in range(1000):
        x = np.reshape(pattern, (1, len(pattern), 1))
        x = x / float(alphabet_size)
        prediction = model.predict(x, verbose=0)
        index = np.argmax(prediction)
        result += ix_to_char[index]
        seq_in = [ix_to_char[value] for value in pattern]
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    output_result(result)