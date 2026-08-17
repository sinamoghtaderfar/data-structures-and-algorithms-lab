

#find 10:08:53 with binary search

def find_first_log_at_or_after(log, target_time):

    low, high = 0, len(log) - 1
    
    candidate = None
    
    while low <= high:
        mid = (low + high) // 2
        guess = log[mid][0]
        
        
        if guess > target_time:
            high = mid - 1
            candidate = mid
        elif guess == target_time:
            return mid
        else:
            low = mid + 1 
            
    return candidate
        
logs = [
    ("10:00:01", "Server started"),
    ("10:02:15", "User login"),
    ("10:05:40", "Payment request"),
    ("10:08:12", "Database warning"),
    ("10:08:48", "Server warning"),
    ("10:12:33", "User logout"),
]
print (find_first_log_at_or_after(logs,"09:08:15"))
