import joblib
import numpy as np

model = joblib.load("model/loan_model.joblib")

def encode_input(data):
    gender_map = {"Male": 1, "Female": 0}
    married_map = {"Yes": 1, "No": 0}
    education_map = {"Graduate": 1, "Not Graduate": 0}
    self_employed_map = {"Yes": 1, "No": 0}
    property_area_map = {"Urban": 2, "Semiurban": 1, "Rural": 0}

    return [
        gender_map.get(data['gender'], 0),
        married_map.get(data['married'], 0),
        data['dependents'],
        education_map.get(data['education'], 0),
        self_employed_map.get(data['self_employed'], 0),
        data['applicant_income'],
        data['coapplicant_income'],
        data['loan_amount'],
        data['loan_amount_term'],
        data['credit_history'],
        property_area_map.get(data['property_area'], 0),
    ]
def predict(input_data: list) -> str:
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return "Approved" if prediction[0] == 1 else "Rejected"


