def binary_search(arr, target):
    """
    Search for a target value in a sorted list using Binary Search.

    Args:
        arr: A sorted list of values.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise None.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid

        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    myarr = [5, 10, 15, 20, 25, 30, 35]

    print(binary_search(myarr, 45))