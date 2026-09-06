from selection_sort import find_smallest


def selection_sort_steps(arr):
    """Sort an array using the selection sort algorithm and return the steps."""
    
    remaining = list(arr)
    sorted_arr = []
    steps = []
    
    while remaining:
        smallest_index = find_smallest(remaining)
        smallest_value = remaining.pop(smallest_index)
        sorted_arr.append(smallest_value)
        steps.append({
          "picked": smallest_value,
          "sorted": list(sorted_arr),
          "remaining": list(remaining),
        })
        
    return steps
  
steps = selection_sort_steps([5, 3, 6, 2, 10])

for step in steps:
    print(step)