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
###  Robo-Advisor is an application that uses characterisics of an investor to create custom portfolios of specific securities
""")


st.write(" ## What is Risk Tolerance? ")
st.write(" ### To put simply, risk tolerance is the level of risk an investor is willing to take. But being able to accurately gauge your appetite for risk can be tricky. Risk can mean opportunity, excitement or a shot at big gains—a 'you have to be in it to win it' mindset. But risk is also about tolerating the potential for losses, the ability to withstand market swings and the inability to predict what’s ahead.")

st.write("## How much risk can you afford? ")
st.write("### When determining your risk tolerance, it's also important to understand your goals so you don't make a costly mistake. Your time horizon, or when you plan to withdraw the money you've invested, can greatly influence your approach to risk.")

st.write("### Your time horizon depends on what you are saving for, when you expect to begin withdrawing the money and how long you need that money to last. Goals like saving for college or retirement have longer time horizons than saving for a vacation or a down payment on a house. In general, the longer your time horizon, the more risk you can assume because you have more time to recover from a loss. As you near your goal, you may want to reduce your risk and focus more on preserving what you have—rather than risking major losses at the worst possible time.")

st.write("### One way to fine-tune your strategy is by dividing your investments into buckets, each with a separate goal. For example, a bucket created strictly for growth and income can be invested more aggressively than one that is set aside as an emergency fund.")

st.write("## What is your Investment Goal?")
st.write("### The options for investing your savings are continually increasing, but every one of them can still be categorized according to three fundamental characteristics: safety, income, and gains.")
st.write("### Safety: It is said that there is no such thing as a completely safe and secure investment. But you can get pretty close.Safety comes at a price. The returns are very modest compared to the potential returns of riskier investments. This is called opportunity risk. Those who choose the safest investments may be giving up big gains.There also is, to some extent, interest rate risk.")
st.write("### Income: Investors who focus on income may buy some of the same fixed-income assets. But their priorities shift towards income. They're looking for assets that guarantee a steady income supplement. And to get there they may accept a bit more risk.This is often the priority of retirees who want to generate a stable source of monthly income while keeping up with inflation.")
st.write("### Gains: By definition, capital growth is achieved only by selling an asset. Stocks are capital assets. Barring dividend payments, their owners have to cash them in to realize gains.There are many other types of capital growth assets, from diamonds to real estate.The stock markets offer some of the most speculative investments available since their returns are unpredictable and riskier.")
import webbrowser

url = 'http://192.168.0.104:8502'

if st.button('Create your Portfolio now!!'):
    webbrowser.open_new_tab(url)
