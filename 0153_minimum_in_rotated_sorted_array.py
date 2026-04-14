def find_min(nums):
    if not nums: return None
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if nums[left] <= nums[right]:
            return nums[left]
        
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
            
            
print(find_min([3,4,5,1,2]))          # 1
print(find_min([4,5,6,7,0,1,2]))      # 0
print(find_min([11,13,15,17]))        # 11

print(find_min([2,1]))                # 1
print(find_min([1,2]))                # 1

print(find_min([5,1,2,3,4]))          # 1
print(find_min([2,3,4,5,1]))          # 1
print(find_min([1]))                  # 1

print(find_min([6,7,8,9,1,2,3,4,5]))  # 1
print(find_min([2,3,4,5,6,7,8,1]))    # 1
print(find_min([1,2,3,4,5]))          # 1