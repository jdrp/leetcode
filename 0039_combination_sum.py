def combination_sum(candidates, target):
    candidates.sort()
    result = []
    path = []
    
    def find_combinations(start, remaining):
        if remaining == 0:
            result.append(path.copy())
            
        for i in range(start, len(candidates)):
            n = candidates[i]
            if n > remaining:
                break
            path.append(n)
            find_combinations(i, remaining - n)
            path.pop()
    
    find_combinations(0, target)
    return result
    
    
print(combination_sum([2,3,6,7], 7))          # [[2,2,3],[7]] en cualquier orden
print(combination_sum([2,3,5], 8))            # [[2,2,2,2],[2,3,3],[3,5]] en cualquier orden
print(combination_sum([2], 1))                # []
print(combination_sum([1], 1))                # [[1]]
print(combination_sum([1], 2))                # [[1,1]]

print(combination_sum([2,4,6], 8))            # [[2,2,2,2],[2,2,4],[2,6],[4,4]] en cualquier orden
print(combination_sum([3,5,7], 10))           # [[3,7],[5,5]] en cualquier orden
print(combination_sum([2,3], 6))              # [[2,2,2],[3,3]] en cualquier orden
print(combination_sum([4,5], 3))              # []

print(combination_sum([8,7,4,3], 11))         # [[8,3],[7,4],[4,4,3]] en cualquier orden
print(combination_sum([2,3,5], 0))            # [[]] o [] según cómo quieras tratar target=0 fuera de LC; en LC normalmente target >= 1