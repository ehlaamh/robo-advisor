# robo-advisor
An automated Robo-advisor that takes inputs related to characteristics of an investor and uses that information to create custom portfolios of securities specific to them.
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import os
import csv
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from scipy.optimize import minimize


st.write("""
# Asset Allocation Web App
### Automated Robo-Advisor that uses characterisics of an investor to create custom portfolios of specific securities

""")

st.subheader('Prediction')

st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.slider('Age', 18, 50, 100)
    risk_tol = st.sidebar.slider('Risk Tolerance', 0.0, 50.0, 100.0)
    years_to_invest = st.sidebar.slider('Number of years you want to invest', 1, 5, 10)
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






iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)





import numpy as np

returns = pd.read_csv('Assets.csv')


# the objective function is to minimize the portfolio risk
def objective(weights): 
    weights = np.array(weights)
    return weights.dot(returns.cov()).dot(weights.T)
# The constraints
cons = (# The weights must sum up to one.
        {"type":"eq", "fun": lambda x: np.sum(x)-1}, 
        # This constraints says that the inequalities (ineq) must be non-negative.
        # The expected daily return of our portfolio and we want to be at greater than 0.002352
        {"type": "ineq", "fun": lambda x: np.sum(returns.mean()*x)-0.05})
# Every stock can get any weight from 0 to 1
bounds = tuple((0,1) for x in range(returns.shape[1]))
# Initialize the weights with an even split
# In out case each stock will have 10% at the beginning
guess = [1./returns.shape[1] for x in range(returns.shape[1])]
optimized_results = minimize(objective, guess, method = "SLSQP", bounds=bounds, constraints=cons)
optimized_results



optimized_results.x
symbols = ['U.S. Large Cap Stocks', 'U.S. Small Cap Stocks', 'Intl Dev Stocks',
           'Emerging Stocks', 'All U.S. Bonds', 'High-Yield U.S. Bonds',
           'Intl Bonds',  'Cash (T-Bill)', 'REIT', 'Gold' ]

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
plt.bar(name, price)
 
# Show Plot
plt.show()





# /Users/ananya/Documents/python/aajx1.csv

@st.cache
def load_data(nrows):
    data = pd.read_csv('aajx1.csv', nrows=nrows)
    return data
weekly_data = load_data(100)
st.subheader('Weekly Demand Data')
st.write(weekly_data)


#line chart
st.subheader("Line chart plotting High, low, open and close")
df = pd.DataFrame(weekly_data[:30], columns = ['High','Low','Open','Close'])
df.hist()
st.line_chart(df)


st.subheader("Line chart for low and high")
chart_data = pd.DataFrame(weekly_data[:40], columns=['Low', 'High'])
st.area_chart(chart_data)
st.subheader("Line chart for open and close")
chart_data = pd.DataFrame(weekly_data[:40], columns=['Open', 'Close'])
st.area_chart(chart_data)



#histogram
st.subheader("Historgram comparing open and close")
hist_data = [weekly_data['Close'],weekly_data['Open']]
group_labels = ['Close', 'Open']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
st.plotly_chart(fig, use_container_width=True)



st.markdown("<span style=“background-color:#121922”>",unsafe_allow_html=True)
