# Arrays

[نسخه فارسی](README.fa.md)

This folder contains a small exploration of Python lists while studying arrays.

I did not reimplement an array from scratch here. Instead, I used Python's built-in `list` to observe how a dynamic array behaves in practice, especially how its memory usage changes as new elements are appended.

## Array basics

An array stores elements in an ordered sequence and supports direct access by index.

For example:

```python
numbers = [10, 20, 30, 40]

print(numbers[2])
```

Output:

```text
30
```

Accessing an element by index is generally:

```text
O(1)
```

because the location of the element can be calculated directly.

## Python lists as dynamic arrays

Python's `list` behaves like a dynamic array.

Unlike a fixed-size array, it can grow when new elements are appended.

That growth does not happen by allocating space for exactly one new element every time. Python usually reserves some extra capacity so that several future appends can happen without resizing again.

## Size and capacity

Two ideas are useful here:

```text
size     = number of elements currently stored
capacity = amount of space currently reserved
```

They are not always the same.

A list may contain only a few elements while already having extra reserved space for future growth.

## Memory experiment

The exploration script uses:

```python
sys.getsizeof(numbers)
```

to inspect the size of the list object as values are appended.

One run produced this pattern:

```text
Empty list memory: 56

Length 1  → 88
Length 2  → 88
Length 3  → 88
Length 4  → 88

Length 5  → 120

Length 6  → 120
Length 7  → 120
Length 8  → 120

Length 9  → 184

...

Length 17 → 248
```

The important part is the step-like growth.

The memory size does not increase after every single append. It stays unchanged for a while, then jumps when the current capacity is no longer enough.

## What `sys.getsizeof()` shows

`sys.getsizeof()` reports the size of the list structure itself.

It does not represent the total memory used by every object referenced by the list.

Conceptually, a Python list stores references:

```text
list

┌─────┬─────┬─────┐
│ ref │ ref │ ref │
└──┬──┴──┬──┴──┬──┘
   ↓     ↓     ↓
   10    20    30
```

The referenced Python objects are separate from the list's internal storage.

## Why append is usually fast

Because Python reserves extra capacity, most calls to:

```python
numbers.append(value)
```

do not require a resize.

Occasionally the list has to allocate a larger block and move its references, which is more expensive.

Across many appends, this gives an amortized time complexity of:

```text
O(1)
```

## Common operation costs

| Operation | Typical complexity |
| --- | --- |
| Access by index | `O(1)` |
| Append | `O(1)` amortized |
| Search by value | `O(n)` |
| Insert in the middle | `O(n)` |
| Delete from the middle | `O(n)` |

Insertion and deletion in the middle are usually linear because later elements may need to be shifted.

## Exploration file

The experiment is in:

```text
explore_python_list.py
```

It prints the list length and memory size after each append so the capacity growth can be observed directly.

## What I learned

The main thing I wanted to see was the difference between the number of elements in a list and the amount of memory reserved for it.

Seeing the memory grow in steps made dynamic arrays easier to understand. Python does not resize the list for every append, which explains why repeated appends are efficient on average.

This also made the trade-off with linked lists clearer: arrays are strong at direct indexed access and cache-friendly traversal, while insertion or deletion in the middle can require shifting many elements.
