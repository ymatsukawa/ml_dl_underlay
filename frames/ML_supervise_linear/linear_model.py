import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class LinearModel:
  def __init__(self, x_train=None, y_train=None, x_test=None, y_test=None):
    self.model = LinearRegression()
    self.x_train = x_train
    self.y_train = y_train
    self.x_test = x_test
    self.y_test = y_test

  def fit(self, plot_evaluate=False):
    any_none = any(e for e in [self.x_train, self.y_train, self.x_test, self.y_test] if e is None)
    if any_none:
      raise ValueError('set all train and test parameters')

    self.model.fit(self.x_train, self.y_train.values.ravel())

    if plot_evaluate == True:
      self._evaluate_by_plot()

  def predict(self, x, y):
    self.model.predict(x, y)

  def _evaluate_by_plot(self):
    train_accuracy = []
    test_accuracy = []

    k_model = LinearRegression()
    k_model.fit(self.x_test, self.y_test.values.ravel())

    train_score = k_model.score(self.x_train, self.y_train)
    test_score = k_model.score(self.x_test, self.y_test)
    print("train ACCuracy: [{}]".format(train_score))
    print("test ACCuracy: [{}]".format(test_score))