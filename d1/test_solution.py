import os
from bisect import bisect

def twosum(nums, target):    
    for left in range(len(nums)):
        right = bisect(nums, target - nums[left])
        if right > 0 and nums[right - 1] == target - nums[left]:
            return nums[left] * nums[right-1]
    return -1
        

def threesum(nums, target):    
   for left in range(len(nums)):
       ans = twosum(nums[left+1:], target - nums[left])
       if ans != -1:
           return nums[left] * ans
   return -1

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = [int(num) for num in f.readlines()]
    arr.sort()
    return arr

def test_day1(outfile=None):
    test_nums = preprocess("test_input")
    nums = preprocess("input")

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 1 Results" + codeblock)

    assert twosum(test_nums, 2020) == 514579
    print("P1:\t" + str(twosum(nums, 2020)))

    assert threesum(test_nums, 2020) == 241861950
    print("P2:\t" + str(threesum(nums, 2020)) + codeblock)

if __name__ == "__main__":
    test_day1()