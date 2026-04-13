def two_sum(nums, target):
    complement_map = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in complement_map:
            return [complement_map[comp], i]
        complement_map[n] = i
    return []
        
    
print(two_sum([3], 8))
