
import os
import sys
from bisect import bisect

def two_sum_exists(arr, num):
    arr.sort()
    for idx in range(len(arr)):
        insertidx = bisect(arr, num-arr[idx], lo=idx+1)
        if arr[insertidx-1] == num-arr[idx]:
            # print(num, idx, insertidx)
            return True
    return False

def FNAME1(arr, preamble):    
    idx = preamble
    while two_sum_exists(arr[idx-preamble:idx], arr[idx]):
        idx = idx + 1
    return arr[idx]

def target_sum(arr, target):
    dp = [[0]*len(arr) for _ in range(len(arr))]
    for i in range(len(arr)): dp[i][i] = arr[i]
    for wlen in range(1, len(arr)):
        for i in range(0, len(arr) - wlen):
            dp[i][i + wlen] = dp[i][i + wlen - 1] + dp[i + wlen][i + wlen]
            if dp[i][i + wlen] == target: return i, i+wlen
    return -1, -1
'''
1 3 6 10
0 2 5 9
0 0 3 7
0 0 0 4
'''

def FNAME2(arr, preamble):  
    target = FNAME1(arr, preamble)  
    start, end = target_sum(arr, target)
    return min(arr[start:end+1]) + max(arr[start:end+1])

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = [int(line[:-1]) for line in f.readlines()]
    return arr

def test_day9(outfile):

    test_arr = preprocess("test_input")
    arr = preprocess("input")

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 9 Results:" + codeblock)

    assert FNAME1(test_arr, 5) == 127
    print("P1:\t" + str(FNAME1(arr, 25)))

    assert FNAME2(test_arr, 5) == 62
    print("P2:\t" + str(FNAME2(arr, 25)) + codeblock)

if __name__ == "__main__":
    test_day9(None)