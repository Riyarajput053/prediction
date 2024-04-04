import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


#----loading the saved models---
diabetes_model = pickle.load(open('models/diabetes_pred_model.sav', 'rb'))
heart_disease_model = pickle.load(open('models/heart_disease_model.sav', 'rb'))

#---sidebar for navigation---
with st.sidebar:
    selected = option_menu("Patient's insights",
                           ['Diabetes Prediction',
                           'Heart disease prediction'],
                           icons = ['activity','heart-pulse-fill' ],   # bootstrap icons
                           default_index = 0)
    
# -------------------diabetes prediction page-------------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    
    gender_options = {
        "Male": 0,
        "Female": 1,
        "Other" : 2
    }
    hypertension_options = {
        "Yes" : 1,
        "No" : 0
    }
    heartdisease_options = {
        "Yes" : 1,
        "No" : 0
    }
    smoking_options = {
        "Never" : 0,
        "Former" : 3,
        "Currently" : 1,        
    }
    
    # columns for input field
    col1, col2 = st.columns(2)
    
    with col1:
        selected_gender = st.selectbox("Select your gender", list(gender_options.keys()))
        selected_gender_value = gender_options[selected_gender]

    with col2:
        age = st.text_input('age')
    with col1:
        hypertension = st.selectbox("Blood Pressure", list(hypertension_options.keys()))
        selected_hypertension = hypertension_options[hypertension]
    with col2:
        heart_disease = st.selectbox("Heart disease", list(heartdisease_options.keys()))
        selected_heart_disease = heartdisease_options[heart_disease]
    with col1:
        smoking_history = st.selectbox("Smoking History", list(smoking_options.keys()))
        selected_smoking_history = smoking_options[smoking_history]
    with col2:
        BMI = st.text_input('BMI')
    with col1:
        HbA1c_level = st.text_input('HbA1c_level')
    with col2:
        blood_glucose_level = st.text_input('blood_glucose_level')
    
    # code for prediction
    diab_diagnosis = ''
    

    # button for prediction
    if st.button('Diabetes test result'):
        if age=='' or BMI=='' or HbA1c_level=='' or blood_glucose_level=='': 
            st.warning("Please fill all the details")
        else:
            input_data_diab = [selected_gender_value,age,selected_hypertension,selected_heart_disease,selected_smoking_history,BMI,HbA1c_level,blood_glucose_level]
            input_data_diab = [float(x) for x in input_data_diab]
           
            print("Input Data for Prediction:", input_data_diab)
            diab_prediction = diabetes_model.predict([input_data_diab])   # double brackets to tell model that we are predicting on only one instance
    
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person can be diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

    
# ---------------------heart disease prediction page--------------------
else:
    st.title('Heart health')
    
    gender_options = {
        "Male": 0,
        "Female": 1,
        "Other" : 2
    }
    chest_pain_type = { "Typical Angina" : 0, "Atypical Angina":1, "Non-anginal pain":2, "Asymptomatic":3}
    fbs_option = { "True" : 1, "False" : 0}
    rest = { "Normal" :0, "having ST-T wave abnormality":1, " showing probable or definite left ventricular hypertrophy by Estes' criteria":2}
    exer = { "Yes":1, "No":0}
    sloping = { "Upsloping":0, "Flat":1, "Downsloping":2}
    thalium = {"Normal" :0, "Fixed defect":1, "Reversible defect":2, "Not described":3}
     # columns for input field
    col1, col2 = st.columns(2)
    
    
    with col1:
        age = st.text_input('Age')
    with col2:
        gender = st.selectbox("Select your gender", list(gender_options.keys()))
        sel_gender = gender_options[gender]
    with col1:
        cp = st.selectbox("Chest Pain type", list(chest_pain_type.keys()))
        sel_cp = chest_pain_type[cp]
    with col2:
        trestbps = st.text_input('Resting blood pressure (in mm Hg)')
    with col1:
        chol = st.text_input('Cholestoral in mg/dl fetched via BMI sensor')
    with col2:
        fbs = st.selectbox("fasting blood sugar > 120 mg/dl", list(fbs_option.keys()))
        sel_fbs = fbs_option[fbs]
    with col1:
        restecg = st.selectbox("Resting electrocardiographic results", list(rest.keys()))
        sel_restecg = rest[restecg]
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    with col1:
        exang = st.selectbox("Exercise induced angina ", list(exer.keys()))
        sel_exang = exer[exang]
                             
    with col2:
        oldpeak = st.text_input('Previous peak')
    with col1:
        slope = st.selectbox("Slope", list(sloping.keys()))
        sel_slope = sloping[slope]
    with col2:
        ca= st.text_input('Number of major vessels (0-4) colored by flourosopy')
    with col1:
        thal = st.selectbox("Thalium Stress Test result ", list(thalium.keys()))
        sel_thal = thalium[thal]
     
    
    heart_diagnosis = ''
    input_data = [age, sel_gender, sel_cp, trestbps, chol, sel_fbs, sel_restecg, sel_thal, sel_exang, oldpeak, sel_slope, ca, sel_thal]
    input_data = [float(x) for x in input_data]
    # Check if all inputs are numeric
    if st.button('Heart Disease test result'):
        if age=='' or trestbps=='' or chol=='' or thalach=="" or oldpeak=='' or ca=='' or thal=='' :
            st.warning("Please fill out all the details")
        else:
        # Predict using the model
            print("Input Data for Prediction:", input_data)
            heart_prediction = heart_disease_model.predict([input_data])
        
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has a healthy heart'
            else:
                heart_diagnosis = 'The person has an unhealthy heart'

    # Display the diagnosis
    st.success(heart_diagnosis)
