from sklearn.linear_model import LogisticRegression

class Model:
  def __init__(self, x_test=None, y_test=None):
    self._model = LogisticRegression()

  def fit(self, x_test=None, y_test=None):
    if x_test is None or y_test is None:
      raise ValueError('x_test and y_test must be specified')
    self._model.fit(x_test, y_test)
    self._score()

  def predict(self, x=None):
    if x is None:
      raise ValueError('x must be specified')
    score = self._model.predict(x)
    print(score)

  def _score(self):
    pass
