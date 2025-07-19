from pydantic import BaseModel

class ApplicantData(BaseModel):
    gender: int
    married: int
    dependents: int
    education: int
    self_employed: int
    applicant_income: float
    coapplicant_income: float
    loan_amount: float
    loan_amount_term: float
    credit_history: int
    property_area: int
    loan_purpose: int

