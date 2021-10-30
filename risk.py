def risk_calc():
dependants = st.sidebar.slider('Number of dependents', 0, 3, 6)
monthly_income = st.sidebar.slider('Monthly Income (in ₹):', 0, 500000, 1000000)
page_names= ['Safety', 'Income', 'Gains']
page= st.radio('Investment Goals:', page_names)

risk = 0
if dependants==0:
 risk+=30

elif dependants==1; 
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

if page=='Safety'
 risk-=10
elif page=='Income'
 risk+=25
elif page=='Gains'
 risk+=50

if monthly_income <=20000
 risk-=40
elif monthly_income >20000 and <=40000
 risk-=20
elif monthly_income >40000 and <=80000
 risk-=5
elif monthly_income >80000 and <=120000
 risk+=5
elif monthly_income >120000 and <=180000
 risk+=7
elif monthly_income >180000 and <=250000
 risk+=10
elif monthly_income >250000 and <=350000
 risk+=20
elif monthly_income >350000 and <=450000
 risk+=30
elif monthly_income >450000 and <=550000
 risk+=40
elif monthly_income >550000 and <=650000
 risk+=50
elif monthly_income >650000 and <=750000
 risk+=60
elif monthly_income >750000 and <=850000
 risk+=70
elif monthly_income >850000 and <=100000
 risk+=80







