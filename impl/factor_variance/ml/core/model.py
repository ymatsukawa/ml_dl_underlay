from sklearn.linear_model import LogisticRegression
from ml.test_tune.accuracy_check import get_accurate_score

class Model:
  def __init__(self, x_train=None, y_train=None, x_test=None, y_test=None):
    self._model = LogisticRegression()
    self._x_train = x_train
    self._y_train = y_train
    self._x_test = x_test
    self._y_test = y_test

  def fit(self):
    self._model.fit(self._x_train, self._y_train)

  def predict(self, x=None):
    if x is None:
      raise ValueError('x must be specified as predicate date')
    predicted = self._model.predict(x)

    self._score(predicted=predicted)

  def _score(self, predicted):
    accuracy = get_accurate_score(model=self._model, x_test=self._x_test, y_test=self._y_test, predicted=predicted)
    print("accuracy score is {}".format(accuracy))
