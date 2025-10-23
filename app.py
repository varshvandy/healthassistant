# -------------------------------
# Smart Health Assistant - Streamlit Web App
# -------------------------------

# Step 1: Install Streamlit (only in Colab)
# !pip install streamlit

# Step 2: Import Libraries
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 3: Load or Create Dataset
data = {
    'Symptoms': [
        'fever cough headache',
        'chest pain shortness of breath',
        'stomach pain nausea vomiting',
        'joint pain swelling',
        'sore throat cough fever',
        'runny nose sneezing',
        'dizziness blurred vision',
        'back pain muscle stiffness',
        'rash itching fever',
        'fatigue weight loss'
    ],
    'Disease': [
        'Flu',
        'Heart Attack',
        'Food Poisoning',
        'Arthritis',
        'Cold',
        'Allergy',
        'Migraine',
        'Muscle Strain',
        'Chickenpox',
        'Diabetes'
    ],
    'Precautions': [
        'Rest, drink fluids, take paracetamol',
        'Call emergency, take aspirin, consult doctor immediately',
        'Drink water, rest, avoid spicy food',
        'Apply ice, rest joints, consult doctor',
        'Rest, warm fluids, avoid cold drinks',
        'Take antihistamines, avoid allergens',
        'Rest in dark room, drink water, consult doctor if severe',
        'Rest, apply heat/cold packs, avoid heavy lifting',
        'Isolate, take antiviral medication, consult doctor',
        'Maintain healthy diet, regular exercise, consult doctor'
    ]
}

df = pd.DataFrame(data)

# Step 4: Prepare ML Model
le = LabelEncoder()
y = le.fit_transform(df['Disease'])
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Symptoms'])
model = MultinomialNB()
model.fit(X, y)

# Step 5: Prediction Function
def predict_disease(symptom_text):
    symptom_text = symptom_text.lower()
    X_input = vectorizer.transform([symptom_text])
    disease_pred = model.predict(X_input)
    disease = le.inverse_transform(disease_pred)[0]
    precautions = df[df['Disease'] == disease]['Precautions'].values[0]
    return disease, precautions

# -------------------------------
# Streamlit Web App Interface
# -------------------------------

st.title("🩺 Smart Health Assistant")
st.write("Type your symptoms separated by spaces (e.g., 'fever cough headache')")

# User input
user_input = st.text_input("Enter your symptoms:")

if st.button("Predict Disease"):
    if user_input.strip() != "":
        disease, precautions = predict_disease(user_input)
        st.success(f"Predicted Disease: {disease}")
        st.info(f"Precautions / Advice: {precautions}")
    else:
        st.warning("Please enter your symptoms before clicking Predict")
        import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------------------
