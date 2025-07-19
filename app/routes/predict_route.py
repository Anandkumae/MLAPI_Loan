from fastapi import APIRouter
from app.schema.request import ApplicantData
from app.model.predict import predict_loan_approval

router = APIRouter()

@router.post("/predict")
def predict(data: ApplicantData):
    prediction = predict_loan_approval(data)
    return {"prediction": prediction}
