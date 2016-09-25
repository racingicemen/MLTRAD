import pandas_datareader.data as web

def download_data(symbol='SPY', start_date='1997-01-01', end_date='2016-08-31'):
    dframe = web.DataReader(name=symbol, data_source='yahoo', start=start_date, end=end_date)
    dframe.to_csv('data/' + str(symbol) + '.csv', index_label='Date')

if __name__ == '__main__':
    download_data('XOM')
    
