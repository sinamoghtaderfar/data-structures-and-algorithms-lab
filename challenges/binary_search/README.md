[English](./README.md) | [فارسی](./README.fa.md)

# Binary Search Challenge — Server Log Search

This challenge applies Binary Search to a more realistic problem using sorted server logs.

The goal is to move beyond searching for an exact number in a simple array and adapt the Binary Search idea to a practical search problem.

---

## Problem

A server stores its logs in chronological order.

Each log contains:

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

Write a function that receives a `target_time` and finds the **first log whose timestamp is equal to or later than the target time**.

The condition is:

```text
timestamp >= target_time
```

The solution must use **Binary Search**.

---

## Example 1 — Exact Match

Input:

```python
target_time = "10:08:12"
```

The timestamp exists exactly in the log list:

```text
Index:  0         1         2         3
Time:   10:00:01  10:02:15  10:05:40  10:08:12
                                      ↑
```

Expected result:

```text
3
```

---

## Example 2 — Target Between Two Logs

Input:

```python
target_time = "10:08:15"
```

There is no log at exactly `10:08:15`.

The closest surrounding timestamps are:

```text
10:08:12
10:08:48
```

`10:08:12` is too early.

The first timestamp that satisfies:

```text
timestamp >= target_time
```

is:

```text
10:08:48
```

Expected result:

```text
4
```

Because:

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

The first log already occurs after the requested time:

```text
10:00:01
```

Expected result:

```text
0
```

---

## Example 4 — No Valid Log

Input:

```python
target_time = "23:00:00"
```

No log exists at or after this time.

Expected result:

```text
None
```

---

## Constraint

The solution should not scan the logs one by one.

A linear search such as:

```python
for log in logs:
    ...
```

would have a worst-case running time of:

```text
O(n)
```

Instead, the challenge should preserve the main advantage of Binary Search:

```text
O(log n)
```

---

## Key Idea

Normal Binary Search usually searches for an exact value.

For example:

```text
guess == target
→ return the index
```

This challenge is slightly different because the exact target may not exist.

For example:

```text
target = 10:08:15
```

while the available timestamps are:

```text
10:08:12
10:08:48
```

The algorithm must still return `10:08:48`.

This means that while searching, some values can become possible answers.

---

## Candidate

If:

```text
guess > target_time
```

the current log is a valid possible answer.

However, there might be another valid log closer to the target on the left side.

Therefore, the current index is stored as a **candidate**, and Binary Search continues searching to the left.

Conceptually:

```text
guess > target

        ↓

save current index
as candidate

        ↓

continue searching
the left half
```

If a better candidate is found later, it replaces the previous one.

---

## Search Decisions

The search follows three main cases.

### Guess is smaller than the target

```text
guess < target_time
```

The current value and everything to its left are too early.

Search the right half.

```text
low = mid + 1
```

---

### Guess exactly matches the target

```text
guess == target_time
```

The requested timestamp has been found.

Return its index.

---

### Guess is greater than the target

```text
guess > target_time
```

The current log may be the answer.

Save it as the current candidate and continue searching the left half.

```text
candidate = mid
high = mid - 1
```

---

## Example Search

Suppose:

```text
target = 10:08:15
```

and the logs are:

```text
10:00:01
10:02:15
10:05:40
10:08:12
10:08:48
10:12:33
```

Binary Search may proceed like this:

```text
Step 1

guess = 10:05:40

10:05:40 < 10:08:15

→ search right
```

Then:

```text
Step 2

guess = 10:08:48

10:08:48 > 10:08:15

→ candidate = index 4
→ search left
```

Then:

```text
Step 3

guess = 10:08:12

10:08:12 < 10:08:15

→ search right
```

The search range becomes empty.

The best candidate found was:

```text
index 4
```

which corresponds to:

```python
("10:08:48", "Server warning")
```

---

## Complexity

Binary Search removes roughly half of the remaining search space after every comparison.

Therefore:

```text
Time Complexity: O(log n)
```

The algorithm only needs a few variables such as:

```text
low
high
mid
candidate
```

so the additional memory usage is constant:

```text
Space Complexity: O(1)
```

---

## Implementation

The implementation for this challenge can be found here:

[View `binary_search_log_server.py`](./binary_search_log_server.py)

---

## Suggested Tests

Useful cases to test:

* Exact timestamp exists
* Target is between two timestamps
* Target is before the first log
* Target is after the last log
* Empty log list
* Single log entry

---

## What I Learned

This challenge extends the basic Binary Search implementation from Chapter 1.

Instead of only searching for an exact value, I adapted the algorithm to find the first value that satisfies:

```text
value >= target
```

The important idea is that Binary Search is not just a fixed piece of code.

The real skill is understanding how to use:

```text
low
high
mid
```

to safely eliminate part of an ordered search space.

The `candidate` variable makes it possible to remember a valid answer while continuing the search for a better one.

---

## Key Takeaway

The standard Binary Search question is:

> Is this exact target in the collection?

This challenge asks a more useful question:

> What is the first value that is equal to or greater than the target?

Both can still be solved in:

```text
O(log n)
```

because the data is sorted and the search space can be reduced by approximately half after every comparison.
