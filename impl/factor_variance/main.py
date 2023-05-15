from preprocess import Preprocess


# preprocess
prep = Preprocess("impl/factor_variance/data.csv")
x_train, x_test, y_train, y_test = prep.prepare()

# classify by 'k-learn'

# plots