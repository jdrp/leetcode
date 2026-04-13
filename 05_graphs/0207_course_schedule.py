def validate_course_schedule(numCourses, prerequisites):
    dependencies = [[] for _ in range(numCourses)]
    states = [0 for _ in range(numCourses)]
    
    for node_id, dep_id in prerequisites:
        dependencies[node_id].append(dep_id)
        
    def dfs(node_id):
        if states[node_id] == 2:  # already validated
            return True
        
        if states[node_id] == 1:  # found a loop
            return False
        
        states[node_id] = 1
        if all(dfs(child) for child in dependencies[node_id]):
            states[node_id] = 2
            return True
        else:
            return False
            
    for i in range(numCourses):
        if not dfs(i):
            return False
        
    return True


print(validate_course_schedule(2, [[1, 0]]))                          # True
print(validate_course_schedule(2, [[1, 0], [0, 1]]))                  # False

print(validate_course_schedule(4, [[1, 0], [2, 1], [3, 2]]))         # True
print(validate_course_schedule(4, [[1, 0], [2, 1], [0, 2]]))         # False

print(validate_course_schedule(1, []))                                # True
print(validate_course_schedule(3, []))                                # True

print(validate_course_schedule(3, [[1, 0], [2, 0]]))                 # True
print(validate_course_schedule(3, [[1, 0], [2, 1], [1, 2]]))         # False

print(validate_course_schedule(5, [[1,0],[2,0],[3,1],[3,2],[4,3]]))  # True
print(validate_course_schedule(5, [[1,0],[2,0],[3,1],[3,2],[4,3],[1,4]]))  # False

print(validate_course_schedule(4, [[0,1],[1,2],[2,3]]))              # True
print(validate_course_schedule(4, [[0,1],[1,2],[2,3],[3,1]]))        # False

print(validate_course_schedule(6, [[1,0],[2,1],[3,2],[4,2],[5,4]]))  # True
print(validate_course_schedule(6, [[1,0],[2,1],[3,2],[4,2],[5,4],[2,5]]))  # False