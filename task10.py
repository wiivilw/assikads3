def quickSort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quickSort(nums, low, p - 1)
        quickSort(nums, p + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low

    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i

nums = [5,2,3,1,4]
quickSort(nums,0,len(nums)-1)
print(nums)