from ml.preprocess.feature_encode import FeatureEncode
from ml.preprocess.sanitizer import Sanitizer

import pandas as pd
from sklearn.model_selection import train_test_split

class Loader:
  def __init__(self, path_csv_file):
    self._path_csv_file = path_csv_file

  """
  returns:
    X_train, X_test, Y_train, Y_test
  """
  def load_for_ml(self):
    self._load_xy()
    return train_test_split(self.x, self.y, test_size=0.2, random_state=32)

  def load_data(self):
    self._load_xy()
    return pd.concat([self._x[:], self._y], axis=1)

  def _load_xy(self):
    data = pd.read_csv(self._path_csv_file)
    sanitized = Sanitizer.sanitize(data)
    d = FeatureEncode.get_featured(data=sanitized)

    self._x = d[['sale_type', 'department']]
    self._y = d['cancel']
