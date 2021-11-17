import streamlit as st
import pandas as pd
from sklearn import datasets, linear_model
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import os
import csv
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from scipy.optimize import minimize

import requests
import sys



st.subheader('Prediction')

def risk_calc():
 st.subheader("To calculate risk tolerance for an optimum portfolio, choose from the options and adjust the values on the sliderbar to the values that seem closest to your profile")
 
 #(""" range(1,6)
 #dependants = st.select_slider("Number of dependents: ", options = my_range, value = 10)
 #st.write("You chose: %s ", %dependants)
 #myy_range = range(0,1000000)
 #monthly_income = st.select_slider("Monthly Income: ", options = myy_range, value = 10)
  # st.write("You chose: %s ", %monthly_income) """)
 page_names= ['Safety', 'Income', 'Gains']
 page= st.sidebar.radio('Investment Goals:', page_names)
 dependants = st.sidebar.slider('Number of dependents', 0, 3, 6)
 monthly_income = st.sidebar.slider('Monthly Income (in ₹):', 0, 300000, 500000)
 

 risk = 0
 if dependants==0:
  risk+=30

 elif dependants==1:
  risk-=5

 elif dependants==2:
  risk-=10

 elif dependants==3:
  risk-=15

 elif dependants==4:
  risk-=20

 elif dependants==5:
  risk-=25

 elif dependants==6:
  risk-=30

 if page=='Safety':
  risk-=10
 elif page=='Income':
  risk+=25
 elif page=='Gains':
  risk+=50

 if monthly_income <=20000:
  risk-=40
 elif monthly_income >20000 and monthly_income <= 40000:
  risk-=20
 elif monthly_income >40000 and monthly_income <=80000:
  risk-=5
 elif monthly_income >80000 and monthly_income <=120000:
  risk+=5
 elif monthly_income >120000 and monthly_income <=180000:
  risk+=7
 elif monthly_income >180000 and monthly_income <=250000:
  risk+=10
 elif monthly_income >250000 and monthly_income <=350000:
  risk+=20
 elif monthly_income >350000 and monthly_income <=450000:
  risk+=30
 elif monthly_income >450000 and monthly_income <=550000:
  risk+=40
 elif monthly_income >550000 and monthly_income <=650000:
  risk+=50
 elif monthly_income >650000 and monthly_income <=750000:
  risk+=60
 elif monthly_income >750000 and monthly_income <=850000:
  risk+=70
 elif monthly_income >850000 and monthly_income <=100000:
  risk+=80
 return risk

ab =risk_calc()

if ab <0:
    st.sidebar.write('Your Risk Tolerance is:')
    st.sidebar.write(ab)
    st.sidebar.warning('Your Risk Tolerance is very low.')
else:
        st.sidebar.write('Your Risk Tolerance is:')
        st.sidebar.write(ab)


st.sidebar.header('User Input Parameters')

def user_input_features():
    #age = st.sidebar.slider('Age', 18, 50, 100)
    #risk_tol= range(0, 100)
    #number = st.select_slider("Risk Tolerance: ", options = risk_tol, value = 10)
    old = st.sidebar.slider('Risk Tolerance', 0, 50, 120)
    OldMin = -80
    OldMax = 120
    NewMax = 13
    NewMin=0
    def new(OldValue):
        NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
        return NewValue
    a= new(old)
    print(a)
    #years_to_invest = st.sidebar.slider('Number of years you want to invest', 1, 10, 25)
    #money_invest = st.sidebar.slider('Amount to Invest (in ₹)', 1000.0, 50000.0, 100000.0)
    data = {#'Age': age,
            'Risk Tolerance': a,
            #'Number of investing years': years_to_invest,
            #'Amount to Invest (in ₹)': money_invest
            }
    features = pd.DataFrame(data, index=[0])
    return features
   
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)



excel = pd.ExcelFile("roboDataset.xlsx", engine='openpyxl')
prediction_percentages = [2.307, 4.803, 8.99, 0.611, 4.279, 0.436, 2.270, 0.611, 14.323, 19.126]
predictions = []

for i in range(1, 2):
    dataset = pd.DataFrame(pd.read_excel(excel, ('Sheet' + str(i))))
    dataset_x = dataset['x'].values.reshape(-1,1)
    dataset_y = dataset['y']
    model = LinearRegression()
    model.fit(dataset_x, dataset_y)
    prediction = model.predict([[df['Risk Tolerance'].get(0)]])
    #print(prediction)
    predictions.append(prediction)
    



import numpy as np

returns = pd.read_csv('Assets.xls')
#returns = pd.read_excel('roboDataset.xlsx')

# the objective function is to minimize the portfolio risk
def objective(weights): 
    weights = np.array(weights)
    return weights.dot(returns.cov()).dot(weights.T)
# The constraints
cons = (# The weights must sum up to one.
        {"type":"eq", "fun": lambda x: np.sum(x)-1}, 
        # This constraints says that the inequalities (ineq) must be non-negative.
        # The expected daily return of our portfolio and we want to be at greater than 0.002352
        {"type": "ineq", "fun": lambda x: np.sum(returns.mean()*x)-(predictions[0])})
# Every stock can get any weight from 0 to 1
bounds = tuple((0,1) for x in range(returns.shape[1]))
# Initialize the weights with an even split
# In out case each stock will have 10% at the beginning
guess = [1./returns.shape[1] for x in range(returns.shape[1])]
optimized_results = minimize(objective, guess, method = "SLSQP", bounds=bounds, constraints=cons)


#optimized_results.x






returns = pd.read_csv('Assets.xls')
symbols = ['Stocks', 'Derivatives', 'Commodities',
           'Currencies', 'Mutual Funds', 'Loans',
           'Insurance',  'SIP', 'REIT', 'Gold'  ]

final = pd.DataFrame(list(zip(symbols, optimized_results.x)), 
                       columns=['Symbol', 'Weight'])
final

st.line_chart(final.rename(columns={'Symbol':'index'}).set_index('index'),width = 900,height=500)

#ax = final.plot.bar(x='Symbol', y='Weight', rot=0)

df = final
 
name = df['Symbol']
price = df['Weight']
 
# Figure Size
fig = plt.figure(figsize =(14, 10))
 
# Horizontal Bar Plot


# /Users/ananya/Documents/python/aajx1.csv
