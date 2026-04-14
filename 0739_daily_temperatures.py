def daily_temperatures(temperatures):
    stack = []
    answer = [0] * len(temperatures)
    
    for id, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            other_id = stack.pop()
            answer[other_id] = id - other_id
        stack.append(id)
            
    return answer


print(daily_temperatures([73,74,75,71,69,72,76,73]))   # [1,1,4,2,1,1,0,0]
print(daily_temperatures([30,40,50,60]))               # [1,1,1,0]
print(daily_temperatures([30,60,90]))                  # [1,1,0]

print(daily_temperatures([90,80,70,60]))               # [0,0,0,0]
print(daily_temperatures([70,70,70]))                  # [0,0,0]
print(daily_temperatures([70]))                        # [0]

print(daily_temperatures([70,71,70,72]))               # [1,2,1,0]
print(daily_temperatures([70,69,68,71]))               # [3,2,1,0]
print(daily_temperatures([71,70,69,72]))               # [3,2,1,0]

print(daily_temperatures([65,66,65,66,65,67]))         # [1,4,1,2,1,0]
print(daily_temperatures([80,79,78,77,76,81]))         # [5,4,3,2,1,0]
