from solution import find_first_log_at_or_after


logs = [
    ("10:00:01", "Server started"),
    ("10:02:15", "User login"),
    ("10:05:40", "Payment request"),
    ("10:08:12", "Database warning"),
    ("10:08:48", "Server warning"),
    ("10:12:33", "User logout"),
]


def test_exact_match():
    result = find_first_log_at_or_after(logs, "10:08:12")

    assert result == 3


def test_between_two_timestamps():
    result = find_first_log_at_or_after(logs, "10:08:15")

    assert result == 4


def test_before_first_log():
    result = find_first_log_at_or_after(logs, "09:30:00")

    assert result == 0


def test_after_last_log():
    result = find_first_log_at_or_after(logs, "23:00:00")

    assert result is None


def test_empty_logs():
    result = find_first_log_at_or_after([], "10:00:00")

    assert result is None


def test_single_log():
    single_log = [
        ("10:00:01", "Server started"),
    ]

    result = find_first_log_at_or_after(
        single_log,
        "09:00:00",
    )

    assert result == 0


def test_duplicate_timestamps_returns_first():
    duplicate_logs = [
        ("10:00:01", "Server started"),
        ("10:05:00", "Request A"),
        ("10:05:00", "Request B"),
        ("10:05:00", "Request C"),
        ("10:10:00", "Server stopped"),
    ]

    result = find_first_log_at_or_after(
        duplicate_logs,
        "10:05:00",
    )

    assert result == 1