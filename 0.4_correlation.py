""" 
- variance measures how a single variable deviates from its mean
- covariance, the paired analogue of variance. covariance measures how two variables vary in tandem from their means """

import math

num_friends = [100, 49, 41, 40, 25]
daily_minutes = [30, 14, 10, 9, 4]

def mean(x):
    return sum(x) / len(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
    for v_i, w_i in zip(v, w))

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

covariance(num_friends, daily_minutes) # 284.75

"""  
- A “large” negative covariance means the opposite — that x tends to be small when y is large and vice versa. 
- A covariance close to zero means that no such relationship exists. 

covariance is hard to intrepret for 2 reasons:
- its input is the product of the inputs unit which is hard to make sense
- If each user had twice as many friends (but the same number of minutes), the
        covariance would be twice as large. But in a sense the variables would be just as
        interrelated. Said differently, it’s hard to say what counts as a “large” covariance.
"""

""" For this reason, it’s more common to look at the correlation, which divides out the
standard deviations of both variables: """

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero

correlation(num_friends, daily_minutes) # 0.99

""" 
- The correlation is unitless and always lies between -1 (perfect anti-correlation) and 1 (perfect correlation). 
- A number like 0.99 represents a positive correlation. """

# examine the data via viz
# if outlier are present, remove outlier for better correlation
