""" 
- Dispersion refers to measures of how spread out our data is. 
- Typically they’re statistics for which values near zero signify not spread out at all and 
    for which large values signify very spread out """

import math

num_friends = [100, 49, 41, 40, 25]

# 1. simple range
# very simple measure is the range, which is just the difference between the largest and smallest elements
def data_range(x):
    return max(x) - min(x)

data_range(num_friends) # 75

""" 
- The range is zero precisely when the max and min are equal, which can only happen if the
elements of x are all the same, which means the data is as undispersed as possible.
- Conversely, if the range is large, then the max is much larger than the min and the data is
more spread out.
- Like the median, the range doesn’t really depend on the whole data set. A data set whose
points are all either 0 or 100 has the same range as a data set whose values are 0, 100, and
lots of 50s. But it seems like the first data set “should” be more spread out.

A more complex measure of dispersion is the variance, which is computed as: """

def mean(x):
    return sum(x)/len(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
    for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

# 2. Variance
def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

variance(num_friends) # 825.5

""" 
- Now, whatever units our data is in (e.g., “friends”), all of our measures of central tendency
are in that same unit. 
- The range will similarly be in that same unit. 
- The variance, on the other hand, has units that are the square of the original units (e.g., “friends squared”). 
- As it can be hard to make sense of these, we often look instead at the standard deviation:
"""
# 3. standard deviation
def standard_deviation(x):
    return math.sqrt(variance(x))
    
standard_deviation(num_friends) # 28.7315

""" 
- Both the range and the standard deviation have the same outlier problem 
- so more robust alternative is interquartile range
- interquartile range is the difference between the 75th percentile value and the 25th percentile value"""

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

# 4. interquartile range
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

interquartile_range(num_friends) # 9
