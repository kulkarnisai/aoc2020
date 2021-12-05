
import os
import sys

def FNAME1(code):    
    pc = 0
    acc = 0
    executed = set()
    while pc not in executed and pc < len(code):
        executed.add(pc)
        if code[pc][0] == 'jmp':
            pc = pc + code[pc][1]
        elif code[pc][0] == 'acc':
            acc = acc + code[pc][1]
            pc = pc + 1
        else:
            pc = pc + 1
    return acc, pc


def FNAME2(code):
    for i in range(len(code)):
        acc, pc = 0, 0
        if code[i][0] == 'jmp': 
            code[i][0] = 'nop'
            acc, pc = FNAME1(code)
            code[i][0] = 'jmp'
        elif code[i][0] == 'nop': 
            code[i][0] = 'jmp'
            acc, pc = FNAME1(code)
            code[i][0] = 'nop'
        
        if pc == len(code):
            return acc
    return 0

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        code = [[line[:3], int(line[4:-1])] for line in f.readlines()]
    # print(code)
    return code

def test_day8(outfile):

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

    print(header + "Day 8 Results:" + codeblock)

    assert FNAME1(test_arr)[0] == 5
    print("P1:\t" + str(FNAME1(arr)[0]))

    assert FNAME2(test_arr) == 8
    print("P2:\t" + str(FNAME2(arr)) + codeblock)

if __name__ == "__main__":
    test_day8(None)