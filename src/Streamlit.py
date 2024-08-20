import pickle
from PIL import Image
import streamlit as st
 
# Load the image and display it in the Streamlit app
img1 = Image.open("bank1.png")
st.image(img1, use_column_width=False)

# Load the pre-trained model using pickle
pickle_in = open('bestmodelxgboost.pkl', 'rb') 
classifier = pickle.load(pickle_in)

# Define the function that will make predictions based on user inputs
def prediction(loan_amnt, term, int_rate, installment, grade, 
        home_ownership, annual_inc, verification_status, 
        purpose, dti, earliest_cr_line, 
        pub_rec, revol_bal, revol_util, total_acc, 
        mort_acc, postal_code):   
   
    # Make a prediction using the classifier model
    prediction = classifier.predict( 
        [[loan_amnt, term, int_rate, installment, grade, 
        home_ownership, annual_inc, verification_status, 
        purpose, dti, earliest_cr_line, 
        pub_rec, revol_bal, revol_util, total_acc, 
        mort_acc, postal_code]])
     
    # Interpret the prediction result
    if prediction == 0:
        pred = 'Unfortunately, the loan is likely to be rejected'
    else:
        pred = 'Congratulations, the loan is likely to be approved.'
    
    return pred
  
# Main function to define the layout of the web app
def main():       
      
    # Creating input boxes where users can enter data required for prediction
    loan_amnt = st.number_input("Loan Amount", min_value=1000, max_value=5000000, value=10000)
    term = st.selectbox("Term (in months)", [36, 60])
    int_rate = st.number_input("Interest Rate", min_value=5.0, max_value=40.0, value=10.0)
    installment = st.number_input("Installment", min_value=10.0, max_value=2000.0, value=200.0)
    grade = st.number_input("Grade (1 to 7)", min_value=1, max_value=7, value=1)
    home_ownership = st.number_input("Home Ownership (1: Own, 2: Mortgage, 3: Rent)", min_value=1, max_value=3, value=2)
    annual_inc = st.number_input("Annual Income", min_value=1000.0, max_value=1000000.0, value=50000.0)
    verification_status = st.number_input("Verification Status (1: Verified, 0: Not Verified)", min_value=0, max_value=1, value=1)
    purpose = st.number_input("Purpose (1: Debt consolidation, 2: Credit card, ...)", min_value=1, max_value=14, value=1)
    dti = st.number_input("Debt-to-Income Ratio (DTI)", min_value=0.0, max_value=10000.0, value=10.0)
    earliest_cr_line = st.number_input("Earliest Credit Line (Year)", min_value=1900, max_value=2024, value=2000)
    pub_rec = st.number_input("Public Records", min_value=0, max_value=86, value=0)
    revol_bal = st.number_input("Revolving Balance", min_value=0.0, max_value=3500000.0, value=1000.0)
    revol_util = st.number_input("Revolving Utilization Rate (%)", min_value=0.0, max_value=100.0, value=30.0)
    total_acc = st.number_input("Total Accounts", min_value=2, max_value=151, value=10)
    mort_acc = st.number_input("Mortgage Accounts", min_value=0, max_value=34, value=1)
    postal_code = st.number_input("Postal Code")
    
    result = ""
      
    # When the 'Predict' button is clicked, make the prediction and display the result
    if st.button("Predict"): 
        result = prediction(loan_amnt, term, int_rate, installment, grade, 
        home_ownership, annual_inc, verification_status, 
        purpose, dti, earliest_cr_line, 
        pub_rec, revol_bal, revol_util, total_acc, 
        mort_acc, postal_code) 
        st.success(result)

# Run the main function when the script is executed
if __name__=='__main__': 
    main()