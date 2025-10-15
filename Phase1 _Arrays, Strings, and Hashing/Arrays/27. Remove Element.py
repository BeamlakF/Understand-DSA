def removeElement(nums, val):
    i = 0  # TODO 1: Initialize a pointer 'i' at 0 (for placement)
    
    # TODO 2: Loop through the array with 'j'
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums [j]
            i += 1
        return i
    
    # Why return i? Because i tells us how many valid elements remain.
# The array’s first i elements are the new array.
