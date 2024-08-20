# Credit Worthiness Forecaster

## Problem Statement
Lenders face challenges in effectively predicting which individuals are at higher risk of defaulting on their loans. Inaccurate predictions can lead to significant financial losses, either by extending credit to high-risk individuals or by denying credit to individuals who are actually creditworthy. The goal is to create a robust machine-learning model that can accurately predict the likelihood of an individual defaulting on a loan based on their historical loan repayment behavior and transactional activities.

## Dataset
This dataset contains information on loans made through the Lending Club platform, a peer-to-peer lending company that connects borrowers with investors. The dataset includes data on loans issued between 2007 and 2018.

The goal of this dataset is to predict whether a borrower will fully pay off their loan or default.

### Dataset Columns
The dataset includes the following 27 columns:

- `loan_amnt`: The listed amount of the loan applied for by the borrower.
- `term`: The number of payments on the loan. Values are in months and can be either 36 or 60.
- `int_rate`: Interest Rate on the loan.
- `installment`: The monthly payment owed by the borrower if the loan originates.
- `grade`: LC assigned loan grade.
- `sub_grade`: LC assigned loan subgrade.
- `emp_title`: The job title supplied by the borrower when applying for the loan.
- `emp_length`: Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years.
- `home_ownership`: The home ownership status provided by the borrower during registration or obtained from the credit report.
- `annual_inc`: The self-reported annual income provided by the borrower during registration.
- `verification_status`: Indicates if income was verified by LC, not verified, or if the income source was verified.
- `issue_d`: The month which the loan was funded.
- `loan_status`: Current status of the loan.
- `purpose`: A category provided by the borrower for the loan request.
- `title`: The loan title provided by the borrower.
- `zip_code`: The first 3 numbers of the zip code provided by the borrower in the loan application.
- `addr_state`: The state provided by the borrower in the loan application.
- `dti`: A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.
- `earliest_cr_line`: The month the borrower's earliest reported credit line was opened.
- `open_acc`: The number of open credit lines in the borrower's credit file.
- `pub_rec`: Number of derogatory public records.
- `revol_bal`: Total credit revolving balance.
- `revol_util`: Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
- `total_acc`: The total number of credit lines currently in the borrower's credit file.
- `initial_list_status`: The initial listing status of the loan. Possible values are W or F.
- `application_type`: Indicates whether the loan is an individual application or a joint application with two co-borrowers.
- `mort_acc`: Number of mortgage accounts.
- `pub_rec_bankruptcies`: Number of public record bankruptcies.

### Target Variable
The target variable for this dataset is the `loan_status` column. This column indicates whether the borrower has fully paid off their loan or has defaulted.

- A value of "Fully Paid" indicates that the borrower has fully paid off their loan.
- A value of "Default" indicates that the borrower has failed to pay off the loan.

### Source
This dataset was obtained from Kaggle. It was originally compiled by Lending Club and made available through Kaggle.

## Project Overview
1. **Exploratory Data Analysis:** Analyzing and understanding the data, including data visualization, identifying missing values, outliers, and understanding the relationship between the features.
2. **Data Cleaning:** Handling missing values, outliers, and removing irrelevant features that are not useful in our analysis.
3. **Categorical to Numerical:** Converting categorical variables into numerical ones using different encoding techniques.
4. **Feature Engineering:** Creating new features from existing ones that may improve our model's performance.
5. **Model Training:** Model training using various algorithms such as Logistic Regression, XGBoost, and Random Forest Classifier (RFC).
6. **Front-end Development:** Creating a user-friendly front-end using Streamlit, a Python library for building interactive web applications.

## Model Training
We trained our model using various Machine Learning algorithms such as Logistic Regression, XGBoost, and Random Forest Classifier (RFC). The following table shows the accuracy achieved by each model:

| Model                  | Accuracy |
|------------------------|----------|
| XGBoost                | 0.8851   |
| Logistic Regression    | 0.8034   |
| Random Forest Classifier | 0.8034 |

Based on the accuracy achieved, we selected XGBoost as our final model.

## Deployment
We deployed the XGBoost model using a Streamlit front-end, allowing users to input loan information and receive a prediction of whether the loan will be fully paid or will default.

## Repository Structure
- **data/**: Contains the dataset used for the project.
- **src/**: Contains necessary files required for the development of a user interface that utilizes the Streamlit platform.
  - `Streamlit.py`: Contains the Streamlit front-end code for the deployed application.
  - `bestmodelxgboost.pkl`: Contains saved trained model.
  - `bestmodelxgboost.joblib`: Contains saved trained model.
- **models/**: Contains the trained models.
  - `modelxgboost.ipynb`
  - `model_randomforest.ipynb`
  - `model_catboost.ipynb`
  - `Gridsearchanalysis.ipynb`

## Installation

### Requirements
- Python 3.11 or higher
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit

### Installation
To install the project, first clone the repository:
## Running the Project
To run the deployed application, navigate to the project directory in your command prompt or terminal and run the following command:

```bash
streamlit run app.py
This will launch the application in your browser, where you can input loan information and receive a prediction of whether the loan will be fully paid or will default.

The Streamlit.py file in the src directory contains the Streamlit front-end code for the deployed application.
This README.md provides a well-structured overview of the project, including problem definition, dataset description, project steps, model training, deployment, and repository structure.
