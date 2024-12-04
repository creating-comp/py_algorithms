def zeroSumSubarray(nums):
    
    if len(nums) == 0:
        return False

    sum_set = set()
    current_sum = 0

    for num in nums:
        current_sum += num
        
        if current_sum == 0 or current_sum in sum_set:
            return True
        
        sum_set.add(current_sum)

    return False
