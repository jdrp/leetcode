def num_islands(grid):
    if not grid: return 0
    height, width = len(grid), len(grid[0])
    
    def flood_fill(r, c):
        if r < 0 or r > height - 1 or c < 0 or c > width - 1: return
        
        if grid[r][c] == "0": return
        grid[r][c] = "0"
        
        flood_fill(r-1, c)
        flood_fill(r+1, c)
        flood_fill(r, c-1)
        flood_fill(r, c+1)
    
    total_islands = 0
    for r in range(height):
        for c in range(width):
            val = grid[r][c]
            if val == "1":
                total_islands += 1
                flood_fill(r, c)
                
    return total_islands
            
            
grid1 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

grid2 = [
    ["1","1","1","1"],
    ["1","1","1","1"],
    ["1","1","1","1"]
]

grid3 = [
    ["0","0","0"],
    ["0","0","0"],
    ["0","0","0"]
]

grid4 = [
    ["1"]
]

grid5 = [
    ["0"]
]

grid6 = [
    ["1","0","1","0"],
    ["0","0","0","0"],
    ["1","0","1","1"]
]

grid7 = [
    ["1","0","1"],
    ["0","1","0"],
    ["1","0","1"]
]

grid8 = [
    ["1","1","0","0"],
    ["0","1","0","1"],
    ["0","1","1","1"],
    ["0","0","0","0"]
]

grid9 = [
    ["1","1","0","1","0","1"]
]

grid10 = [
    ["1"],
    ["1"],
    ["0"],
    ["1"],
    ["1"]
]


print(num_islands(grid1))   # 3
print(num_islands(grid2))   # 1
print(num_islands(grid3))   # 0
print(num_islands(grid4))   # 1
print(num_islands(grid5))   # 0
print(num_islands(grid6))   # 4
print(num_islands(grid7))   # 5
print(num_islands(grid8))   # 1
print(num_islands(grid9))   # 3
print(num_islands(grid10))  # 2