import streamlit as st

# Page title
st.title("BMI Calculator")

# Text input for Name
name = st.text_input("Name:")

# Radio button for Gender
gender = st.radio("Gender:", ("Male", "Female", "Other"))

# Numeric input for Age
age = st.number_input("Age:", min_value=1, max_value=120)

# Text input for Address
address = st.text_area("Address:")

# Checkbox for Hobbies
hobbies = st.checkbox("Select hobbies:", ("Reading", "Gaming", "Traveling", "Cooking"))

# Numeric input for Weight
weight = st.number_input("Weight (in kg):", min_value=1, max_value=500)

# Numeric input for Height
height = st.number_input("Height (in cm):", min_value=1, max_value=300)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / ((height/100) ** 2)
    st.write("Your BMI is:", round(bmi, 2))
    st.write("You are underweight" if bmi < 18.5 else
             "You have a healthy weight" if bmi >= 18.5 and bmi <= 24.9 else
             "You are overweight" if bmi >= 25 and bmi <= 29.9 else
             "You have obesity" if bmi >= 30 else "")