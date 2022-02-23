""" Central Tendency is some notion of where our data is centered """

from collections import Counter

num_friends = [100, 49, 41, 40, 25]

# 1. mean 
def mean(x):
    return sum(x)/len(x)

mean([1,2,3,4]) # 2.5

# mean is prone to outlier

# 2. median
def median(x):
    n = len(x)
    sorted_v = sorted(x)
    midpoint = n // 2
    print(f"midpoint: {midpoint}")

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

median(num_friends)
""" 
midpoint: 2
41 """

# median is not prone to outlier.
# median represents the value less than which 50% of the data lies

# A generalization of the median is the quantile, which represents the value less than which
# a certain percentile of the data lies

# 3. quantile
def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10) # 25
quantile(num_friends, 0.25) # 40
quantile(num_friends, 0.75) # 49
quantile(num_friends, 0.90) # 100

# 4. mode
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    print(f"counts: {counts}")
    max_count = max(counts.values())
    print(f"max_count: {max_count}")
    return [x_i for x_i, count in counts.items() if count == max_count]
    
num_friends = [41, 100, 49, 41, 40, 25, 25]
mode(num_friends) # [41, 25]



