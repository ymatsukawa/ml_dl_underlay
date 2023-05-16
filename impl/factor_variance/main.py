from ml.preprocess.load_data import Loader
from ml.core.model import Model




exit

# preprocess
loader = Loader("impl/factor_variance/data.csv")
x_train, x_test, y_train, y_test = loader.load()

# fit and predict by model
model = Model()
model.fit(x_train, y_train)

model.predict(x_test)
