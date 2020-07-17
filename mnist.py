# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:48:25 2019

@author: 13716
"""

from keras.datasets import mnist
from keras.utils import np_utils
from keras import Sequential
from keras.layers import Dense, Activation, Dropout


(x_train, y_train), (x_test, y_test) = mnist.load_data()

# =============================================================================
# x_train = x_train.reshape(60000, 784).astype('float32')
# x_test = x_test.reshape(10000, 784).astype('float32')
# x_train /= 255
# x_test /= 255 
# =============================================================================

batch_size = 512
nb_class = 10
nb_epochs = 4

# =============================================================================
# # 把数据0~9个值，转化为一个10位数组的判定
# y_test = np_utils.to_categorical(y_test, nb_class)
# y_train = np_utils.to_categorical(y_train, nb_class)
# 
# =============================================================================
model = Sequential()


# 第一层
# 输入 284
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))
# 处理过拟合
model.add(Dropout(0.2))
# 第二层
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.2))
#第三层
model.add(Dense(10))
# softmax 进行十个分类
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy", optimizer="rmsprop", metrics=['accuracy'])

trainning = model.fit(x_train, y_train, batch_size=batch_size, epochs=nb_epochs)
