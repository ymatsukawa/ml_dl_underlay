from feature_encode import FeatureEncode
from sanitizer import Sanitizer

import pandas as pd
from sklearn.model_selection import train_test_split

class Preprocess:
  def __init__(self, path_csv_file):
    self._path_csv_file = path_csv_file

  """
  returns:
    X_train, X_test, Y_train, Y_test
  """
  def prepare(self):
    self._load_xy()
    # return train_test_split(self.x, self.y, test_size=0.2, random_state=32)

  def _load_xy(self):
    data = pd.read_csv(self._path_csv_file)
    d = Sanitizer.sanitize(data)

    self.x = FeatureEncode.new_feature(data=d)
    self.y = d['cancel']
