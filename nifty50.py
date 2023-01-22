import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pandas_datareader.data as pdr
yf.pdr_override()


nifty_50 = ['ADANIPORTS.NS', 'ADANIENT.NS', 'APOLLOHOSP.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BRITANNIA.NS', 
           'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SUNPHARMA.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS']

st.sidebar.title("Nifty 50 Stocks")
stock = st.sidebar.selectbox("Select a stock", nifty_50)


if stock:
    ## show logo
    stock_data = yf.Ticker(stock)
    imgUrl = stock_data.get_info()['logo_url']
    st.image(imgUrl)
    st.text(f"1-year stock price of {stock_data.get_info()['shortName']} ")

    ## parse 1yr data
    stock_price = stock_data.history(period="1y")
    stock_price.reset_index(inplace=True)


    ## show stock price plot
    fig = px.line(stock_price, x='Date', y='Close')
    fig.update_xaxes(
        # rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=3, label="3m", step="month", stepmode="backward"),
                # dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                # dict(step="all")
            ])
        )
    )
    st.plotly_chart(fig)


    ## date formatting
    stock_price['Date'] = pd.to_datetime(stock_price['Date'])
    stock_price['Date'] = stock_price['Date'].dt.strftime('%b-%d, %Y')  ## Jan-20, 2023
    
    ## show current price, 1 week, 1month, 3month, 1 year percentage change
    today = stock_price.Date.iloc[-1]
    current_price = stock_price['Close'].iloc[-1]
    one_week_change = ((current_price / stock_price['Close'].iloc[-6] - 1 )*100 ).round(2)
    one_month_change = ((current_price / stock_price['Close'].iloc[-21] -1 )*100 ).round(2)
    three_month_change = ((current_price / stock_price['Close'].iloc[-63] -1 )*100 ).round(2)
    one_year_change = ((current_price / stock_price['Close'].iloc[0] -1 )*100 ).round(2)

    stockDetail = pd.DataFrame(columns=['Current price', '1 week return', '1 month return', '3 months return', '1 year return'])
    stockDetail.loc[today] = [current_price.round(2), str(one_week_change)+" %", str(one_month_change)+" %", str(three_month_change)+" %", str(one_year_change)+" %" ]
    st.dataframe(stockDetail)


    # stockDetail = pd.DataFrame(columns=['Day', 'Price', 'Pct change'])
    # stockDetail.loc['Current day'] = [today,current_price , 0]
    # stockDetail.loc['1 week'] = [stock_price.Date.iloc[-6],
    #                              stock_price['Close'].iloc[-6], one_week_change]
    # stockDetail.loc['1 month'] = [stock_price.Date.iloc[-21],
    #                              stock_price['Close'].iloc[-21], one_month_change]
    # stockDetail.loc['3 month'] = [stock_price.Date.iloc[-63],
    #                              stock_price['Close'].iloc[-63], three_month_change]
    # st.dataframe(stockDetail)




    

    
    








