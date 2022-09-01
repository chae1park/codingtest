# HackerRank:  Minimum Absolute Difference in an Array (Easy)
# 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    
    arr = sorted(arr)
    diff = abs(arr[0] - arr[1])
    
    for i in range(1, len(arr)-1):
        temp = abs(arr[i] - arr[i+1])
        
        if diff > temp:
            diff = temp
    return diff 
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(str(result) + '\n')
    # fptr.write(str(result) + '\n')

    # fptr.close()
'''
Inupt:
10
-59 -36 -13 1 -53 -92 -2 -96 -54 75

Output:
1
'''