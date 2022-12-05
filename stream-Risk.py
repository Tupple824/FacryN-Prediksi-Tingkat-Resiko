import pickle
import streamlit as st

# load save model
model = pickle.load(open('Martial_Healt.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Tingkat Intensitas Resiko Selama Kehamilan')

# Form Input
Age = st.text_input('Masukan Umur (Dengan Range 10 - 70 thn)')

SystolicBP = st.text_input('Masukan Nilai Tekanan Darah Yang Lebih Tinggi Dalam mmHg ( Dengan Range 70, ...., 160') 

DiastolicBP = st.text_input('Masukan Nilai Tekanan Darah Yang Lebih Rendah Dalam mmHg( Dengan Range 49, ..., 100')

BS = st.text_input('Masukan Nilai Kadar Glukosa Dalam Darah Dalam mmol/L (Dengan Range 6, ..., 9')

BodyTemp = st.text_input('Masukan Nilai Temperatur Badan ( Dengan Range 98, ..., 103')

HeartRate = st.text_input('Masukan Nilai Detak Jantung Dalam Keadaan Normal  ( Dengan Range 7,..., 90')


# kode Prediksi
Maternal_diagnosis =''

#Button Prediksi
if st.button('Prediksi Resiko'):
    Maternal_prediction = model.predict([[Age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate]])

    if(Maternal_prediction[0]==0):
        Maternal_diagnosis = 'Tingkat Resiko Rendah'
    elif(Maternal_prediction[0]==1):
        Maternal_diagnosis = 'Tingkat Resiko Sedang'
    else:
        Maternal_diagnosis = 'Tingkat Resiko Tinggi'
st.success(Maternal_diagnosis)