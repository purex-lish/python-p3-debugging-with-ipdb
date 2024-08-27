#!/usr/bin/env python3

import ipdb

def plus_two(num):
    num = num + 2     # add 2 to update the num
    #ipdb.set_trace()
    return num

# Call the function 
result = plus_two(3)
print(result)  # Print the result to verify the fix