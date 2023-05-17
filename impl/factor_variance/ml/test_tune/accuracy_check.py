from sklearn.metrics import accuracy_score

def get_accurate_score(model=None, x_test=None, y_test=None, predicted=None):
  if model is None: raise ValueError('specify model')

  predict_Y = model.predict(x_test)
  return accuracy_score(y_test, predicted)
