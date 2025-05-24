import joblib


model = joblib.load('Model/RandomForestClassifier.joblib')
result_target = joblib.load('Model/Encoder/encoder_target.joblib')

def predict(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result (Good, Standard, or Poor)
    """
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result
