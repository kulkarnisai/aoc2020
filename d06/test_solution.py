
import os
import sys

def FNAME1(groups):
    ans = 0
    for group in groups:
        union = set()
        for user in group:
            union = union | user
        ans = ans + len(union)
    return ans


def FNAME2(groups):    
    ans = 0
    for group in groups:
        intersection = group[0]
        for user in group[1:]:
            intersection = intersection & user
        ans = ans + len(intersection)
    return ans

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = f.readlines()
    groups = []
    currgroup = []
    for user in arr:
        if len(user) > 1:
            currgroup.append(set(user[:-1]))
        else:
            groups.append(currgroup)
            currgroup = [] 
    if currgroup: groups.append(currgroup)       
    return groups

def test_day6(outfile):

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

    print(header + "Day 6 Results:" + codeblock)

    assert FNAME1(test_arr) == 11
    print("P1:\t" + str(FNAME1(arr)))

    assert FNAME2(test_arr) == 6
    print("P2:\t" + str(FNAME2(arr)) + codeblock)

if __name__ == "__main__":
    test_day6(None)