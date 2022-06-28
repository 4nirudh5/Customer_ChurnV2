import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

#creating a sidebar with different pages to navigate  
#with st.sidebar: #if you want a side bar 
selected = option_menu(
       menu_title = None ,#"Main Menu",
       options = ["Home","Model","About"],
       icons = ["house","robot","person"],
       menu_icon = "menu-button",
       default_index = 0,
       orientation = "horizontal",  #to make the menubar horizontal 
    )
    
if selected == "Home":
    #st.title('Home')
    with st.container():
        st.title('Customer churn finder for telco company!')
        st.subheader('By Anirudh :wave:')
    
    with st.container():
        st.title('What is customer churn :information_source:')
        st.write('When a customer stops doing business with the company the customer is churned.The buisness are keen in keeping the existing customer because it is far less resource consuming than aquiring a new customer. Existing customers will often have a higher volume of service consumption and can generate additional customer referrals. Customer churn can be resovled by giving a good product and services.Preventing customer churn is critically important in telecommunication sector in retail as barriers to entry switching services and provider are so low. Acquire different datasets from kaggle, IBM sample datasets, Google dataset sample etc.. ')
        st.image("https://cdn.technologyadvice.com/wp-content/uploads/2020/03/6-Ways-CRM-Stop-Customer-Churn.png")
        st.subheader('This is a sample Dataset:')
        df = pd.read_csv("telecom_churn.csv")
        st.write(df)


if selected == "Model":
    #st.title('Model')
    st.title('Customer Churn')
    st.subheader('Enter the details')
 
    model = st.selectbox('choose a model',
      ('Decision tree classification', 'Random forest classification', 'Naive Bayes Classification'))

    if model =='Decision tree classification':
       m = pickle.load(open('decisiontree_sm.sav', 'rb'))
    elif model =='Random forest classification':
       m = pickle.load(open('randomforest_sm.sav', 'rb'))
    else:
       m = pickle.load(open('naivebayes_sm.sav', 'rb'))


    def ccp(input_data):
       na = np.asarray(input_data)
       d = na.reshape(1, -1)

       prediction = m.predict(d)
       print(prediction)

       if (prediction[0] == 0):
        return 'the customer is not churned'
       else:
        return 'the customer is churned'


    def main():
       
     AccountWeeks = st.text_input('Account Weeks')
     ContractRenewal = st.text_input('Contract Renewal')
     DataPlan = st.text_input('Data Plan')
     DataUsage = st.text_input('Data Usage')
     CustServCalls = st.text_input('Customer Service Call')
     DayMins = st.text_input('Day Mins')
     DayCalls = st.text_input('Day Calls')
     MonthlyCharge = st.text_input('Monthly Charge')
     OverageFee = st.text_input('Overage Fee')
     RoamMins = st.text_input('Roam Mins')
  
     cc = ''

     if st.button('Get Results'):
       cc = ccp([AccountWeeks,ContractRenewal,DataPlan,DataUsage,CustServCalls,
                DayMins,DayCalls,MonthlyCharge,OverageFee,RoamMins])
       st.success(cc)

    if __name__ == '__main__':
      main()

if selected == "About":
    #st.title('About')
    st.title('Hi, Anirudh here :smiley:')
    st.subheader('Hope this app was useful to you :innocent:')
    st.write('I am a student as of now who is passionate about Data Science and this is my first project. This customer churn app uses three classification models namely Decision tree, Random forest and Naive Bayes from which you can select one just like the best of three when we used to play stone paper scissors. fill in all the details just as in the data set and get the output.')
    st.write('[More projects in GITHUB >](https://github.com/4nirudh5)')

