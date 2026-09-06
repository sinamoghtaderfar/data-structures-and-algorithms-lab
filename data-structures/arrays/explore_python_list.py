import sys

numbers = []

print("Empty list memory:", sys.getsizeof(numbers))

for i in range(20):
  numbers.append(i)
  
  print(f"Length of the list: {len(numbers)} and memory: {sys.getsizeof(numbers)}")