''' Build a dataframe in pandas'''
import pandas as pd
import matplotlib.pyplot as plt

def get_data(symbols, dates):
    # Create an empty DataFrame
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date",
                              parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])

    return df

def plot_data(df, title="Stock Prices"):
    '''Plot stock prices'''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def test_run():
    # Define date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['SPY', 'GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    # print df.ix['2010-01-01':'2010-01-31']
    #
    # print df['GOOG']
    # print df[['IBM', 'GLD']]
    # print df.ix['2010-03-10':'2010-03-15', ['SPY', 'IBM']]
    df = df/df.ix[0]
    plot_data(df)

if __name__ == "__main__":
    test_run()
