import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

class Preprocess:
  def __init__(self):
    self._load()

  """
  returns:
    X_train, X_test, Y_train, Y_test
  """
  def prepare(self):
    return train_test_split(self.x, self.y, test_size=0.2, random_state=32)

  def _load(self):
    iris = datasets.load_iris()
    self.x = pd.DataFrame(iris.data)
    self.y = pd.DataFrame(iris.target)