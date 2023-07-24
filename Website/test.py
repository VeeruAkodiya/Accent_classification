import librosa
import numpy as np
import tensorflow as tf
from tensorflow import keras
import random

def padding(array, xx, yy):
    """
    :param array: numpy array
    :param xx: desired height
    :param yy: desirex width
    :return: padded array
    """

    h = array.shape[0]
    w = array.shape[1]

    a = (xx - h) // 2
    aa = xx - a - h

    b = (yy - w) // 2
    bb = yy - b - w

    return np.pad(array, pad_width=((a, aa), (b, bb)), mode='constant')

model = keras.models.load_model("LSTM_Final.hdf5")
print(model)
# file = "/mnt/c/Users/rutvik/Documents/Sound Recordings/aus 2.wav"
def get_predictions(file=None):
    if file is None:
        return
    FRAME_LENGTH = 1024
    HOP_LENGTH = 512
    sr = 8000
    random.seed(0)

    signal, _ = librosa.load(file, sr=sr)
    signal = np.trim_zeros(signal)
    data_tmp = librosa.feature.mfcc(y=signal)
    data_in = np.array([np.mean(values) for values in data_tmp])
    data_in.resize(1,1,40)
    return model.predict(data_in)