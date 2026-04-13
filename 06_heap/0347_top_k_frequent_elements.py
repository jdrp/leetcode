import heapq
from collections import Counter


def top_k_frequent(nums, k):
    num_counts = Counter(nums)        
    heap = []
    
    for num, count in num_counts.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
            
        else:
            if count > heap[0][0]:
                heapq.heappushpop(heap, (count, num))
                
    return [num for _, num in heap]


print(top_k_frequent([1,1,1,2,2,3], 2))        # [1,2] en cualquier orden
print(top_k_frequent([1], 1))                  # [1]

print(top_k_frequent([4,4,4,4], 1))            # [4]

print(top_k_frequent([1,2,3,4], 2))            # cualquier 2 elementos válidos; todas tienen freq 1
print(top_k_frequent([1,1,2,2,3,3], 2))        # cualquier 2 entre [1,2,3]

print(top_k_frequent([5,5,5,2,2,3], 1))        # [5]
print(top_k_frequent([5,5,5,2,2,3], 2))        # [5,2] en cualquier orden

print(top_k_frequent([-1,-1,-1,2,2,3], 2))     # [-1,2] en cualquier orden

print(top_k_frequent([1,2], 2))                # [1,2] en cualquier orden

print(top_k_frequent([7,7,8,8,8,9,9,9,9], 3))  # [7,8,9] en cualquier orden
print(top_k_frequent([0,0,0,0,1,1,2], 2))      # [0,1] en cualquier orden