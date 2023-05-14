from tensorflow import keras
from tensorflow.keras import layers, callbacks

class Model:
  def __init__(self, train_x, train_y, val_x, val_y, shape_index):
    self.train_x = train_x
    self.train_y = train_y
    self.val_x = val_x
    self.val_y = val_y

    self.m = keras.Sequential([
      # hidden
      layers.Dense(units=512, activation='relu', input_shape=[shape_index]),
      layers.Dense(units=512, activation='relu'),
      layers.Dense(units=512, activation='relu'),
      # output
      layers.Dense(units=1)
    ])
    self.trained_m = None


  def fit(self):
    self.m.compile(
      optimizer="adam",
      loss="mae"
    )
    early_stopping = callbacks.EarlyStopping(
      min_delta=0.001,
      patience=20,
      restore_best_weights=True,
    )

    self.trained_m = self.m.fit(
      self.train_x, self.train_y,
      validation_data=(self.val_x, self.val_y),
      batch_size=256,
      epochs=10,
      callbacks=[early_stopping]
    )