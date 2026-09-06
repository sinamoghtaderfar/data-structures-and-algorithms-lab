def find_smallest(arr):
    """Find the smallest element in an array."""
    
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
  
#print(find_smallest([5, 3, 6, 2, 10]))  #-> Output: 3


def selection_sort(arr):
    """Sort an array using the selection sort algorithm."""
    
    new_arr = []
    copied_arr = list(arr)
    
    for _ in range(len(copied_arr)):
        smallest_index = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest_index))
        
        
    return new_arr
  
numbers = [5, 3, 6, 2, 10]

sorted_numbers = selection_sort(numbers)

print(sorted_numbers)
print(numbers)