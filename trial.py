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




st.write("""
# Asset Allocation Web App
### Automated Robo-Advisor that uses characterisics of an investor to create custom portfolios of specific securities
""")

st.subheader('Prediction')




st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.slider('Age', 18, 50, 100)
    risk_tol = st.sidebar.slider('Risk Tolerance', 0.0, 15.0, 30.0)
    years_to_invest = st.sidebar.slider('Number of years you want to invest', 1, 10, 25)
    money_invest = st.sidebar.slider('Amount to Invest (in ₹)', 1000.0, 50000.0, 100000.0)
    data = {'Age': age,
            'Risk Tolerance': risk_tol,
            'Number of investing years': years_to_invest,
            'Amount to Invest (in ₹)': money_invest}
    features = pd.DataFrame(data, index=[0])
    return features
   
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

st.write(" ## What is Risk Tolerance? ")
st.write(" ### To put simply, risk tolerance is the level of risk an investor is willing to take. But being able to accurately gauge your appetite for risk can be tricky. Risk can mean opportunity, excitement or a shot at big gains—a 'you have to be in it to win it' mindset. But risk is also about tolerating the potential for losses, the ability to withstand market swings and the inability to predict what’s ahead.")

st.write("## How much risk can you afford? ")
st.write("### When determining your risk tolerance, it's also important to understand your goals so you don't make a costly mistake. Your time horizon, or when you plan to withdraw the money you've invested, can greatly influence your approach to risk.")

st.write("### Your time horizon depends on what you are saving for, when you expect to begin withdrawing the money and how long you need that money to last. Goals like saving for college or retirement have longer time horizons than saving for a vacation or a down payment on a house. In general, the longer your time horizon, the more risk you can assume because you have more time to recover from a loss. As you near your goal, you may want to reduce your risk and focus more on preserving what you have—rather than risking major losses at the worst possible time.")

st.write("### One way to fine-tune your strategy is by dividing your investments into buckets, each with a separate goal. For example, a bucket created strictly for growth and income can be invested more aggressively than one that is set aside as an emergency fund.")





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

st.line_chart(final.rename(columns={'Symbol':'index'}).set_index('index'))

#ax = final.plot.bar(x='Symbol', y='Weight', rot=0)

df = final
 
name = df['Symbol']
price = df['Weight']
 
# Figure Size
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot


# /Users/ananya/Documents/python/aajx1.csv

