import pandas as pd

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
  def new_feature(cls, data):
    sale_type = cls._label_sale_type(data)
    department = cls._label_department(data)

    # TODO: PCA?
    print(sale_type)
    print(department)

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
