import streamlit as st

st.title('Heart Health')

gender_options = {"Male": 0, "Female": 1, "Other": 2}
chest_pain_type = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal pain": 2, "Asymptomatic": 3}
fbs_option = {"True": 1, "False": 0}
rest = {"Normal": 0, "having ST-T wave abnormality": 1,
        "showing probable or definite left ventricular hypertrophy by Estes' criteria": 2}
exer = {"Yes": 1, "No": 0}
sloping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
thalium = {"Normal": 0, "Fixed defect": 1, "Reversible defect": 2, "Not described": 3}

# Columns for input field
col1, col2 = st.columns(2)

with col1:
    age = st.text_input('Age')
    cp = st.selectbox("Chest Pain type", list(chest_pain_type.keys()))
    trestbps = st.text_input('Resting blood pressure (in mm Hg)')
    chol = st.text_input('Cholestoral in mg/dl fetched via BMI sensor')
    restecg = st.selectbox("Resting electrocardiographic results", list(rest.keys()))
    thalach = st.text_input('Maximum heart rate achieved')
    oldpeak = st.text_input('Previous peak')
    ca = st.text_input('Number of major vessels (0-4) colored by flourosopy')

with col2:
    gender = st.selectbox("Select your gender", list(gender_options.keys()))
    fbs = st.selectbox("fasting blood sugar > 120 mg/dl", list(fbs_option.keys()))
    exang = st.selectbox("Exercise induced angina ", list(exer.keys()))
    slope = st.selectbox("Slope", list(sloping.keys()))
    thal = st.selectbox("Thalium Stress Test result ", list(thalium.keys()))

heart_diagnosis = ''

if st.button('Heart Disease test result'):
    if age == '' or trestbps == '' or chol == '' or thalach == "" or oldpeak == '' or ca == '' or thal == '':
        st.warning("Please fill out all the details")
    else:
        try:
            # Convert input to appropriate types
            age = float(age)
            trestbps = float(trestbps)
            chol = float(chol)
            thalach = float(thalach)
            oldpeak = float(oldpeak)
            ca = float(ca)
            
            # Get selected options
            sel_gender = gender_options[gender]
            sel_cp = chest_pain_type[cp]
            sel_fbs = fbs_option[fbs]
            sel_restecg = rest[restecg]
            sel_exang = exer[exang]
            sel_slope = sloping[slope]
            sel_thal = thalium[thal]

            # Prepare input data
            input_data = [age, sel_gender, sel_cp, trestbps, chol, sel_fbs, sel_restecg, sel_thal, sel_exang,
                          oldpeak, sel_slope, ca, sel_thal]

            # Predict using the model
            print("Input Data for Prediction:", input_data)
            

            
             heart_prediction = heart_disease_model.predict([input_data])
             if heart_prediction[0] == 1:
                 heart_diagnosis = 'The person has a healthy heart'
             else:
                 heart_diagnosis = 'The person has an unhealthy heart'
            heart_diagnosis = 'Mock result: The person has a healthy heart'

        except ValueError:
            st.error("Error: Invalid input. Please ensure all inputs are numeric.")
            # Clear the diagnosis if there's an error
            heart_diagnosis = ''

# Display the diagnosis
st.success(heart_diagnosis)
