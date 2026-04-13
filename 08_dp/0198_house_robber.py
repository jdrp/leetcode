def house_robber(nums):
    prev1 = 0
    prev2 = 0
    
    for n in nums:
        current = max(prev1, prev2 + n)
        prev2 = prev1
        prev1 = current
        
    return prev1


print(house_robber([]))                  # 0
print(house_robber([5]))                 # 5
print(house_robber([2, 1]))              # 2
print(house_robber([1, 2]))              # 2

print(house_robber([1,2,3,1]))           # 4
print(house_robber([2,7,9,3,1]))         # 12

print(house_robber([2,1,1,2]))           # 4
print(house_robber([10,1,1,10]))         # 20
print(house_robber([2,4,8,9,9,3]))       # 19
print(house_robber([1,3,1,3,100]))       # 103

print(house_robber([5,5,10,100,10,5]))   # 110
print(house_robber([4,1,2,7,5,3,1]))     # 14