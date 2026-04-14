def search(nums, target):
    if not nums: return -1
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        # check left side
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
            
        # check right side
        elif nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
            
    return -1
            
print(search([4,5,6,7,0,1,2], 0))   # 4
print(search([4,5,6,7,0,1,2], 3))   # -1
print(search([1], 0))               # -1
print(search([1], 1))               # 0

print(search([1,3], 3))             # 1
print(search([1,3], 1))             # 0
print(search([3,1], 1))             # 1
print(search([3,1], 3))             # 0

print(search([5,1,3], 5))           # 0
print(search([5,1,3], 1))           # 1
print(search([5,1,3], 3))           # 2
print(search([5,1,3], 4))           # -1

print(search([6,7,8,1,2,3,4,5], 8)) # 2
print(search([6,7,8,1,2,3,4,5], 2)) # 4
print(search([6,7,8,1,2,3,4,5], 5)) # 7
print(search([6,7,8,1,2,3,4,5], 9)) # -1