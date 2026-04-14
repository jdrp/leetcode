from collections import deque


def orangesRotting(grid):
    if not grid or not grid[0]: return 0
    
    height, width = len(grid), len(grid[0])
    
    healthy_left = 0
    queue = deque()
    minutes = -1
    
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 1:
                healthy_left += 1
            if grid[r][c] == 2:
                queue.append((r,c))
                
    if healthy_left == 0:
        return 0
                
    while queue:
        minutes += 1
        level_size = len(queue)
        for _ in range(level_size):
            r, c = queue.popleft()
            for (new_r, new_c) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if new_r < 0 or new_r >= height or new_c < 0 or new_c >= width: continue
                if grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    healthy_left -= 1
                    queue.append((new_r, new_c))
           
    if healthy_left > 0:
        return -1
    return minutes


print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))          # 4
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))          # -1
print(orangesRotting([[0,2]]))                            # 0

print(orangesRotting([[1]]))                              # -1
print(orangesRotting([[2]]))                              # 0
print(orangesRotting([[0]]))                              # 0

print(orangesRotting([[2,2],[2,2]]))                      # 0
print(orangesRotting([[1,1],[1,1]]))                      # -1
print(orangesRotting([[2,1],[1,1]]))                      # 2

print(orangesRotting([[2,1,1,1]]))                        # 3
print(orangesRotting([[2],[1],[1],[1]]))                  # 3

print(orangesRotting([[2,0,1]]))                          # -1
print(orangesRotting([[2,1,0,1]]))                        # -1
print(orangesRotting([[2,1,1],[1,1,1],[1,1,2]]))          # 2