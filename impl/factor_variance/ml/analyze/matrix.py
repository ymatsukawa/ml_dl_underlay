import pandas as pd
import numpy as np

class Categorize:
  @classmethod
  def cat(cls, x, y):
    d = pd.concat([x[:], y], axis=1)

    # ag_sale = d.drop(d[d['sale_type'] == 1].index)
    direct_sale = d.drop(d[d['sale_type'] == 2].index)

    return direct_sale.groupby('department')['cancel'].sum().reset_index()

  @classmethod
  def get_y(cls, data):
    pass
