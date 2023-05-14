from sklearn.model_selection import train_test_split

class Preprocess:
  def __init__(self, data):
    self.data = data
  
  def split(self, target_col=None):
    if target_col is None:
      raise ValueError('target_col should be set. ex.) target_col="name", target_col="age", etc.')

    # https://datascience.stackexchange.com/a/15136
    x = self.data.drop(target_col, axis=1)
    y = self.data[target_col]
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=32)
    _, val_x, _, val_y = train_test_split(train_x, train_y, test_size=0.25, random_state=32)
    
    return train_x, test_x, train_y, test_y, val_x, val_y