def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    
    intervals = sorted(intervals, key=lambda i: i[0])
    
    merged = [intervals[0][:]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        
        else:
            merged.append([start, end])
    
    return merged

            
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,4],[4,5]]))