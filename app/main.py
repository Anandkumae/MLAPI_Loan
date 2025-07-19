from fastapi import FastAPI
from app.schema.request import ApplicantData
from app.predictor import predict
from app.db import get_connection

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Loan Approval Predictor API is live!"}
@app.post("/predict")
def predict_approval(applicant: ApplicantData):
    input_data = [
        applicant.gender,
        applicant.married,
        applicant.dependents,
        applicant.education,
        applicant.self_employed,
        applicant.applicant_income,
        applicant.coapplicant_income,
        applicant.loan_amount,
        applicant.loan_amount_term,
        applicant.credit_history,
        applicant.property_area,
        applicant.loan_purpose
    ]
    result = predict(input_data)
    return {"loan_status": result}


