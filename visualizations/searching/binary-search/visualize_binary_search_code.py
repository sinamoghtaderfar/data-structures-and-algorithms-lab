def visualize_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        print(
            f"\nStep {step}: "
            f"Searching in range [{low}, {high}] - "
            f"Middle index: {mid}, Guess: {guess}"
        )

        for index, value in enumerate(arr):
            if index == mid:
                print(f"({value})[Mid]", end=" ")
            elif index == low:
                print(f"[{value}][Low]", end=" ")
            elif index == high:
                print(f"[{value}][High]", end=" ")
            else:
                print(value, end=" ")

        print()

        if guess == target:
            print(f"Target {target} found at index {mid}.")
            return mid

        elif guess > target:
            print(
                f"Guess {guess} is greater than target {target}. "
                f"Moving high to {mid - 1}."
            )
            print("Guess is too high → search left half")
            
            high = mid - 1

        else:
            print(
                f"Guess {guess} is less than target {target}. "
                f"Moving low to {mid + 1}."
            )
            print("Guess is too low → search right half")
            low = mid + 1

        step += 1

    print(f"Target {target} not found in the array.")
    return None


arr = [5, 10, 15, 20, 25, 30, 35]

visualize_binary_search(arr, 25)