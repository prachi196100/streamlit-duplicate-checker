#
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Creating the title and the subheader
st.title("My First Made Data Analysis Using Streamlit ")
st.subheader("Happy Me Let'sss See")

#Now if we want to ask user about asking the dataset 
upload=st.file_uploader("Upload Your Dataset (IN CSV FORMAT ONLY)")
if upload is not None:
    df=pd.read_csv(upload)
else:
    print("Alreay Uploaded")  

#Now we are creating a button that will show like preview the data like it will show either head or tail only will data is uploaded
if upload is not None:
    if st.checkbox("Preview Dataset"):
       if st.button("Head"):
           st.write(df.head())
       if st.button("Tail"):
           st.write(df.tail()) 

#Checking the Data type of each column
if upload is not None:
        if st.checkbox("Datatype of Dataset"):
            st.text("DATA TYPES")
            st.write(df.dtypes)
         

#Finding the shape of the data ,whaterver user selects (Rows or coloumns)
if upload is not None:
    #Syntax: st.radio("Text je radio button pela joiye",('OPTION1','OPTION2',..))
    data_shape=st.radio("WHAT DIMENSION DO YOU WANT TO CHECK ?", ('ROWS' ,'COLUMNS'))

    if data_shape=='ROWS':
        st.text("Number of Rows")
        st.write(df.shape[0])
        
    if data_shape=='COLUMNS':
        st.text("Number of Columns")
        st.write(df.shape[1])



#Checking the null values 
if upload is not None:
    test=df.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataSet"):
          sns.heatmap(df.isnull())
          st.pyplot()
else:
    st.success("No misssing values")


#Checking duplicates values in the dataset
if upload is not None:
     test=df.duplicated().any()
     if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do you Want to Remove Duplicate values",("Select One","Yes","No"))
        if dup=='Yes':
             df= df.drop_duplicates()
             st.text("Duplicate Values Are Removed")
        if dup=='No':
             st.text("No problem!!!")


#Get the overall statistics 
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(df.describe(include='all'))
    
#About Section
if st.button("About App"):
    st.text("Build With Streamlit")
    st.text("Thanks to Streamlit")

#By
if st.checkbox("By"):
    st.success("Prachi Patel")