def removeDuplicates(nums):
    if not nums:
        return False
    i = 0  
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums [j]
            
        return i + 1
    
    # Why return i +1? Because i is index based, so to get the count we add 1. i started from 0...and in is the array is sorted then the first element is unique so no need to compare it

