
import os
import sys

def get_max_bp(seats):    
    # print(seats)
    return max(seats)


def find_missing(seats):    
    seats.sort()
    for idx, num in enumerate(seats):
        if num - seats[0] != idx:
            return num - 1
    return seats[-1] + 1

def get_seat_id(bp):
    seat = ['0' if letter in ['F', 'L'] else '1' for letter in bp]
    # print(seat)
    return int(''.join(seat), 2)

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = f.readlines()
    # print(arr)
    return [get_seat_id(bp[:-1]) for bp in arr]


def test_day5(outfile):

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

    print(header + "Day 5 Results:" + codeblock)

    assert get_max_bp(test_arr) == 820
    print("P1:\t" + str(get_max_bp(arr)))

    # assert find_missing(test_arr) == 0
    print("P2:\t" + str(find_missing(arr)) + codeblock)

if __name__ == "__main__":
    test_day5(None)