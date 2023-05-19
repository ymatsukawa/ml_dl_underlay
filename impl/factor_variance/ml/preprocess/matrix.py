import pandas as pd
import numpy as np

class Matrix:
  """
  parameter of 'data' should be pandas dataframe

  column = ["X0", "X2", "Y"]
  d = [
    [1, 1, 2],
    [1, 3, 5],
    [4, 3, 8],
    [4, 3, 2],
    [5, 7, 11],
  ]

  Matrix.count_on_y(data, xcolumn='X0', ycolumn='Y')
  #=> [
    [1, 7],
    [4, 6],
    [5, 11]
  ]

  Matrix.count_on_y(data, xcolumn='X2', ycolumn='Y')
  #=> [
    [1, 2],
    [3, 15],
    [7, 11]
  ]
  """
  @classmethod
  def data_for_cancel(cls, data):
    # TODO: decide sale_type number on final
    d = data.drop(data[data['sale_type'] == 2].index)
    d = pd.concat([d['department'], d['cancel']], axis=1)

    return d.groupby('department')['cancel'].sum().reset_index()
