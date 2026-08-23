[فارسی](./README.fa.md)

# Chapter 2 — Selection Sort

# Chapter 2 — Data Structures and Selection Sort

Chapter 2 changed the way I think about storing a collection of values.

The important question is not only what data I have, but also how that data is arranged and which operations I expect to perform most often.

The chapter begins with arrays and linked lists, compares the way they behave in memory, and eventually uses those ideas to introduce Selection Sort.

---

## Arrays and memory

An array keeps its elements in consecutive positions.

```text
[A][B][C][D][E]
```

That layout makes indexed access efficient. Once the starting location of the array is known, the position of another element can be calculated from its index.

```text
indexed access → O(1)
```

This is why jumping to an arbitrary element of an array is fast.

Array indexes normally start at zero:

```text
Index:  0   1   2   3
Value: 10  20  30  40
```

So `20` is stored at index `1`, not position `2` in programming terms.

---

## The cost of growing an array

The contiguous layout of an array is useful for reading, but it makes growth more complicated.

If an array occupies:

```text
[A][B][C][used]
```

there is no room to place another element directly after `C`.

The program may need another block of memory large enough for the entire collection:

```text
[A][B][C][D][ ][ ][ ]
```

and the existing values may have to be moved there.

One common solution is to reserve more capacity than is currently needed:

```text
size = 3
capacity = 8

[A][B][C][ ][ ][ ][ ][ ]
```

This avoids relocating the array on every insertion.

The downside is that some reserved space can remain unused, and another resize is still required once the capacity is exhausted.

---

# Linked lists

A linked list removes the requirement that all elements live next to each other.

Each node contains a value and a reference to the next node.

```text
[A | next] → [B | next] → [C | None]
```

The nodes themselves may be scattered throughout memory.

What makes them a list is the chain of links connecting them.

---

## Pointers

The link to the next node is stored as a pointer.

A pointer represents a memory address.

For example:

```text
Address 100:
[A | 450]

Address 450:
[B | 820]

Address 820:
[C | None]
```

Following the list means reading one node, finding the address stored inside it, and moving to that location.

This concept becomes especially visible in lower-level languages such as C.

---

# Random and sequential access

The biggest practical difference between arrays and linked lists is the way elements are accessed.

A linked list provides sequential access:

```text
A → B → C → D → E
```

To reach `E`, the earlier nodes must be followed first.

Accessing a position in the list can therefore take:

```text
O(n)
```

An array provides random access.

```python
items[500]
```

can be reached directly without visiting the previous 500 elements.

```text
Array indexed access        → O(1)
Linked-list position access → O(n)
```

This advantage explains a large part of why arrays are so common.

---

# Cache locality

Big O notation does not tell the whole performance story.

Array elements are stored near one another. Modern processors read memory in chunks, so accessing one array element often brings nearby elements into cache as well.

```text
[A][B][C][D][E]
```

This makes sequential traversal efficient.

Linked-list nodes may be located far apart:

```text
[A] --------→ [B] ----------------→ [C]
```

The program must read one node before it even knows where the next node is.

As a result, arrays often have better real-world sequential performance even though traversing both structures is technically `O(n)`.

---

# Insertion

Consider inserting `X` into:

```text
[A][B][C][D]
```

The array needs to become:

```text
[A][B][X][C][D]
```

Elements after the insertion point may need to move.

In the worst case, that means shifting a large part of the array:

```text
array insertion → O(n)
```

A linked list does not need to move its existing nodes.

```text
A → B → C → D
```

can become:

```text
A → B → X → C → D
```

by changing links.

If the insertion point is already known, the link update can be constant time.

Finding that point is a separate operation and may still require a full traversal.

---

# Deletion

Deleting from an array creates a similar problem.

```text
[A][B][C][D]
```

Removing `C` temporarily leaves:

```text
[A][B][ ][D]
```

so later elements need to move.

```text
array deletion → O(n)
```

In a linked list:

```text
A → B → C → D
```

removing `C` can be done by reconnecting `B` directly to `D`.

```text
A → B ─────→ D
```

Again, changing the links is cheap once the required nodes are known. Finding those nodes can still take linear time.

---

# Memory overhead

Neither structure gets memory efficiency for free.

A dynamic array may keep some unused capacity so it can grow without relocating itself immediately.

