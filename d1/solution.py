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


if __name__ == "__main__":
    with open("test_input") as f:
        test_nums = [int(num) for num in f.readlines()]
    test_nums.sort()

    with open("input") as f:
        nums = [int(num) for num in f.readlines()]
    nums.sort()
  
    assert twosum(test_nums, 2020) == 514579
    print("P1:\t" + str(twosum(nums, 2020)))

    assert threesum(test_nums, 2020) == 241861950
    print("P2:\t" + str(threesum(nums, 2020)))