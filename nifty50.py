import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta
import pandas_datareader.data as pdr
from sklearn.metrics import (
    mean_squared_error as mse,
    mean_absolute_error as mae,
    mean_absolute_percentage_error as mape
)
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
yf.pdr_override()


nifty_50 = ['ADANIENT.NS','ADANIPORTS.NS', 'APOLLOHOSP.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BRITANNIA.NS',
           'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SUNPHARMA.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS']

nifty_info = pd.read_csv('nifty50_info.csv')
st.sidebar.title("Nifty 50 Stocks")
stock = st.sidebar.selectbox("Select a stock", nifty_50, 4)
st.subheader('Stock price predictor')

def get_workingdays(start, end, excluded=(6, 7)):
    days = []
    while start <= end:
        if start.isoweekday() not in excluded:
            # days.append(start.strftime('%d-%m-%Y'))
            days.append(start.strftime('%b-%d, %Y'))

        start += timedelta(days=1)
    return days

def performance(actual, predicted):
    _mae = round(mae(actual, predicted))
    _rmse = round(mse(actual, predicted)**0.5, 3)
    _mape = round(mape(actual, predicted), 3)
    return {'MAE': _mae, 'RMSE': _rmse, 'MAPE': _mape}

start_date = date.today() + timedelta(1)
end_date = date.today() + timedelta(15)
future_working_days = get_workingdays(start_date,end_date)[:10]

if stock:

    ## reading names from df
    stockname = nifty_info.loc[nifty_info.ticker == f'{stock}']['shortName'].to_list()[0]
    logo_url = nifty_info.loc[nifty_info.ticker == f'{stock}']['logo_url'].to_list()[0]

    ## show company logo
    st.image(logo_url)
    st.text(f"{stockname}: 1-year stock price")

    ## Getting data from yfinance
    stock_data = yf.Ticker(stock)

    ## parse 1yr data
    stock_price = stock_data.history(period="1y")
    stock_price.reset_index(inplace=True)


    ## plot stock price
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


    st.subheader('Returns:')
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
    st.write("#"); st.write("#") ## createing extra space for separation

    # stockDetail = pd.DataFrame(columns=['Day', 'Price', 'Pct change'])
    # stockDetail.loc['Current day'] = [today,current_price , 0]
    # stockDetail.loc['1 week'] = [stock_price.Date.iloc[-6],
    #                              stock_price['Close'].iloc[-6], one_week_change]
    # stockDetail.loc['1 month'] = [stock_price.Date.iloc[-21],
    #                              stock_price['Close'].iloc[-21], one_month_change]
    # stockDetail.loc['3 month'] = [stock_price.Date.iloc[-63],
    #                              stock_price['Close'].iloc[-63], three_month_change]
    # st.dataframe(stockDetail)


    ## Forecasting with TES
    st.subheader('5 days Forecasting using Triple Exponential smoothing')
    # Training
    model = ExponentialSmoothing(stock_price['Close'], trend='add', seasonal='multiplicative', seasonal_periods=12)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)

    ## Plot forecast
    fig = go.Figure()
    fig.add_trace(go.Scatter( x=stock_price['Date'].tail(7), y=stock_price['Close'].tail(7), name='Actual',
                             line=dict(color='royalblue', width=3)))
    fig.add_trace(go.Scatter(x=future_working_days, y=forecast.values.tolist(), name='Forecast',
                             line=dict(color='firebrick', width=3)))
    st.plotly_chart(fig)

    ## Backtest results
    train_x = stock_price["Close"].loc[stock_price.index < stock_price.index[-5]].copy()
    test_x = stock_price["Close"].loc[stock_price.index >= stock_price.index[-5]].copy()
    tes = ExponentialSmoothing(train_x, trend='add', seasonal='multiplicative', seasonal_periods=12)
    tes_fit = tes.fit()

    test_pred = tes_fit.forecast(steps=5)
    backtest_df = pd.DataFrame({'Day': stock_price['Date'].tail(5), 'Actual price':test_x, 'Predicted price':test_pred}).set_index('Day')
    st.markdown('##### Backtest results:')
    st.dataframe(backtest_df)
    st.markdown('##### Performace metrics:')
    st.text(performance(test_x.values.tolist(), test_pred.values.tolist()))
    st.write("#"); st.write("#") ## createing extra space for separation


    ## Forecasting with Prophet
    st.subheader('90 days Forecasting using Fb-Prophet')
    df = stock_price[['Date', 'Close']]
    df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
    # Define the model and fit it to the data
    model = Prophet()
    model.fit(df)

    # Generate future predictions
    future = model.make_future_dataframe(periods=100)
    forecast = model.predict(future)

    # Plot the forecast
    figProphet = plot_plotly(model, forecast)
    st.plotly_chart(figProphet)

