
import os
import sys
from collections import Counter

def FNAME1(arr): 
    deltas = Counter([arr[idx] - arr[idx-1] for idx in range(1, len(arr))])
    return deltas[1] * deltas[3]



def FNAME2(arr):   
    adapters = set(arr)
    numways = {0: 1}

    def _recursive(target):
        if target in numways: return numways[target]
        ways = 0
        for delta in range(1, 4):
            if target - delta in adapters:
                ways = ways + _recursive(target - delta)
        numways[target] = ways
        return numways[target]
    return _recursive(arr[-1])

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = [int(line[:-1]) for line in f.readlines()]
    arr.sort()
    arr = [0] + arr + [arr[-1] + 3]    
    return arr

def test_day10(outfile):

    test_arr1 = preprocess("test_input1")
    test_arr2 = preprocess("test_input2")
    arr = preprocess("input")

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 10 Results:" + codeblock)

    assert FNAME1(test_arr1) == 35
    assert FNAME1(test_arr2) == 220
    print("P1:\t" + str(FNAME1(arr)))

    assert FNAME2(test_arr1) == 8
    assert FNAME2(test_arr2) == 19208
    print("P2:\t" + str(FNAME2(arr)) + codeblock)

if __name__ == "__main__":
    test_day10(None)