# Page configuration
st.set_page_config(
    page_title="🩺 Smart Health Assistant",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Custom CSS styling
st.markdown("""
<style>
body {
    background-color: #f0f8ff;
}
h1 {
    color: #ff4b5c;
    text-align: center;
    font-family: 'Arial Black', sans-serif;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border-radius: 10px;
}
.stTextInput>div>div>input {
    border-radius: 10px;
    padding: 10px;
    border: 2px solid #4CAF50;
}
.stMarkdown {
    font-family: 'Verdana', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Dataset
data = {
    'Symptoms': [
        'fever cough headache',
        'chest pain shortness of breath',
        'stomach pain nausea vomiting',
        'joint pain swelling',
        'sore throat cough fever',
        'runny nose sneezing',
        'dizziness blurred vision',
        'back pain muscle stiffness',
        'rash itching fever',
        'fatigue weight loss'
    ],
    'Disease': [
        'Flu',
        'Heart Attack',
        'Food Poisoning',
        'Arthritis',
        'Cold',
        'Allergy',
        'Migraine',
        'Muscle Strain',
        'Chickenpox',
        'Diabetes'
    ],
    'Precautions': [
        'Rest, drink fluids, take paracetamol',
        'Call emergency, take aspirin, consult doctor immediately',
        'Drink water, rest, avoid spicy food',
        'Apply ice, rest joints, consult doctor',
        'Rest, warm fluids, avoid cold drinks',
        'Take antihistamines, avoid allergens',
        'Rest in dark room, drink water, consult doctor if severe',
        'Rest, apply heat/cold packs, avoid heavy lifting',
        'Isolate, take antiviral medication, consult doctor',
        'Maintain healthy diet, regular exercise, consult doctor'
    ]
}

df = pd.DataFrame(data)

# ---------------------------
# Prepare ML Model
le = LabelEncoder()
y = le.fit_transform(df['Disease'])
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Symptoms'])
model = MultinomialNB()
model.fit(X, y)

def predict_disease(symptom_text):
    symptom_text = symptom_text.lower()
    X_input = vectorizer.transform([symptom_text])
    disease_pred = model.predict(X_input)
    disease = le.inverse_transform(disease_pred)[0]
    precautions = df[df['Disease'] == disease]['Precautions'].values[0]
    return disease, precautions

# ---------------------------
# App Interface
st.title("🩺 Smart Health Assistant")

user_input = st.text_input("Enter your symptoms here (e.g., 'fever cough headache'):")

if st.button("Predict Disease"):
    if user_input.strip() != "":
        disease, precautions = predict_disease(user_input)
        st.success(f"Predicted Disease: {disease}")
        st.info(f"Precautions / Advice: {precautions}")
    else:
        st.warning("Please enter your symptoms first!")
        import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------------------
# Page configuration
st.set_page_config(
    page_title="🩺 Smart Health Assistant",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Custom CSS styling
st.markdown("""
<style>
body {
    background-color: #f0f8ff;
}
h1 {
    color: #ff4b5c;
    text-align: center;
    font-family: 'Arial Black', sans-serif;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border-radius: 10px;
}
.stTextInput>div>div>input {
    border-radius: 10px;
    padding: 10px;
    border: 2px solid #4CAF50;
}
.stMarkdown {
    font-family: 'Verdana', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Dataset
data = {
    'Symptoms': [
        'fever cough headache',
        'chest pain shortness of breath',
        'stomach pain nausea vomiting',
        'joint pain swelling',
        'sore throat cough fever',
        'runny nose sneezing',
        'dizziness blurred vision',
        'back pain muscle stiffness',
        'rash itching fever',
        'fatigue weight loss'
    ],
    'Disease': [
        'Flu',
        'Heart Attack',
        'Food Poisoning',
        'Arthritis',
        'Cold',
        'Allergy',
        'Migraine',
        'Muscle Strain',
        'Chickenpox',
        'Diabetes'
    ],
    'Precautions': [
        'Rest, drink fluids, take paracetamol',
        'Call emergency, take aspirin, consult doctor immediately',
        'Drink water, rest, avoid spicy food',
        'Apply ice, rest joints, consult doctor',
        'Rest, warm fluids, avoid cold drinks',
        'Take antihistamines, avoid allergens',
        'Rest in dark room, drink water, consult doctor if severe',
        'Rest, apply heat/cold packs, avoid heavy lifting',
        'Isolate, take antiviral medication, consult doctor',
        'Maintain healthy diet, regular exercise, consult doctor'
    ]
}

df = pd.DataFrame(data)

# ---------------------------
# Prepare ML Model
le = LabelEncoder()
y = le.fit_transform(df['Disease'])
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Symptoms'])
model = MultinomialNB()
model.fit(X, y)

def predict_disease(symptom_text):
    symptom_text = symptom_text.lower()
    X_input = vectorizer.transform([symptom_text])
    disease_pred = model.predict(X_input)
    disease = le.inverse_transform(disease_pred)[0]
    precautions = df[df['Disease'] == disease]['Precautions'].values[0]
    return disease, precautions

# ---------------------------
# App Interface
st.title("🩺 Smart Health Assistant")

user_input = st.text_input("Enter your symptoms here (e.g., 'fever cough headache'):")

if st.button("Predict Disease"):
    if user_input.strip() != "":
        disease, precautions = predict_disease(user_input)
        st.success(f"Predicted Disease: {disease}")
        st.info(f"Precautions / Advice: {precautions}")
    else:
        st.warning("Please enter your symptoms first!")