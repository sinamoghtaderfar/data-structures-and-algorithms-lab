[فارسی](./README.fa.md)

# Binary Search Challenge — Server Log Boundary Search

This challenge takes Binary Search beyond exact-value lookup and applies it to a more realistic problem: finding the first server log at or after a requested time.

The main idea is simple:

> Given sorted timestamps, find the **first position** whose timestamp is greater than or equal to the target.

This is a boundary-search problem and a useful variation of Binary Search.

---

## Problem

A server stores its logs in chronological order.

Each log contains a timestamp and a message:

```text
(timestamp, message)
```

Example:

```python
logs = [
    ("10:00:01", "Server started"),
    ("10:02:15", "User login"),
    ("10:05:40", "Payment request"),
    ("10:08:12", "Database warning"),
    ("10:08:48", "Server warning"),
    ("10:12:33", "User logout"),
]
```

Implement a function:

```python
find_first_log_at_or_after(logs, target_time)
```

that returns the index of the **first log whose timestamp is equal to or later than `target_time`**.

In other words, find the first index satisfying:

```text
timestamp >= target_time
```

If no such log exists, return:

```python
None
```

The solution must use **Binary Search**.

---

## Why Binary Search?

A straightforward solution could scan the logs from beginning to end:

```python
for log in logs:
    ...
```

That works, but in the worst case it examines every log:

```text
O(n)
```

Because the logs are already sorted by timestamp, we can do better.

Binary Search lets us repeatedly eliminate approximately half of the remaining search space:

```text
O(log n)
```

For a large log dataset, that difference can become significant.

---

## Example 1 — Exact Match

Input:

```python
target_time = "10:08:12"
```

Logs:

```text
Index:  0         1         2         3         4         5
Time:   10:00:01  10:02:15  10:05:40  10:08:12  10:08:48  10:12:33
                                      ↑
```

The first timestamp satisfying:

```text
timestamp >= "10:08:12"
```

is at index:

```text
3
```

Expected result:

```python
3
```

---

## Example 2 — Target Between Two Logs

Input:

```python
target_time = "10:08:15"
```

There is no log exactly at `10:08:15`.

The surrounding timestamps are:

```text
10:08:12
10:08:48
```

`10:08:12` is too early.

`10:08:48` is the first timestamp satisfying:

```text
timestamp >= target_time
```

Expected result:

```python
4
```

because:

```python
logs[4]
```

is:

```python
("10:08:48", "Server warning")
```

---

## Example 3 — Target Before All Logs

Input:

```python
target_time = "09:30:00"
```

The first log is already later than the requested time:

```text
10:00:01
```

Expected result:

```python
0
```

---

## Example 4 — Target After All Logs

Input:

```python
target_time = "23:00:00"
```

No timestamp satisfies:

```text
timestamp >= "23:00:00"
```

Expected result:

```python
None
```

---

## Example 5 — Duplicate Timestamps

Consider:

```python
logs = [
    ("10:00:00", "Server started"),
    ("10:05:00", "Request A"),
    ("10:05:00", "Request B"),
    ("10:05:00", "Request C"),
    ("10:10:00", "Server warning"),
]
```

Input:

```python
target_time = "10:05:00"
```

There are multiple exact matches.

The requirement is to return the **first** valid log.

Expected result:

```python
1
```

This is an important detail.

Finding *an* exact match is not enough — we need the **leftmost valid position**.

---

## From Exact Search to Boundary Search

A basic Binary Search often asks:

> Does this exact value exist?

This challenge asks something slightly different:

> Where does the valid range begin?

For the condition:

```text
timestamp >= target_time
```

we want the leftmost timestamp for which the condition becomes true.

Conceptually:

```text
too early        valid
   ↓               ↓

10:00  10:05  10:08  10:12  10:20
                ↑
           first valid value
```

This type of problem is commonly described as a **lower-bound search**.

---

## The Candidate Idea

During the search, suppose:

