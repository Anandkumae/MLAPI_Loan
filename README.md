# 🏦 Loan Approval Predictor API

This API predicts whether a loan application is likely to be approved or rejected using a trained ML model.

## 🚀 Tech Stack
- Python + FastAPI
- MySQL for logging
- Render for deployment
- Model trained on Google Colab

## 🔗 API Endpoints

- `GET /` - Health check
- `POST /predict` - Send applicant data and receive approval status
sample live demo-https://mlapi-loan-9.onrender.com
## 💾 Sample SQL Table

```sql
CREATE DATABASE loan_db;
USE loan_db;

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    income INT,
    loan_amount FLOAT,
    result VARCHAR(10)
);
