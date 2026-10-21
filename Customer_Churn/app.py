import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Marvellous Infosystem DashBoard")

st.title("Marvellous Infosystem by Piyush Manohar Khirnar")
st.header("Customer Churn Prediction")
st.write("Machine Learnign Application Dashboard")



MODEL_PATH = Path(__file__).parent / "Marvellous_ML_Customer_Churn.pkl"
model = joblib.load(MODEL_PATH)

st.subheader("Enter Customer details")
age = st.number_input("Customer Age:",min_value=1)
tenure = st.number_input("tenure (Months):",min_value=0)
charges = st.number_input("Monthly Charges :",min_value=0)
calls = st.number_input("Support Calls:",min_value=0)

if st.button("Predicted Churn"):
	new_customer = pd.DataFrame({
	
		"Age":[age],
		"Tenure":[tenure],
		"MonthlyCharges":[charges],
		"SupportCalls":[calls]
		
	
	})
	
	prediction = model.predict(new_customer)[0]
	
	if prediction == 1:
		st.error("Customer is likely to churn")

	else:
		st.success("Customer is unlike to churn")
		
st.divider()

st.caption("Marvellous Infosystem DashBoard")




