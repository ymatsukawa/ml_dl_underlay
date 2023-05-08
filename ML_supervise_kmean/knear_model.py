import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

class KNearModel:
  def __init__(self, x_train=None, y_train=None, x_test=None, y_test=None, neighbors=3):
    self.model = KNeighborsClassifier(n_neighbors=neighbors)
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
    neighbors = range(1, 10)
    for n in neighbors:
      k_model = KNeighborsClassifier(n_neighbors=n)
      k_model.fit(self.x_test, self.y_test.values.ravel())

      train_accuracy.append(k_model.score(self.x_train, self.y_train))
      test_accuracy.append(k_model.score(self.x_test, self.y_test))

    plt.plot(neighbors, train_accuracy, label='train accuracy')
    plt.plot(neighbors, test_accuracy, label='test accuracy')

    plt.ylabel('ACCuracy')
    plt.xlabel('neighbors')
    plt.legend()

    plt.show()
