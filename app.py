import pickle
import numpy as np
import streamlit as st

st.title('Customer churn V2')
st.text('by Anirudh')

model = st.selectbox('choose a model',
	('Decision tree classification', 'Random forest classification'))

if model =='Decision tree classification':
	m = pickle.load(open('decisiontree_sm.sav', 'rb'))
else:
	m = pickle.load(open('randomforest_sm.sav', 'rb'))

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
  st.title('Enter the details')

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