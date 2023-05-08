from preprocess import Preprocess
from knear_model import KNearModel

# load and prepare
prep = Preprocess()
x_train, x_test, y_train, y_test = prep.prepare()

# fit and evaluate
model = KNearModel(neighbors=3, x_train=x_train, y_train=y_train, y_test=y_test, x_test=x_test)
model.fit(plot_evaluate=True)

# predict!
# model.predict(x_data, y_data)
