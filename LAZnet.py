from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.pooling import MaxPooling1D

def LAZnet(weights_path=None, task=1):
    
    if task == 1:
        num_classes = 2
    if task == 2:
        num_classes = 3
    if task == 3:
        num_classes = 8
    
    model = Sequential()
    model.add(Conv1D(64, 5, input_shape=(30,300)))
    model.add(Activation('relu'))
    model.add(MaxPooling1D(5))
    model.add(Dropout(0.5))
    
    model.add(Conv1D(128,5))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, kernel_initializer='uniform'))
    model.add(Activation('softmax'))
    
    if weights_path:
        model.load_weights(weights_path)
        
    return model