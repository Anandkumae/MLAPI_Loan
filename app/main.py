from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.predictor import predict
from app.schema import ApplicantData

app = FastAPI()
origins = [
    "https://mlapi-loan-9.onrender.com",  # your frontend Render app URL
]

# 👇 Add this middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mlapi-loan-9.onrender.com"],  # your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def get_prediction(data: ApplicantData):
    result = predict(data)
    return {"prediction": result}



