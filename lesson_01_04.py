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
    dates = pd.date_range('2012-01-01', '2012-12-31')

    # Choose stock symbols to read
    symbols = ['SPY']

    # Get stock data
    df = get_data(symbols, dates)

    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    # Compute rolling mean using a 20-day window
    rm_SPY = pd.rolling_mean(df['SPY'], window=20)

    # Add rolling mean to the same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

    # plot_data(df)
    #
    # # Compute global statistics for each stock
    # print df.mean()

if __name__ == "__main__":
    test_run()
