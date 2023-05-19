from ml.preprocess.load_data import Loader
from ml.core.model import Model
from ml.preprocess.matrix import Matrix

from ml.analyze.plots import Plot

# preprocess
loader = Loader("impl/factor_variance/testing.csv")
# x_train, x_test, y_train, y_test = loader.load()
data = loader.load_data()

cancle_counted = Matrix.data_for_cancel(data)

Plot.linear(
  x=cancle_counted['department'], y=cancle_counted['cancel'],
  xlabel='department', ylabel='cancel'
)

# fit and predict by model
"""
model = Model(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test)
model.fit()
model.predict(x_test)
"""
