import streamlit as st
import joblib
from extract_interface import parse_sms

st.set_page_config(page_title="Mobile Money Fraud Detection", page_icon=":money_with_wings:", layout="centered")

st.markdown("""
<style>
/* ---------- Global background & font ---------- */
.stApp {
    background: linear-gradient(160deg, #0b1220 0%, #101c30 45%, #0b1220 100%);
    font-family: 'Segoe UI', 'Inter', sans-serif;
}

/* ---------- Title ---------- */
h1 {
    color: #eef4fb !important;
    font-weight: 800 !important;
    text-shadow: 0 2px 12px rgba(45, 212, 191, 0.35);
    padding-bottom: 10px;
    border-bottom: 2px solid rgba(45, 212, 191, 0.3);
    margin-bottom: 25px !important;
}

/* ---------- Labels ---------- */
label, .stTextInput label, .stNumberInput label {
    color: #a9c1d9 !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    margin-bottom: 6px !important;
}

/* ---------- Text input & number input fields ---------- */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background-color: #16233a !important;
    color: #eef4fb !important;
    border: 1px solid rgba(45, 212, 191, 0.25) !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    transition: all 0.25s ease-in-out;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border: 1px solid #2dd4bf !important;
    box-shadow: 0 0 12px rgba(45, 212, 191, 0.5) !important;
}

/* ---------- Number input +/- buttons ---------- */
.stNumberInput button {
    background-color: #1c2c47 !important;
    color: #eef4fb !important;
    border: none !important;
    border-radius: 8px !important;
    transition: background-color 0.2s ease-in-out;
}

.stNumberInput button:hover {
    background-color: #2dd4bf !important;
    color: #0b1220 !important;
}

/* ---------- Predict button ---------- */
.stButton > button {
    background: linear-gradient(135deg, #f5a623, #d4820a);
    color: #14100a !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 30px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px;
    box-shadow: 0 4px 15px rgba(245, 166, 35, 0.4);
    transition: all 0.25s ease-in-out;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ffb946, #e0910f);
    box-shadow: 0 6px 22px rgba(245, 166, 35, 0.6);
    transform: translateY(-2px);
}

.stButton > button:active {
    transform: translateY(0px) scale(0.98);
}

/* ---------- Result / alert boxes ---------- */
.stAlert {
    border-radius: 12px !important;
    border: 1px solid rgba(45, 212, 191, 0.25) !important;
    background-color: #16233a !important;
}

/* ---------- Scrollbar polish ---------- */
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-track {
    background: #0b1220;
}
::-webkit-scrollbar-thumb {
    background: #2dd4bf;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("Mobile Money Fraud Detection")

st.write("This application predicts whether a mobile money transaction is legitimate, suspicious, or fraudulent based on the transaction details provided.")

st.warning("Please note that no personal information is collected or stored. The prediction is based solely on the transaction details you provide.")

sms = st.text_input("Paste the transaction message:")

transaction_id, amount, hour = parse_sms(sms)

acc_age = st.number_input("Enter the account age in days:", min_value=0, step=1)

avg_daily_trans = st.number_input("Enter the average daily transactions:", min_value=0, step=1)

dist_from_usual_location = st.number_input("Enter the distance from usual location in km:", min_value=0, step=1)

time_since_last_transaction = st.number_input("Enter the time since last transaction in minutes:", min_value=0, step=1)

predict = st.button("Predict Fraud")

if predict:
    # Load the trained model
    model = joblib.load('Fraud_model.pkl')

    # Prepare the input data for prediction
    input_data = [[amount, hour, acc_age, avg_daily_trans, dist_from_usual_location, time_since_last_transaction]]
    
    # Make the prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    # Display the prediction result
    if prediction == 'Fraudulent':
        st.error(f"Transaction ID: {transaction_id} - Fraudulent transaction detected!")
    elif prediction == 'Suspicious':
        st.warning(f"Transaction ID: {transaction_id} - Suspicious transaction detected!")
    else:
        st.success(f"Transaction ID: {transaction_id} - Transaction is legitimate.")

