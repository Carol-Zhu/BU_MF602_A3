# author: Xujaihui Zhu 
# 2023/06/29 
# A3-task1

# function 1
""" Write the function mean(values), that takes as a parameter a list of numbers,
and calculates and returns the mean of those values.
"""

def mean(values):
  count = 0 # initiate count to accumulate the value from val 

  for val in values:
      count += val

  mean = count / len(values) # mean is the average of all numbers 

  return mean


# function 2
""" Write the function variance(values), that takes as a parameter a list of numbers,
and calculates and returns the population variance of the values in that list.
"""

def variance(values):
  count = 0 # Still, we need a counter to accumulate values 
  mn = mean(values)

  for val in values:
    count += (val - mn) ** 2 # directly use the function provided from the document 

  var = count / len(values)

  return var





# function 3
""" Write the function stdev(values), that takes as a parameter a list of numbers,
and calculates and returns the population standard deviation of the values in that list.
"""

def stdev(values):
  return variance(values) ** 0.5 # return the function provided in the ducument 


# function 4
""" Write the function covariance(x,y) that takes as parameters two lists of values,
and calculates and returns the population covariance for those two lists.
"""
def covariance(x,y):
  count = 0 # still, the counter matters for us to accumulate the numbers as we add the value in a loop 
  mn_x = mean(x)
  mn_y = mean(y)

  for ind in range(len(x)):
    count += (x[ind] - mn_x) * (y[ind] - mn_y) # plug in the function provided in the ducument 

  cov = count / len(x)

  return cov



# function 5
""" Write the function correlation(x,y) that takes as parameters two lists of values,
and calculates and returns the correlation coefficient between these data series.
"""
def correlation(x,y):
  return covariance(x,y) / (stdev(x) * stdev(y)) # plug the covariance function and devide by the std deviation separatly 


# function 6
""" Write the function rsq(x,y) that takes as parameters two lists of values,
    and calculates and returns the square of the correlation between those two data series,
    which is a measure of the goodness of fit measure to explain variation in y as a function of variation of x.
"""
def rsq(x,y):
  return correlation(x,y) ** 2 # rsq is important to judge the correctness of two lists of numbers 


# function 7
""" Write the function simple_regression(x,y) that takes as parameters two lists of values,
and calculates and returns the regression coefficients between these data series.
The function should return a list containing two values: the intercept and regression coefficients, α and β.
"""
def simple_regression(x,y):
  beta = covariance(x,y) / variance(x) # bate is the sensitivity of a stock with regard to the market which is the S&P500
  alpha = mean(y) - beta * mean(x)

  return (alpha, beta)



if __name__ == '__main__':
    # test the functions 
    x = [4,4,3,6,7]
    print("x =", x) 
    print("mean(x) returned", mean(x))

    print("variance(x) returned", variance(x))
    print("stdev(x) retruned", stdev(x))
  
    y = [6,7,5,10,12] 
    print("y =", y)
    print("covariance(x,y) returned", covariance(x,y))
    print("correlation(x,y) returned", correlation(x,y))
    print("rsq(x,y) returned", rsq(x,y))
    print("simple_regression(x,y) returned", simple_regression(x,y))
    



