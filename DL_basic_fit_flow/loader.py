import pandas as pd

class Loader:
  @classmethod
  def load_csv(cls, filepath):
    return pd.read_csv(filepath)
  