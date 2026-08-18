# Binary Search

[فارسی](./README.fa.md)

Binary Search is an efficient searching algorithm for finding a target value in a **sorted collection**.

Instead of checking every element one by one, Binary Search repeatedly divides the search space in half.

## How It Works

Given a sorted array:

```text
[5, 10, 15, 20, 25, 30, 35]
```

Suppose we want to find:

```text
25
```

Binary Search follows these steps:

1. Find the middle element.
2. Compare the middle element with the target.
3. If the target is smaller, continue searching in the left half.
4. If the target is larger, continue searching in the right half.
5. Repeat until the target is found or the search range becomes empty.

Example:

```text
[5, 10, 15, 20, 25, 30, 35]
            ^
           mid
```

The middle value is `20`.

Since:

```text
25 > 20
```

the entire left half can be ignored.

The next search range becomes:

```text
[25, 30, 35]
```

This process continues until the target is found.

## Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | `O(1)`          |
| Average Case | `O(log n)`      |
| Worst Case   | `O(log n)`      |

For the iterative implementation, the space complexity is:

```text
O(1)
```

## Important Requirement

Binary Search requires the input collection to be **sorted**.

Using Binary Search on unsorted data does not guarantee a correct result.

## Why Is Binary Search Fast?

After every comparison, Binary Search removes approximately half of the remaining search space.

For example, with around one million sorted elements, Binary Search needs only about 20 comparisons in the worst case.

This is the key difference between:

```text
Linear Search  -> O(n)
Binary Search  -> O(log n)
```

## Files

```text
binary-search/
├── assets/
│   ├── step_1.png
│   ├── step_2.png
│   └── step_3.png
├── binary_search.py
├── test_binary_search.py
├── visualize.py
├── visualize_steps.py
├── VISUALIZATION.md
├── README.fa.md
└── README.md
```

### `binary_search.py`

Contains the Binary Search implementation.

### `test_binary_search.py`

Contains automated tests for the implementation and its edge cases.

### `visualize.py`

Provides a visual representation of the Binary Search process.

### `visualize_steps.py`

Generates step-by-step visualizations showing how the search range changes.

### `assets/`

Contains generated visualization images.

### `VISUALIZATION.md`

Contains additional documentation about the visualization tools.

## Example

```python
from binary_search import binary_search

numbers = [5, 10, 15, 20, 25, 30, 35]

result = binary_search(numbers, 25)

print(result)
```

Output:

```text
4
```

The result represents the index of the target value.

## What I Learned

While implementing Binary Search, I focused on:

* understanding how the search range changes using `low`, `high`, and `mid`;
* understanding why the algorithm requires sorted data;
* understanding the difference between `O(n)` and `O(log n)`;
* testing successful searches and missing targets;
* visualizing each search step;
* applying Binary Search to a practical challenge.

## Related Challenge

A practical Binary Search exercise is available in:

```text
challenges/binary-search/
```

The challenge applies Binary Search to a log-searching scenario instead of only searching simple numeric arrays.

## Benchmark

I compared Binary Search with Linear Search using both operation counts
and measured runtime.

The benchmark includes repeated measurements, warm-up, automatic
calibration, and logarithmic visualizations.

[View the full benchmark](./BENCHMARK.md)