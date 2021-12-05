
import os
import sys
import re

def FNAME1(bu, color):   

    currlist = bu[color]
    outside_bags = set()
    while currlist:
        nextcolor = currlist.pop()
        if nextcolor not in outside_bags:
            if nextcolor in bu: currlist = currlist + bu[nextcolor]
            outside_bags.add(nextcolor)
    return len(outside_bags)

def FNAME2(td, color):  
    count = 0
    for subcolor in td[color]:
        count = count + td[color][subcolor] * (FNAME2(td, subcolor) + 1)
    # print(color, count)
    return count

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = f.readlines()
    td, bu = {}, {}
    topre = re.compile(r"(?P<topc>[a-zA-Z ]+) (?P<bctoken>bags contain)")
    botre = re.compile(r"(\d+) (\w+ \w+) (bag)")
    for line in arr:
        topc = topre.match(line).group('topc')
        td[topc] = {}
        for match in botre.findall(line):
            td[topc][match[1]]  = int(match[0])
            if match[1] in bu: bu[match[1]].append(topc)
            else: bu[match[1]] = [topc]
    # print(td)
    return td, bu

def test_day7(outfile):

    test_td1, test_bu1 = preprocess("test_input1")
    test_td2, test_bu2 = preprocess("test_input2")
    td, bu = preprocess("input")
  

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 7 Results:" + codeblock)

    assert FNAME1(test_bu1, 'shiny gold') == 4
    print("P1:\t" + str(FNAME1(bu, 'shiny gold')))

    assert FNAME2(test_td2, 'shiny gold') == 126
    print("P2:\t" + str(FNAME2(td, 'shiny gold')) + codeblock)

if __name__ == "__main__":
    test_day7(None)