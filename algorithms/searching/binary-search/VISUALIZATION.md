# Binary Search Visualization

[فارسی](./VISUALIZATION.fa.md)

This section provides a visual representation of how the **Binary Search** algorithm reduces the search space step by step.

The goal of this visualization is to make the roles of `low`, `mid`, and `high` easier to understand and to show why Binary Search has a time complexity of `O(log n)`.

## How the Visualization Works

Binary Search maintains three important positions:

* `low` — the beginning of the current search range
* `mid` — the middle position of the current search range
* `high` — the end of the current search range

At each step, the algorithm checks the value at `mid`.

Depending on the comparison with the target, either the left or right half of the remaining search space is discarded.

For example:

```text
[5, 10, 15, 20, 25, 30, 35]
 ^           ^           ^
low         mid         high
```

Suppose the target is `30`.

Since:

```text
30 > 20
```

the algorithm discards the left half and continues searching in the right half.

The new search range becomes:

```text
[25, 30, 35]
```

This process continues until the target is found or the search range becomes empty.

## Visualization Files

```text
binary-search/
├── assets/
│   ├── step_1.png
│   ├── step_2.png
│   └── step_3.png
├── visualize.py
├── visualize_steps.py
├── VISUALIZATION.md
└── VISUALIZATION.fa.md
```

### `visualize.py`

Runs a visualization of the Binary Search process.

It demonstrates how the active search range changes after each comparison.

### `visualize_steps.py`

Generates the individual visualization steps used to inspect the algorithm's execution.

### `assets/`

Contains generated visualization images.

Each image represents a different step of the Binary Search process.

## Generated Steps

### Step 1

![Binary Search Step 1](./assets/step_1.png)

The algorithm starts with the complete search range and calculates the first middle position.

### Step 2

![Binary Search Step 2](./assets/step_2.png)

After comparing the middle value with the target, one half of the search space is eliminated.

### Step 3

![Binary Search Step 3](./assets/step_3.png)

The search range becomes smaller again as Binary Search moves closer to the target.

## What the Visualization Demonstrates

The important idea is not only where `mid` is located.

The visualization demonstrates how the search space changes:

```text
n
↓
n / 2
↓
n / 4
↓
n / 8
↓
...
```

This repeated division by two is the reason Binary Search has logarithmic time complexity:

```text
O(log n)
```

## Run the Visualization

From the repository root:

```bash
python algorithms/searching/binary-search/visualize.py
```

To generate or inspect the step-by-step visualization:

```bash
python algorithms/searching/binary-search/visualize_steps.py
```

> The exact output depends on the input array and target configured in the visualization scripts.

## Main Takeaway

Binary Search becomes easier to understand when viewed as a process of **shrinking the search space**, rather than simply comparing numbers.

At every step, approximately half of the remaining candidates can be ignored.
