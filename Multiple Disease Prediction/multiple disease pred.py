# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 23:08:50 2025

@author: USER
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model = pickle.load(open('E:/ML projects/multiple disease web deploy using streamlit/diabetes_trained_model.sav','rb'))

heart_disease_model =  pickle.load(open("E:/ML projects/multiple disease web deploy using streamlit/heart_training_model.sav", 'rb'))

parkinsons_model = pickle.load(open("E:/ML projects/multiple disease web deploy using streamlit/parkinsons_training_model.sav", 'rb'))

breast_cancer_model = pickle.load(open("E:/ML projects/multiple disease web deploy using streamlit/breast_cancer_training_model.sav", 'rb'))


#sidebar for navigation

with st.sidebar:
    selected = option_menu("Multiple Disease prediction System using ML",
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons = ['activity','heart','person','person-standing-dress'],  #these are icons from bootstrap, streamlit supports bootstrap
                           
                           default_index = 0) # when web page is run the default page is diabetes prediction
    

#Diabetes predictiion page
if (selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes prediction using ML')
    
    
    #getting the input data from the user
    #columns for input fields
    
    #the order must be same as in the data set
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPresure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThicknes = st.text_input('Skin thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin value')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes predigree function value')
    
    with col2:
        Age = st.text_input('Age of the person')
    
    

    
    #code for prediction
    diab_diagnosis = ''  #empty string to store the end result
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_pred = [Pregnancies, Glucose,BloodPresure, SkinThicknes, Insulin, BMI, DiabetesPedigreeFunction, Age]
        #the columns names are in 2 square brackets to tell the model that we are predicting for one data point
        
        #to convert the text/string data into numeric data
        diab_pred = [float(x) for x in diab_pred]

        diab_prediction = diabetes_model.predict([diab_pred])

        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'

    st.success(diab_diagnosis)



if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age of the person")
        
    with col2:
        sex = st.text_input("Gender of the person")
    
    with col3:
        cp = st.text_input("Chest pain type")
        
    with col1:
        trestbps = st.text_input("Resting blood pressure")
        
    with col2:
        chol = st.text_input("Serum cholestrol")
        
    with col3:
        fbs = st.text_input("Fasting blood pressure")
        
    with col1:
        restecg = st.text_input("Resting electrocardiographic")
        
    with col2:
        thalach = st.text_input("Maximum heart rate")
        
    with col3:
        exang = st.text_input("Exercise induced angina")
        
    with col1:
        oldpeak = st.text_input("ST depresion induced by exercise relative to rest")
        
    with col2:
        slope = st.text_input("The slope of the peak exercise")
        
    with col3:
        ca = st.text_input("Number of major vessels")
        
    with col1:
        thal = st.text_input("Normal/Defect/Reversable")
        
        
    #code for prediction
    heart_diagnosis = ''  #empty string to store the end result
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_pred = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        #the columns names are in 2 square brackets to tell the model that we are predicting for one data point
        heart_pred = [float(x) for x in heart_pred]

        heart_prediction = heart_disease_model.predict([heart_pred])
        
        if(heart_prediction[0] == 1):
            heart_diagnosis = 'The person is Diabetic'
        else:
            heart_diagnosis = 'The person is not Diabetic'

    st.success(heart_diagnosis)
    
    
    
    
    
    

if(selected =='Parkinsons Prediction'):
    st.title('Parkinsons prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    
    #the order must be same as in the data set
    
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        parkinson_pred = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        parkinson_pred = [float(x) for x in parkinson_pred]

        parkinson_prediction = parkinsons_model.predict([parkinson_pred])
        
        if parkinson_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    

if(selected == 'Breast Cancer Prediction'):
    st.title('Breast Cancer prediction using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius = st.text_input("Mean Radius")
        
    with col2:
        mean_texture = st.text_input("Mean texture")
        
    with col3:
        mean_perimeter = st.text_input("Mean perimeter")
        
    with col1:
        mean_area = st.text_input("Mean area")
        
    with col2:
        mean_smoothness = st.text_input("Mean smoothness")
        
    with col3:
        mean_compactness  = st.text_input("Mean compactness")
        
    with col1:
        mean_concavity = st.text_input("Mean concavity")
        
    with col2:
        mean_concave_points = st.text_input("Mean concave")
            
    with col3:
        mean_symmetry = st.text_input("Mean symmetry")
    
    with col1:
        mean_fractal_dimensions = st.text_input("Mean Fractal Dimensions")
        
    with col2:
        radius_error = st.text_input("Radius Error")
        
    with col3:
        texture_error = st.text_input("Texture Error")
        
    with col1:
        perimeter_error = st.text_input("Perimeter Error")
        
    with col2:
        area_error = st.text_input("Area error")
        
    with col3:
        smoothness_error = st.text_input("Smoothness error")
        
    with col1:
        compactnesss_error = st.text_input("compactness error")
        
    with col2:
        concavity_error = st.text_input("Concavity Error")
        
    with col3:
        concave_points_error = st.text_input("Concave Points error")
        
    with col1:
        symmetry_error = st.text_input("Symmetry error")
        
    with col2:
        fractal_dimension_error = st.text_input("Fractal Dimension error")
        
    with col3:
        worst_radius  = st.text_input("Worst radius")
        
    with col1:
        worst_texture = st.text_input("Worst Texture")
        
    with col2:
        worst_preimeter = st.text_input("Worst Preimeter")
        
    with col3:
        worst_area = st.text_input("Worst area")
        
    with col1:
        worst_smoothness = st.text_input("worst smoothness")
        
    with col2:
        worst_compactness = st.text_input("worst ccompactness")
    
    with col3:
        worst_concavity = st.text_input("Worst Concavity")
        
    with col1:
        worst_concave_points = st.text_input("Worst concave points")
        
    with col2:
        worst_symmetry = st.text_input("worst symmetry")
        
    with col3:
        worst_fractal_dimension = st.text_input("Worst Fractal dimension")
        
    
    
    #code for prediction
    breast_diagnosis = ''  #empty string to store the end result
    
    #creating a button for prediction
    if st.button('Breast Cancer Test Result'):
        breast_pred = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, 
                                                    mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, 
                                                    mean_fractal_dimensions, radius_error, texture_error, perimeter_error, 
                                                    area_error, smoothness_error, compactnesss_error, concavity_error, concave_points_error, 
                                                    symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_preimeter, 
                                                    worst_area, worst_smoothness, worst_compactness,worst_concavity, worst_concave_points, worst_symmetry, 
                                                    worst_fractal_dimension]
        #the columns names are in 2 square brackets to tell the model that we are predicting for one data point
        
        breast_pred = [float(x) for x in breast_pred]

        breast_prediction = diabetes_model.predict([breast_pred])
        

        if(breast_prediction[0] == 1):
            breast_diagnosis = 'The tumor is benign'
        else:
            breast_diagnosis = 'The tumor is malignant'

    st.success(breast_diagnosis)
    


























