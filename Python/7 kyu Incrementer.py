def incrementer(nums):
    return [(nums[i-1] + i) % 10 for i in range(1, len(nums) + 1)]
