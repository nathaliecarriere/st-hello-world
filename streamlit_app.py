from datetime import timedelta
from pathlib import Path
from time import sleep
import snowflake.connector
import os


import numpy as np
import pandas as pd
import plotly_express as px
import streamlit as st
from feature_engineering import preprocess_data


@st.cache_data()
#def load_data():
 #  bikes_data_path = Path() / 'bike_sharing_demand_train.csv'
#   data = pd.read_csv(bikes_data_path)
#   return data

#df = load_data()
#df_preprocessed = preprocess_data(df.copy())
#mean_counts_by_hour = pd.DataFrame(df_preprocessed.groupby(['hour', 'season'], sort=True)['count'].mean()).reset_index()
#fig1 = px.bar(mean_counts_by_hour, x='hour', y='count', color='season', height=400)
#barplot_chart = st.write(fig1)

def load_data():
    orders_path=Path() / 'order.csv'
    data2=pd.read_csv(orders_path)
    return data2

df2=load_data()

fig2=px.bar(df2.copy(),x='DATE',y='PRICE',color='CUSTOMER',height=400)
#barplot_chart=st.write(fig2)


def load_data():
    conn = snowflake.connector.connect(
                user='NCARRIERE',
                password='Drigas48!s',
                account='qq37004.west-europe.azure',
                warehouse='TEST_WH',
                database='ORDERS',
                schema='PUBLIC',
                insecure_mode=True
                )
    #data3=pd.read_sql_query("select DATE as DATE, PRICE as CA, CUSTOMER as CUSTOMER from ORDERS", conn)
    data3=pd.read_sql_query("select DATE as DATE, sum(PRICE) as CA, CUSTOMER as CUSTOMER from ORDERS group by DATE,CUSTOMER order by DATE ASC", conn)
    #data3=pd.read_sql_table('ORDERS', conn)
    return data3

df3=load_data()
fig3=px.bar(df3.copy(),x='DATE',y='CA',color='CUSTOMER',height=400)


#df3 = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
#df3.loc[df3['CUSTOMER'] < 2.e6, 'CA'] = 'Other countries' # Represent only large countries
#fig4 = px.pie(df3, values='CA', names='CUSTOMER', title='CA par client')
#fig4.show()

#df4 = px.data.tips()
def load_data():
    conn = snowflake.connector.connect(
                user='NCARRIERE',
                password='Drigas48!s',
                account='qq37004.west-europe.azure',
                warehouse='TEST_WH',
                database='ORDERS',
                schema='PUBLIC',
                insecure_mode=True
                )
    data4=pd.read_sql_query("select CUSTOMER, sum(PRICE)as total_price from ORDERS.PUBLIC.ORDERS group by CUSTOMER", conn)
    #data3=pd.read_sql_table('ORDERS', conn)
    return data4

df4=load_data()
fig4 = px.pie(df4, values='TOTAL_PRICE', names='CUSTOMER')

barplot_chart=st.write(fig4)

barplot_chart=st.write(fig3)

