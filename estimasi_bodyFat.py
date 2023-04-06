import pickle
import streamlit as st

model = pickle.load(open('estimasi_bodyFat.sav', 'rb'))

st.title('Percent body fat Prediction')

Density = st.number_input('Input Your Density (determined from underwater weighing)')
Age = st.number_input('Input Your Age (Years Only)')
Weight = st.number_input('Input Your Weight (lbs)')
Height = st.number_input('Input Your Height(inchies)')
Neck = st.number_input('Input Your Neck circumference (cm)')
Chest = st.number_input('Input Your Chest circumference (cm)')
Abdomen = st.number_input('Input Your Abdomen 2 circumference (cm)')
Hip = st.number_input('Input Your Hip circumference (cm)')
Thigh = st.number_input('Input Your Thigh circumference (cm)')
Knee = st.number_input('Input Your Knee circumference (cm)')
Ankle = st.number_input('Input Your Angkle circumference (cm)')
Biceps = st.number_input('Input Your Biceps circumference (cm)')
Forearm = st.number_input('Input Your Forearm circumference (cm)')
Wrist = st.number_input('Input Your Wrist circumference (cm)')

predict = ''

if st.button('Percent body fat Prediction'):
    predict = model.predict(
        [[Density,Age,Weight,Height,Neck,Chest,Abdomen,Hip,Thigh,Knee,Ankle,Biceps,Forearm,Wrist]]
    )
    st.write ('Your Percent body fat Prediction is : ', predict)
    st.write ('Your Over Weight in Kg : ', predict*Weight)