A linked list uses extra memory in every node because it needs to store a pointer.

```text
Array:
[A][B][C][D]

Linked list:
[A|ptr] [B|ptr] [C|ptr] [D|ptr]
```

If the stored values are small, the pointer overhead can be significant.

The best choice therefore depends on the workload rather than a simple rule that one structure is always better.

---

# Comparing the two structures

| Property | Array | Linked List |
|---|---:|---:|
| Access by position | `O(1)` | `O(n)` |
| Full traversal | `O(n)` | `O(n)` |
| Insert at a known place | Usually `O(n)` | `O(1)` for the link change |
| Delete at a known place | Usually `O(n)` | `O(1)` for the link change |
| Random access | Yes | No |
| Requires contiguous layout | Yes | No |
| Cache locality | Usually good | Usually poor |

Arrays are more common in general-purpose programs because fast indexed access and good memory locality are extremely useful.

Linked lists make sense when their linking behavior matches the operations required by the problem.

---

# What the exercises showed

The exercises were useful because they forced me to choose a structure based on the operations being performed rather than by preference.

An expense tracker with frequent additions and few reads favors insertion behavior.

A restaurant order queue mainly adds items at one end and removes them from the other.

A username list searched with Binary Search needs random access, which makes an array the natural choice.

That same sorted array becomes more expensive to maintain when new usernames are inserted, because the sorted order must be preserved.

The final exercise combined an array with several linked lists:

```text
A → Alice → Adam
B → Bob → Bella
C → Carl → Chris
...
Z → Zara → Zakhir
```

Instead of searching one huge linked list, the first letter narrows the search to a much smaller list.

The main lesson was that data structures do not always have to be used in isolation. Combining them can give a better balance of properties.

---

# Selection Sort

The second algorithm in the book is Selection Sort.

Its idea is straightforward:

1. Find the smallest remaining element.
2. Move it into the sorted result.
3. Repeat until nothing remains.

Starting with:

```text
[5, 3, 6, 2, 10]
```

the result grows like this:

```text
[2]
[2, 3]
[2, 3, 5]
[2, 3, 5, 6]
[2, 3, 5, 6, 10]
```

The algorithm gets its name from repeatedly selecting the smallest remaining value.

---

## Why Selection Sort is O(n²)

Finding the smallest item in an unsorted collection requires scanning the remaining values.

The amount of work looks roughly like:

```text
n
+ (n - 1)
+ (n - 2)
+ ...
+ 2
+ 1
```

The sum is:

```text
n(n + 1) / 2
```

which grows proportionally to:

```text
n²
```

Constant factors do not change the Big O growth rate.

Therefore:

```text
Selection Sort → O(n²)
```

Even though each pass examines fewer elements than the previous one, the total work is still quadratic.

---

## Input order does not save the algorithm

Selection Sort still scans the remaining portion of the collection to find the minimum, even when the input is already sorted.

Its growth rate therefore remains quadratic across the usual cases:

```text
Best case    → O(n²)
Average case → O(n²)
Worst case   → O(n²)
```

---

## A simple implementation

One way to write it is to first locate the smallest value:

```python
def find_smallest(items):
    smallest_index = 0

    for index in range(1, len(items)):
        if items[index] < items[smallest_index]:
            smallest_index = index

    return smallest_index
```

Then repeatedly move that value into another list:

```python
def selection_sort(items):
    remaining = list(items)
    result = []

    while remaining:
        smallest_index = find_smallest(remaining)
        result.append(remaining.pop(smallest_index))

    return result
```

Example:

```python
selection_sort([5, 3, 6, 2, 10])
```

produces:

```text
[2, 3, 5, 6, 10]
```

The input is copied first because removing elements from the working list would otherwise modify the original data.

---

# What I took away from Chapter 2

The most useful idea from this chapter was not Selection Sort itself.

It was the connection between memory layout, data structures, and algorithmic cost.

Arrays make some operations cheap because their elements have predictable positions.

Linked lists trade that direct access for a more flexible linking structure.

Selection Sort then shows how repeated linear work can build into quadratic growth.

```text
Data layout
    ↓
Data structure
    ↓
Cost of operations
    ↓
Algorithm performance
```

That connection is what I want to keep in mind when choosing a structure for future problems.