```text
guess >= target_time
```

The current log is a valid answer.

But it may not be the **first** valid answer.

There could be another valid timestamp further to the left.

So instead of returning immediately, we:

1. save the current index as a candidate;
2. continue searching the left half.

Conceptually:

```text
guess >= target

      ↓

current index is valid

      ↓

save candidate

      ↓

search left for an earlier valid index
```

If we find a better candidate, it replaces the previous one.

---

## Search Decisions

The algorithm only needs two cases.

### Case 1 — Guess Is Too Early

If:

```text
guess < target_time
```

then the current timestamp cannot be the answer.

Because the data is sorted, everything to its left is also too early.

So we discard that entire part:

```python
low = mid + 1
```

---

### Case 2 — Guess Is Valid

If:

```text
guess >= target_time
```

then the current index is a possible answer.

We save it:

```python
candidate = mid
```

but continue searching left:

```python
high = mid - 1
```

because an earlier valid timestamp may still exist.

This also correctly handles duplicate timestamps.

---

## Example Search

Suppose:

```text
target_time = "10:08:15"
```

and:

```text
10:00:01
10:02:15
10:05:40
10:08:12
10:08:48
10:12:33
```

### Step 1

Middle value:

```text
10:05:40
```

Comparison:

```text
10:05:40 < 10:08:15
```

So this value and everything to its left can be discarded.

```text
→ search right
```

### Step 2

Next middle value:

```text
10:08:48
```

Comparison:

```text
10:08:48 >= 10:08:15
```

This is a valid answer:

```text
candidate = index 4
```

But there may be an earlier valid value:

```text
→ search left
```

### Step 3

Next value:

```text
10:08:12
```

Comparison:

```text
10:08:12 < 10:08:15
```

So:

```text
→ search right
```

The search range is now empty.

The best candidate found was:

```text
index 4
```

which corresponds to:

```python
("10:08:48", "Server warning")
```

---

## Why String Comparison Works Here

The timestamps use the fixed-width format:

```text
HH:MM:SS
```

For zero-padded timestamps in this format, lexicographical string order matches chronological order within the same day.

For example:

```text
"10:05:00" < "10:08:00" < "11:00:00"
```

That allows these timestamp strings to be compared directly in this challenge.

For more complex real-world timestamps involving dates, time zones, or different formats, parsing them into proper datetime values would be safer.

---

## Complexity

Binary Search eliminates approximately half of the remaining search space after each comparison.

Therefore:

```text
Time Complexity: O(log n)
```

The algorithm only needs a few additional variables:

```text
low
high
mid
candidate
```

Therefore:

```text
Space Complexity: O(1)
```

---

## Edge Cases

The implementation should correctly handle:

- an exact timestamp;
- a target between two timestamps;
- a target before the first log;
- a target after the last log;
- an empty log list;
- a single log entry;
- duplicate timestamps.

These cases are covered by the test suite.

---

## Implementation

The solution is available here:

[`solution.py`](./solution.py)

Tests:

[`test_solution.py`](./test_solution.py)

Run the tests from the repository root:

```bash
pytest challenges/binary-search/test_solution.py
```

---

## What I Learned

The most useful lesson from this challenge is that Binary Search is not just a piece of code for finding exact values.

The deeper idea is:

> Use sorted data to safely eliminate part of the search space after every comparison.

In basic Binary Search, I might stop when:

```text
guess == target
```

Here, that is not always enough.

I need to find the **boundary** where values first begin satisfying:

```text
value >= target
```

That changes how I update `low` and `high`.

The `candidate` variable lets me remember a valid answer while continuing to search for an earlier and therefore better one.

---

## Key Takeaway

Basic Binary Search asks:

> Where is this exact value?

This challenge asks:

> Where is the first value that is at least this large?

That small change turns a basic search exercise into a useful boundary-search pattern.

And because the data is sorted, the solution still runs in:

```text
O(log n)
```