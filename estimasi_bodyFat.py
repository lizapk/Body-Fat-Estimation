import pickle
import streamlit as st

model = pickle.load(open('estimasi_bodyFat.sav', 'rb'))

st.title('Estimasi Persentase Body Fat')

Density = st.number_input('Input Density (Kepadatan ditentukan dari penimbangan bawah air)')
Age = st.number_input('Input Umur (tahun)')
Weight = st.number_input('Input Berat Badan (lbs)')
Height = st.number_input('Input Tinggi Badan(inchies)')
Neck = st.number_input('Input Lingkar Leher (cm)')
Chest = st.number_input('Input Lingkar Dada (cm)')
Abdomen = st.number_input('Input Lingkar Perut (cm)')
Hip = st.number_input('Input Lingkar Pinggul (cm)')
Thigh = st.number_input('Input Lingkar Paha (cm)')
Knee = st.number_input('Input Lingkar Lutut (cm)')
Ankle = st.number_input('Input Lingkar Pergelangan Kaki (cm)')
Biceps = st.number_input('Input Lingkar Bisep (cm)')
Forearm = st.number_input('Input Lingkar Lengan bawah (cm)')
Wrist = st.number_input('Input Lingkar Pergelangan Tangan (cm)')

predict = ''

if st.button('Proses'):
    predict = model.predict(
        [[Density,Age,Weight,Height,Neck,Chest,Abdomen,Hip,Thigh,Knee,Ankle,Biceps,Forearm,Wrist]]
    )
    st.write ('Estimasi Persentase Lemak Tubuh : ', predict)
    st.write ('Total Lemak Tubuh (Kg) : ', predict*Weight*0.453592)
