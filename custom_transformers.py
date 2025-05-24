# custom_transformers.py
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import joblib

preprocess_enc_scal = joblib.load('Model\Encoder\preprocess_enc_scal.joblib')


class ColumnSelectorTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.columns]

class ToDataFrameTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, prefix='pca'):
        self.prefix = prefix

    def fit(self, X, y=None):
        self.n_features_ = X.shape[1]
        return self

    def transform(self, X):
        columns = [f"{self.prefix}_{i+1}" for i in range(X.shape[1])]
        return pd.DataFrame(X, columns=columns, index=range(X.shape[0]))

def get_feature_names(column_transformer):
    output_features = []

    for name, transformer, columns in column_transformer.transformers_:
        if name == 'remainder':
            continue
        if hasattr(transformer, 'get_feature_names_out'):
            names = transformer.get_feature_names_out(columns)
        else:
            names = columns
        output_features.extend(names)
    return output_features

def convert_to_df(X):
    return pd.DataFrame(
        X.toarray() if hasattr(X, 'toarry') else
        X, columns= get_feature_names(preprocess_enc_scal))