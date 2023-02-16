def search(nums, target):
    first = 0
    last = len(nums)+1
    mid = (first + last)//2

    while first <= last:
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            mid = first + 1
            continue
        else:
            mid = last - 1
            continue
    return -1



nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))