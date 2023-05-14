import tensorflow as tf
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras.layers import Dense

df = pd.read_csv('DL_tf_linear_basic/data.csv')

x = np.array(df.X)
y = np.array(df.Y)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)

model = keras.Sequential([
  Dense(units=1, input_shape=(1,), activation=None)
])
model.compile(
  loss='mse',
  optimizer='adam'
)
model.fit(train_x, train_y, epochs=100, batch_size=32, validation_split=0.2)

eval_results = model.evaluate(test_x, test_y, batch_size=32)
print(eval_results)
predict = model.predict(test_x)