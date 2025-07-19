from pydantic import BaseModel

from pydantic import BaseModel

class ApplicantData(BaseModel):
    Gender: int
    Married: int
    Education: int
    ApplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: int
    Property_Area: int


