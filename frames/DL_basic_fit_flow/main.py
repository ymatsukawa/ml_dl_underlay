from pathlib import Path
from loader import Loader
from preprocess import Preprocess
from model import Model

data = Loader.load_csv(Path("./DL_basic_fit_flow/data/concrete.csv"))

prep = Preprocess(data)
train_x, test_x, train_y, test_y, val_x, val_y = prep.split(target_col="CompressiveStrength")
shape_index = data.columns.get_loc('CompressiveStrength')

model = Model(train_x=train_x, train_y=train_y, val_x=val_x, val_y=val_y, shape_index=shape_index)
model.fit()