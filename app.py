import streamlit as slt
import pandas as pd
import joblib
from data_prep import preprocessing
from custom_transformers import ColumnSelectorTransformer, ToDataFrameTransformer, convert_to_df, get_feature_names
from prediction import predict

categorical_columns= joblib.load('Model/categorical_columns.joblib')

col1, col2= slt.columns([1, 5])
with col1:
    slt.image("foto/GedungSekolah.png", width=200)
with col2:
    slt.header('Predict Student App(Prototype)')


df= pd.DataFrame()

slt.subheader("Data Orang Tua")
slt.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)
col1, col2= slt.columns(2)
with col1:
    Mothers_occupation= slt.selectbox("Mothers Occupation", options= categorical_columns["Mothers_occupation"],
                                    index=2)
    df["Mothers_occupation"]= [Mothers_occupation]
with col2:
    Fathers_occupation= slt.selectbox("Fathers Occupation",
                                    options= categorical_columns["Fathers_occupation"],
                                    index=1)
    df["Fathers_occupation"]= [Fathers_occupation]
col3, col4= slt.columns(2)
with col3:
    Mothers_qualification= slt.selectbox("Mothers Qualification",
                                        options= categorical_columns["Mothers_qualification"], index=2)
    df["Mothers_qualification"]= [Mothers_qualification]
with col4:
    Fathers_qualification= slt.selectbox("Fathers Qualification",
                                        options= categorical_columns["Fathers_qualification"], index=2)
    df["Fathers_qualification"]= [Fathers_qualification] 

slt.subheader("Data Pribadi")
slt.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)
col1, col2, col3= slt.columns(3)
with col1:
    age= int(slt.number_input(label='Age', value=25))
    df["Age_at_enrollment"]= age
with col2:
    gender= slt.selectbox("Gender",
                    options= categorical_columns["Gender"],
                    index=0)
    df["Gender"]= [gender]
with col3:
    marital_status= slt.selectbox("Marital Status",
                            options= categorical_columns["Marital_status"],
                            index=2)
    df["Marital_status"]= [marital_status]

col4, col5, col6= slt.columns(3)
with col4:
    nacionality= slt.selectbox("Nacionality",
                        options= categorical_columns["Nacionality"],
                        index=2)
    df["Nacionality"]= [nacionality]
with col5:
    tuition= slt.selectbox("Tuition fees up to date",
                    options= categorical_columns["Tuition_fees_up_to_date"],
                    index=1)
    df["Tuition_fees_up_to_date"]= [tuition]
with col6:
    sh= slt.selectbox("Scholarship Holder",
                options= categorical_columns["Scholarship_holder"],
                index=1)
    df["Scholarship_holder"]= [sh]

col7, col8, col9= slt.columns(3)
with col7:
    displaced= slt.selectbox("Displaced",
                        options= categorical_columns["Displaced"],
                        index=1)
    df["Displaced"]=  [displaced]
with col8:
    db= slt.selectbox("Debtor",
                options= categorical_columns["Debtor"],
                index=0)
    df["Debtor"]= [db]
with col9:
    educational_special= slt.selectbox("Educational Special Needs",
                                options= categorical_columns["Educational_special_needs"],
                                index=0)
    df["Educational_special_needs"]= [educational_special]

slt.subheader("Informasi Akademik")
slt.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)
col1, col2, col3= slt.columns(3)
with col1:
    Previous_qualification= slt.selectbox("Previous Qualification",
                                        options= categorical_columns["Previous_qualification"],
                                        index=1)
    df["Previous_qualification"]= [Previous_qualification]
with col2:
    ao= int(slt.number_input(label='Application Order', value=1))
    df["Application_order"]= ao
with col3:
    Application_mode= slt.selectbox("Application Mode", 
                                    options= categorical_columns["Application_mode"],
                                    index=1)
    df["Application_mode"]= [Application_mode]

col4, col5, col6= slt.columns(3)
with col4:
    Inter= slt.selectbox("International", 
                        options= categorical_columns["International"],
                        index=1)
    df["International"]= [Inter]
with col5:
    course= slt.selectbox("Course",
                        options= categorical_columns["Course"],
                        index=1)
    df["Course"]= [course]
with col6:
    daytime= slt.selectbox("Daytime Evening Attendance",
                        options= categorical_columns["Daytime_evening_attendance"],
                        index=1)
    df["Daytime_evening_attendance"]= [daytime]

col7, col8= slt.columns(2)
with col7:
    pqg= float(slt.number_input(label='Previous Qualification Grade', value=3))
    df['Previous_qualification_grade'] = pqg
with col8:
    ag= float(slt.number_input(label='Admission Grade', value=3))
    df['Admission_grade']= ag

slt.subheader("Semester 1")
slt.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)
col1, col2, col3= slt.columns(3)
with col1:
    credited_1st= int(slt.number_input(label='Curricular 1st Sem Credited', value=1))
    df['Curricular_units_1st_sem_credited']= credited_1st
with col2:
    enrolled_1st= int(slt.number_input(label='Curricular 1st Sem Enrolled', value=3))
    df['Curricular_units_1st_sem_enrolled']= enrolled_1st
with col3:
    approved_1st= int(slt.number_input('Curricular 1st Sem Approved', value=3))
    df['Curricular_units_1st_sem_approved']= approved_1st

col4, col5, col6= slt.columns(3)
with col4:
    grade_1st= float(slt.number_input(label='Curricular 1st Sem Grade', value=30))
    df['Curricular_units_1st_sem_grade']= grade_1st
with col5:
    evaluations_1st= int(slt.number_input(label='Curricular 1st Sem Evaluations', value=10))
    df['Curricular_units_1st_sem_evaluations']= evaluations_1st
with col6:
    without_evaluation_1st= int(slt.number_input(label='Curricular 1st Sem Without Evaluations', value=1))
    df['Curricular_units_1st_sem_without_evaluations']= without_evaluation_1st

slt.subheader("Semester 2")
slt.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)
col1, col2, col3= slt.columns(3)
with col1:
    credited_2nd= int(slt.number_input(label='Curricular 2nd Sem Credited', value=1))
    df['Curricular_units_2nd_sem_credited']= credited_2nd
with col2:
    enrolled_2nd= int(slt.number_input(label='Curricular 2nd Sem Enrolled', value=3))
    df['Curricular_units_2nd_sem_enrolled']= enrolled_2nd
with col3:
    approved_2nd= int(slt.number_input('Curricular 2nd Sem Approved', value=3))
    df['Curricular_units_2nd_sem_approved']= approved_2nd

col4, col5, col6= slt.columns(3)
with col4:
    grade_2nd= float(slt.number_input(label='Curricular 2nd Sem Grade', value=30))
    df['Curricular_units_2nd_sem_grade']= grade_2nd
with col5:
    evaluations_2nd= int(slt.number_input(label='Curricular 2nd Sem Evaluations', value=10))
    df['Curricular_units_2nd_sem_evaluations']= evaluations_2nd
with col6:
    without_evaluation_2nd= int(slt.number_input(label='Curricular 2nd Sem Without Evaluations', value=1))
    df['Curricular_units_2nd_sem_without_evaluations']= without_evaluation_2nd

# with slt.expander("Raw Data"):
#     slt.dataframe(df, width=1000, height=50)

if  slt.button('Predict'):
    new_data = preprocessing(df)
    with slt.expander("View the Preprocessed Data"):
        slt.dataframe(data=new_data, width=800, height=10)
    slt.write("Status Siswa : {}".format(predict(new_data)))
