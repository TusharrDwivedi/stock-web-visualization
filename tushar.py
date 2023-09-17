import streamlit as st 

from datetime import date

import yfinance as yf

import pandas_datareader as data

from plotly import graph_objs as go 

from PIL import Image

from urllib.request import urlopen

import matplotlib.pyplot as plt

START = "2015-1-1"

TODAY = date.today()

st.title("WELCOME TO ")

st.title("*STOCK VISUALIZATION WEB APP*")



stocks = st.text_input('Enter Stock which you want to vizualise','SBIN.NS')

selected_stock= ( stocks)




@st.cache

def load_data(ticker):

    data = yf.download(ticker,START,TODAY)

    data.reset_index(inplace=True)

    return data



data_load_state = st.text("load data ...")

data=load_data(selected_stock)

data_load_state.text("loadind data ... done!")


st.subheader('Raw data')

st.write(data.tail())

def plot_raw_data():

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'], name = 'stock_open'))

    fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'], name = 'stock_close'))

    fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible=True)

    st.plotly_chart(fig)


    

#CHART ACCORDING TO ABOVE DATA

plot_raw_data() 

fig = plt.figure(figsize = (12,6))

plt.plot(data.Close)

st.subheader('chart for price')

st.pyplot(fig)

#CLOSING TIME CHART

st.subheader('closing price vs time chart with 100MA')

ma100 = data.Close.rolling(100).mean()

ma200 = data.Close.rolling(200).mean()

fig = plt.figure(figsize = (12,6))

plt.plot(data.Close)

st.pyplot(fig)



#DATA VISUALIZATION

st.subheader ('vizualise the price accordingly','r')

plt.plot(ma100 , 'r')

plt.plot(ma200, 'g')

plt.plot(data.Close, 'b')

st.pyplot(fig)








