import math

def find_min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    
    while right > left:
        k = math.floor((right + left) / 2)
        total_h = sum((pile + k - 1) // k for pile in piles)
        is_valid = (total_h <= h)
        
        if is_valid:
            right = k
        else:
            left = k + 1
        
    return left


print(find_min_eating_speed([3,6,7,11], 8))          # 4
print(find_min_eating_speed([30,11,23,4,20], 5))    # 30
print(find_min_eating_speed([30,11,23,4,20], 6))    # 23

print(find_min_eating_speed([1], 1))                # 1
print(find_min_eating_speed([10], 5))               # 2
print(find_min_eating_speed([10], 10))              # 1

print(find_min_eating_speed([5,5,5,5], 4))          # 5
print(find_min_eating_speed([5,5,5,5], 8))          # 3

print(find_min_eating_speed([100,1], 2))            # 100
print(find_min_eating_speed([100,1], 101))          # 1

print(find_min_eating_speed([9,9,9], 3))            # 9
print(find_min_eating_speed([9,9,9], 9))            # 3

print(find_min_eating_speed([8,16,24], 6))          # 8
print(find_min_eating_speed([8,16,24], 7))          # 8
print(find_min_eating_speed([8,16,24], 8))          # 8