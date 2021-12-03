import os
import sys
from collections import Counter

def count_valid1(crs):    
    count = 0
    for cr in crs:
        lcounts = Counter(cr.pwd)
        if cr.letter in lcounts:
            lc = lcounts[cr.letter]
            if lc >= cr.n1 and lc <= cr.n2:
                count = count + 1
    return count


def count_valid2(crs):
    count = 0
    for cr in crs:
        lc = 0        
        if cr.n1 - 1 in range(0, len(cr.pwd)) and cr.pwd[cr.n1-1] == cr.letter: lc = lc + 1
        if cr.n2 - 1 in range(0, len(cr.pwd)) and cr.pwd[cr.n2-1] == cr.letter: lc = lc + 1
        # print(cr, lc)
        if lc == 1: count = count + 1
    return count

class Criteria:
    def __init__(self, n1, n2, letter, pwd):
        self.n1 = int(n1)
        self.n2 = int(n2)
        self.letter = letter
        self.pwd = pwd
    def __str__(self) -> str:
        return  "[" + str(self.n1) + ", " + str(self.n2) + ", " + self.letter + ", " + self.pwd + "]"

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        lines = f.readlines()
    criteria = []
    for line in lines:
        temp = line.split(" ")
        nums = temp[0].split('-')
        n1 = nums[0]
        n2 = nums[1]
        letter = temp[1][0]
        pwd = temp[2][:-1]
        criteria.append(Criteria(n1, n2, letter, pwd))
    return criteria
        

def test_day2(outfile=None):
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

    print(header + "Day 2 Results" + codeblock)
    
    assert count_valid1(test_arr) == 2
    print("P1:\t" + str(count_valid1(arr)))

    assert count_valid2(test_arr) == 1
    print("P2:\t" + str(count_valid2(arr)) + codeblock)

if __name__ == "__main__":
    test_day2()