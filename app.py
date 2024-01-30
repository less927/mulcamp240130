#-*- coding:utf-8 -*-


import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
st.header('dashboard practice', divider='blue')
st.header('대쉬보드 실습  🌭')

with st.sidebar:
    "menu",
      

@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df

def main():
    st.title("Hello World on Streamlit.io")
    iris = load_data()
    st.table(iris)
    
    df = sns.load_dataset("iris")
    sns.distplot(df['sepal_length'])
    sns.distplot(df['sepal_length'])
    
    fig, ax = plt.subplots(ncols=2)

    sns.distplot(df['sepal_length'], ax=ax[0])
    sns.distplot(df['sepal_width'], ax=ax[1])
    sns.distplot(df['sepal_length'], ax=ax[0])
    sns.distplot(df['sepal_width'], ax=ax[1])
    fig, ax = plt.subplots(ncols=2, nrows=2)

    sns.distplot(df['sepal_length'], ax=ax[0,0])
    sns.distplot(df['sepal_width'], ax=ax[0,1])
    sns.distplot(df['petal_length'], ax=ax[1,0])
    sns.distplot(df['petal_width'], ax=ax[1,1])
    
    col_n = 2
    row_n = 2

    fig, ax = plt.subplots(ncols=col_n, nrows=row_n, figsize=(20,row_n*5))

    # 마지막 컬럼은 문자형 값을 가지기 때문에 [:-1]로 범위지정함
    for i,col in enumerate(df.columns[:-1]):
        sns.distplot(df[col], bins=20, ax=ax[int(i/col_n),int(i%col_n)])
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
          
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    main()