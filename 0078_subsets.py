def subsets(nums):
    result = []
    path = []
    
    def backtrack(i):
        if i == len(nums):
            result.append(path.copy())
            return
        
        backtrack(i+1)
        
        path.append(nums[i])
        backtrack(i+1)
        path.pop()
        
    backtrack(0)
    return result


print(subsets([1,2,3]))
# [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]] en cualquier orden

print(subsets([0]))
# [[], [0]]

print(subsets([]))
# [[]]

print(subsets([1,2]))
# [[], [1], [2], [1,2]] en cualquier orden

print(subsets([4,5,6]))
# 8 subsets en total

print(subsets([1,3,5,7]))
# 16 subsets en total

print(len(subsets([1,2,3,4])))
# 16