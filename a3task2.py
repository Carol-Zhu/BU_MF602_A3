# author: Xujiahui Zhu 
# 2023/06/29
# A3-task2 

from a3task1 import *

# function 1
""" Write a function calc_returns(prices).
    This function will process a list of stock prices and calculate the periodic returns.
"""
def calc_returns(prices):
  ret_list = []

  for index in range(len(prices))[1:]:
    ret = prices[index] / prices[index - 1] -1 # calculate return by the function 
    ret_list.append(ret) # append the return in the list and calculate next with the for loop 

  return ret_list

# function 2
""" Write a function process_stock_prices_csv(filename).
    This function will process a data file containing stock price data, and return a list of stock prices.
"""
def process_stock_prices_csv(filename):
  data = []
  prices = []
  with open(filename) as f:
      for line in f:
        data.append(line)

  for lin in data[1:]:
    adj_price = float(lin.split(',')[-2]) # we append the adjusted price into our dataset and we need the price with two digits after the point 
    prices.append(adj_price)

  return prices


# function 3
""" Write a function stock_report(filenames) as a client program to process stock prices
    and display descriptive statistics about the stocks.
"""
def stock_report(filenames):
  # get the file for later processing 
  market_ret = calc_returns(process_stock_prices_csv('SPY.csv'))
  # each index need a list to store for all stocks 
  mean_list = []
  std_list = []
  cov_list = []
  corr_list = []
  rsq_list = []
  beta_list = []
  alpha_list = []

    # for loop can help us to get the data one by one 
  for file in filenames:
    prices = process_stock_prices_csv('AAPL.csv')
    returns = calc_returns(prices)

    mean_re = mean(returns)
    mean_list.append(mean_re)
    std_re = stdev(returns)
    std_list.append(std_re)

    cov_re = covariance(returns,market_ret)
    cov_list.append(cov_re)
    corr_re = correlation(returns,market_ret)
    corr_list.append(corr_re)
    rsq_re = rsq(returns,market_ret)
    rsq_list.append(rsq_re)

    beta_re = simple_regression(returns,market_ret)[1]
    beta_list.append(beta_re)
    alpha_re = simple_regression(returns,market_ret)[0]
    alpha_list.append(alpha_re)

  head_symbol = "Calculated returns for 4 stocks. \n\
  \nDescriptive statistics for daily stock returns:     \nSymbol:       %s          %s          %s         %s\
  "% (filenames[0][:-4], filenames[1][:-4], filenames[2][:-4], filenames[3][:-4])
  print(head_symbol)
  # we print all required numbers from the fomula we have in task 1
  mean_line = f"Mean:  {mean_list[0]:12.5f}" + f"{mean_list[1]:12.5f}" + f"{mean_list[2]:12.5f}" + f"{mean_list[3]:12.5f}"

  print(mean_line)

  std_line = f"StDev: {std_list[0]:12.5f}" + f"{std_list[1]:12.5f}" + f"{std_list[2]:12.5f}" + f"{std_list[3]:12.5f}"
  print(std_line)

  cov_line = f"Covar: {cov_list[0]:12.5f}" + f"{cov_list[1]:12.5f}" + f"{cov_list[2]:12.5f}" + f"{cov_list[3]:12.5f}"
  print(cov_line)

  corr_line = f"Correl:{corr_list[0]:12.5f}" + f"{corr_list[1]:12.5f}" + f"{corr_list[2]:12.5f}" + f"{corr_list[3]:12.5f}"
  print(corr_line)

  rsq_line = f"R-SQ:  {rsq_list[0]:12.5f}" + f"{rsq_list[1]:12.5f}" + f"{rsq_list[2]:12.5f}" + f"{rsq_list[3]:12.5f}"
  print(rsq_line)

  beta_line = f"Beta:  {beta_list[0]:12.5f}" + f"{beta_list[1]:12.5f}" + f"{beta_list[2]:12.5f}" + f"{beta_list[3]:12.5f}"
  print(beta_line)

  alpha_line = f"Alpha: {alpha_list[0]:12.5f}" + f"{alpha_list[1]:12.5f}" + f"{alpha_list[2]:12.5f}" + f"{alpha_list[3]:12.5f}"
  print(alpha_line)

  # ret_string = head_symbol + mean_line + std_list
  # print(ret_string)
  return True
  

if __name__ == '__main__':
  # test the functions 
  prices = [100,110,105,112,115]
  print("prices is", prices)
  print("calc_returns(prices) returned", calc_returns(prices))

  # function 2
  filename = './AAPL.csv'
  prices = process_stock_prices_csv(filename)

  # function 3 
  filenames = ['AAPL.csv', 'HD.csv', 'PM.csv', 'SPY.csv']
  # note, this function will return a string
  stock_report(filenames)
