def longest_substring(s):
    left = 0
    seen = set()
    top_size = 0
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        seen.add(s[right])
        top_size = max(top_size, right - left + 1)
        
    return top_size
            
            
        
        
print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))