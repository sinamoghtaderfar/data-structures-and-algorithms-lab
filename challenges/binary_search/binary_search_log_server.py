def find_first_log_at_or_after(logs, target_time):
    """
    Find the first log whose timestamp is equal to or later
    than the target time.

    Args:
        logs: A sorted list of (timestamp, message) tuples.
        target_time: Timestamp to search for.

    Returns:
        The index of the first matching log, otherwise None.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    low = 0
    high = len(logs) - 1

    candidate = None

    while low <= high:
        mid = (low + high) // 2
        guess = logs[mid][0]

        if guess >= target_time:
            candidate = mid
            high = mid - 1
        else:
            low = mid + 1

    return candidate


if __name__ == "__main__":
    logs = [
        ("10:00:01", "Server started"),
        ("10:02:15", "User login"),
        ("10:05:40", "Payment request"),
        ("10:08:12", "Database warning"),
        ("10:08:48", "Server warning"),
        ("10:12:33", "User logout"),
    ]

    print(find_first_log_at_or_after(logs, "10:08:15"))