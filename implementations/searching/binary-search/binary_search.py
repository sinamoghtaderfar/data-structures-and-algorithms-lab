#arr = [5,10,15,20,25,30,35]
#index =0, 1, 2, 3  4 ,5, 6
#target = 25  index = 4

def binary_search(arr, target):
    low = 0
    high = len(arr)-1  # last valid index
    
    while low <= high:
        mid = (low + high) // 2   # middle index of the current search range
        guess = arr[mid]
        
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1  # target not found

myarr = [5,10,15,20,25,30,35]

print(binary_search(myarr, 45))
