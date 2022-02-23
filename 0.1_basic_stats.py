# lets create a list 
num_friends = [100, 49, 41, 40, 25]

# 1. simple stats

# 1.1 len of the list
num_points = len(num_friends) # 5

# 1.2 largest value in the list
largest_value = max(num_friends) # 100

# 1.3 lowest value in the list
smallest_value = min(num_friends) # 25

# special cases of wanting to know the values in specific positions:
sorted_values = sorted(num_friends) # [25, 40, 41, 49, 100]

smallest_value = sorted_values[0] # 25

second_smallest_value = sorted_values[1] # 40

second_largest_value = sorted_values[-2] # 49

