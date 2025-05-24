import pandas as pd
import joblib
import custom_transformers
import sys
sys.modules['__main__'].convert_to_df = custom_transformers.convert_to_df
sys.modules['__main__'].ColumnSelectorTransformer = custom_transformers.ColumnSelectorTransformer
sys.modules['__main__'].ToDataFrameTransformer = custom_transformers.ToDataFrameTransformer

prepro= joblib.load('Model/Encoder/preprocessing_pipe.joblib')
final_columns= joblib.load('Model/final_columns.joblib')

def preprocessing(df):
    transformed= prepro.transform(df)
    transform_df= pd.DataFrame(transformed, columns= final_columns)

    return transform_df
