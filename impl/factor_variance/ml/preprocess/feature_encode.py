import pandas as pd

from ml.analyze.plots import Plot

class FeatureEncode:
  _DEPARTMENT_LABEL = {
    None       : -1,
    'software' : 1,
    'hardware' : 2,
    'design'   : 3
  }

  _SALE_TYPE_LABEL = {
    None     : 1,
    'agA'    : 2,
    'agB'    : 2,
    'agC'    : 2
  }

  @classmethod
  def get_featured(cls, data):
    new_sale_type = cls._label_sale_type(data)
    new_department = cls._label_department(data)

    data.loc[:, 'sale_type'] = new_sale_type
    data.loc[:, 'department'] = new_department
    # --- for debug
    # print(data)
    # Plot.simple(new_sale_type, new_department, xlegend='sale', ylegend='department', xlabel='sale', ylabel='department')
    return data

  @classmethod
  def _label_department(cls, data):
    return data.department.apply(cls._convert_department)

  @classmethod
  def _label_sale_type(cls, data):
    return data.sale_type.apply(cls._convert_sale_type)

  @classmethod
  def _convert_department(cls, value):
    key = None if pd.isna(value) else value
    return cls._DEPARTMENT_LABEL[key]

  @classmethod
  def _convert_sale_type(cls, value):
    key = None if pd.isna(value) else value
    return cls._SALE_TYPE_LABEL[key]
