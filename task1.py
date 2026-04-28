def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in m:
            return [m[diff], i]
        m[nums[i]] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))