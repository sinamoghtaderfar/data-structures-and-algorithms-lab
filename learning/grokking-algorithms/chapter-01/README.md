[فارسی](./README.fa.md)

# Chapter 01 — Introduction to Algorithms

These are my notes from Chapter 1 of *Grokking Algorithms*.

This chapter starts with Binary Search, but the bigger lesson is not really about one search algorithm. It introduces a way of thinking about algorithms:

> How does the amount of work grow as the input becomes larger?

That question leads to some of the foundations I will use throughout the rest of this repository:

- Binary Search
- Simple Search
- logarithms
- running time
- Big O notation
- growth rates
- worst-case analysis
- common complexity classes
- factorial growth and the Traveling Salesperson Problem

The goal of this chapter is not to memorize complexity notation.

It is to start recognizing why two algorithms that solve the same problem can behave very differently as the amount of data grows.

---

## 1. Binary Search

Binary Search is an efficient algorithm for finding a target in a **sorted collection**.

Suppose I have:

```text
[5, 10, 15, 20, 25, 30, 35]
```

and I want to find:

```text
25
```

Instead of checking:

```text
5 → 10 → 15 → 20 → 25
```

Binary Search starts from the middle:

```text
[5, 10, 15, 20, 25, 30, 35]
            ↑
           20
```

Since:

```text
25 > 20
```

everything on the left can be ignored.

The remaining search space is:

```text
[25, 30, 35]
```

The next middle value is:

```text
30
```

Since:

```text
25 < 30
```

the right side can be discarded.

That leaves:

```text
25
```

and the target is found.

The important idea is:

> Binary Search does not become fast by making comparisons faster.  
> It becomes fast by eliminating a large part of the remaining search space after every comparison.

---

## 2. Why the Data Must Be Sorted

Binary Search depends on ordering.

This works:

```text
[2, 5, 8, 12, 17, 21, 30]
```

This does not:

```text
[21, 5, 30, 2, 17, 8, 12]
```

Why?

Suppose the middle value is smaller than the target.

With sorted data, I know that everything before the middle is also too small.

That lets me safely discard half of the data.

Without sorting, that conclusion is no longer valid.

So the requirement is not just a technical detail:

> **The ordering of the data is what makes elimination possible.**

---

## 3. Tracking the Search Range

The iterative Binary Search implementation keeps track of the current search space using:

```python
low = 0
high = len(arr) - 1
```

At the beginning:

```text
low                              high
 ↓                                 ↓

[5, 10, 15, 20, 25, 30, 35]
```

The middle index is calculated with:

```python
mid = (low + high) // 2
```

and the value is:

```python
guess = arr[mid]
```

Now there are three possibilities.

### The target was found

```python
if guess == target:
    return mid
```

### The guess is too high

```python
high = mid - 1
```

The right side is discarded.

### The guess is too low

```python
low = mid + 1
```

The left side is discarded.

The search continues while:

```python
low <= high
```

If eventually:

```text
low > high
```

the search range is empty and the target does not exist.

---

## 4. Python Implementation

The basic implementation looks like this:

```python
def binary_search(arr, target):
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
```

Example:

```python
numbers = [5, 10, 15, 20, 25, 30, 35]

result = binary_search(numbers, 25)

print(result)
```

Output:

```text
4
```

because Python indexes begin at zero:

```text
Index:  0   1   2   3   4   5   6
Value:  5  10  15  20  25  30  35
                       ↑
```

The maintained implementation, tests, and visualization live outside these learning notes:

[Binary Search implementation and documentation](../../../algorithms/searching/binary-search/README.md)

---

## 5. Simple Search vs Binary Search

Simple Search checks values sequentially.

```text
1 → 2 → 3 → 4 → 5 → ...
```

For `n` elements, it may need to inspect all `n` elements.

So its worst-case running time grows as:

```text
O(n)
```

Binary Search behaves differently.

Consider 128 possible values:

```text
128
 ↓
64
 ↓
32
 ↓
16
 ↓
8
 ↓
4
 ↓
2
 ↓
1
```

Only seven halvings are needed.

So:

```text
Simple Search  → O(n)
Binary Search  → O(log n)
```

This difference becomes much more important as `n` grows.

---

## 6. Understanding Logarithms

A logarithm reverses exponentiation.

For example:

```text
2³ = 8
```

therefore:

```text
log₂(8) = 3
```

Similarly:

```text
2¹⁰ = 1024
```

so:

```text
log₂(1024) = 10
```

For Binary Search, a useful way to think about `log₂(n)` is:

> How many times can I divide the remaining possibilities by two before only one remains?

For example:

```text
16
↓
8
↓
4
↓
2
↓
1
```

That takes four halvings:

```text
log₂(16) = 4
```

This is why logarithms naturally appear when analyzing Binary Search.

---

## 7. Running Time Is About Growth

When comparing algorithms, measuring one execution in milliseconds does not tell the whole story.

A more useful question is:

> What happens when the input becomes much larger?

Consider:

| Input size | Simple Search | Binary Search |
|---:|---:|---:|
| 100 | up to 100 checks | ~7 checks |
| 1,000 | up to 1,000 | ~10 |
| 1,000,000 | up to 1,000,000 | ~20 |
| 1,000,000,000 | up to 1,000,000,000 | ~30 |

For small inputs, performance differences may not look dramatic.

For large inputs, the growth rate becomes much more important.

That is the perspective Big O helps describe.

---

## 8. Big O Notation

Big O describes how the amount of work performed by an algorithm grows as the input size increases.

It does **not** tell me:

```text
This algorithm takes exactly 0.25 seconds.
```

Instead, it tells me something like:

```text
If the input becomes much larger,
how quickly does the required work grow?
```

For Simple Search:

```text
n items
→ potentially n checks
→ O(n)
```

For Binary Search:

```text
n items
→ roughly log₂(n) checks
→ O(log n)
```

So:

```text
Simple Search
O(n)

Binary Search
O(log n)
```

Big O is therefore much more useful for reasoning about scalability than a single timing measurement.

---

## 9. Growth Rates

Some common complexity classes are:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n!)
```

They do not grow at the same speed.

### `O(1)` — Constant

The amount of work does not grow with `n` in the usual model.

Example:

```python
value = arr[5]
```

---

### `O(log n)` — Logarithmic

The problem becomes dramatically smaller after each step.

Example:

```text
Binary Search
```

---

### `O(n)` — Linear

The amount of work grows roughly in proportion to the input size.

Example:

```text
Simple Search
```

---

### `O(n log n)`

This complexity appears in efficient comparison-based sorting algorithms such as Merge Sort and average-case Quick Sort.

It grows faster than linear time but much more slowly than quadratic time for large inputs.

---

### `O(n²)` — Quadratic

The amount of work can grow roughly with the square of the input.

For example:

```text
n = 10
n² = 100

n = 1,000
n² = 1,000,000
```

Algorithms involving nested work over the same input often appear in this area.

Selection Sort, introduced later in the book, has `O(n²)` time complexity.

---

### `O(n!)` — Factorial

Factorial growth becomes enormous very quickly.

```text
5!  = 120
6!  = 720
7!  = 5,040
8!  = 40,320
10! = 3,628,800
```

This is a completely different scale of growth.

---

## 10. Worst-Case Analysis

An algorithm can behave differently depending on the input.

Suppose Simple Search looks for a value in:

```text
[5, 10, 15, 20, 25]
```

If the target is:

```text
5
```

it is found immediately.

That is a best-case situation.

But if the target is:

```text
25
```

or does not exist, many or all elements may need to be checked.

Big O in this chapter mainly focuses on how the algorithm behaves as the input grows, commonly using the worst-case upper-bound perspective.

For Simple Search:

```text
O(n)
```

For Binary Search:

```text
O(log n)
```

Even Binary Search has a best case of:

```text
O(1)
```

when the target happens to be the first middle element.

But its worst-case growth remains:

```text
O(log n)
```

---

## 11. Why Constant Factors Are Usually Ignored

Suppose one algorithm performs roughly:

```text
n
```

operations and another performs:

```text
2n
```

Both are still classified as:

```text
O(n)
```

Big O focuses primarily on how the work grows, not on constant multipliers.

This does **not** mean constants never matter in real software.

They absolutely can.

But when studying algorithmic growth, the difference between:

```text
O(n)
```

and:

```text
O(n²)
```

eventually matters much more than a fixed multiplier.

---

## 12. The Traveling Salesperson Example

The Traveling Salesperson Problem asks for a shortest route that visits a collection of cities and returns to the starting point.

One naive brute-force approach is:

1. generate possible city orders;
2. calculate the distance of each route;
3. compare the routes;
4. keep the shortest.

The number of possible orderings grows factorially.

For example:

```text
5! = 120
6! = 720
7! = 5,040
8! = 40,320
```

A brute-force enumeration of permutations therefore has factorial-scale growth:

```text
O(n!)
```

The important lesson here is not that every possible algorithm for TSP literally runs in `O(n!)`.

The lesson is that **brute-force enumeration of every ordering explodes extremely quickly**.

This is my first clear example of how some problems become computationally difficult even when `n` does not look very large.

---

## 13. Exercises

### Exercise 1.1

A sorted list contains 128 names.

Maximum Binary Search steps:

```text
log₂(128) = 7
```

Answer:

```text
7
```

---

### Exercise 1.2

Now the list contains 256 names.

```text
log₂(256) = 8
```

Answer:

```text
8
```

So doubling the input from:

```text
128 → 256
```

adds only one additional Binary Search step.

That is a useful intuition for logarithmic growth.

---

### Exercise 1.3

Find someone's phone number when their name is known and the phone book is sorted by name.

Binary Search can be used:

```text
O(log n)
```

---

### Exercise 1.4

Find someone's name when only the phone number is known, while the phone book is not sorted by phone number.

In the basic model, the entries may need to be scanned:

```text
O(n)
```

---

### Exercise 1.5

Read every person's phone number.

Every entry must be visited:

```text
O(n)
```

---

### Exercise 1.6

Read the phone numbers of all people whose names begin with `A`.

In the simplified analysis used in the chapter, this is treated as linear work:

```text
O(n)
```

The broader lesson is that Big O describes the growth class and ignores constant factors.

Later, with different data structures or more precise assumptions about how the data is organized, the analysis of similar queries can become more nuanced.

---

## 14. Testing Binary Search

Understanding the idea is not enough.

The implementation also needs to behave correctly around its boundaries.

Useful tests include:

- target exists;
- first element;
- last element;
- target does not exist;
- empty collection;
- single-element collection;
- missing target in a single-element collection.

Example:

```python
def test_target_exists():
    arr = [5, 10, 15, 20, 25, 30, 35]

    result = binary_search(arr, 25)

    assert result == 4
```

The actual tests for this repository live here:

[Binary Search tests](../../../algorithms/searching/binary-search/test_binary_search.py)

Testing is useful because an algorithm can look correct on the normal case while still failing at its boundaries.

---

## 15. Visualization

Binary Search is particularly useful to visualize because its search space changes after every comparison.

The three important positions are:

```text
LOW
MID
HIGH
```

For example:

```text
[5, 10, 15, 20, 25, 30, 35]
 ↑          ↑              ↑
LOW        MID            HIGH
```

After comparing the middle value with the target, either `low` or `high` moves.

The remaining search range becomes smaller.

That makes the central idea visible:

> Every comparison should remove a part of the search space that can no longer contain the answer.

The visualization for the maintained implementation is documented here:

[Binary Search Visualization](../../../algorithms/searching/binary-search/VISUALIZATION.md)

---

## 16. From Exact Search to Boundary Search

After implementing normal Binary Search, I used the same core idea for a slightly more interesting problem.

Instead of asking:

> Where is this exact value?

the challenge asks:

> Where is the first value that is equal to or greater than the target?

For example, with sorted server logs:

```text
10:00:01
10:02:15
10:05:40
10:08:12
10:08:48
10:12:33
```

and:

```text
target = 10:08:15
```

the answer is:

```text
10:08:48
```

This is a **boundary-search / lower-bound** variation of Binary Search.

It helped me understand that Binary Search is not just one fixed function.

The deeper technique is using sorted data to repeatedly eliminate impossible regions.

[View the Binary Search Challenge](../../../challenges/binary-search/README.md)

---

## 17. Learning Workflow

The workflow I am using in this repository is:

```text
Understand
    ↓
Implement
    ↓
Test
    ↓
Visualize
    ↓
Benchmark when useful
    ↓
Apply
```

### Understand

Build the mental model first.

### Implement

Write the algorithm myself instead of only reading it.

### Test

Check normal cases and edge cases.

### Visualize

Use visualization when seeing the state changes makes the concept easier to understand.

### Benchmark

Measure behavior when performance comparisons actually add something useful.

### Apply

Use the idea in a problem that is slightly different from the textbook example.

The last step matters because being able to reproduce an algorithm is not the same as being able to recognize when to use it.

---

## 18. What I Learned

After Chapter 1, these are the ideas I want to keep:

- Binary Search requires sorted data.
- Its power comes from eliminating roughly half of the remaining search space.
- Binary Search has `O(log n)` worst-case time complexity.
- Simple Search has `O(n)` worst-case time complexity.
- Logarithms explain repeated halving.
- Big O describes growth, not exact execution time.
- Small benchmark differences can hide huge scalability differences.
- Best-case and worst-case behavior can be different.
- Constant factors are usually ignored when describing Big O growth classes.
- `O(log n)`, `O(n)`, `O(n log n)`, `O(n²)`, and `O(n!)` scale very differently.
- Brute-force permutation search becomes impractical very quickly.
- Binary Search is a technique that can be adapted to boundary-search problems, not just exact lookup.

---

## Related Project Files

The concepts from this chapter are implemented, tested, visualized, and applied elsewhere in the repository.

### Binary Search

- [Algorithm Overview](../../../algorithms/searching/binary-search/README.md)
- [Implementation](../../../algorithms/searching/binary-search/binary_search.py)
- [Tests](../../../algorithms/searching/binary-search/test_binary_search.py)
- [Visualization Documentation](../../../algorithms/searching/binary-search/VISUALIZATION.md)

### Visualization Output

![Binary Search Step 1](../../../algorithms/searching/binary-search/assets/step_1.png)

![Binary Search Step 2](../../../algorithms/searching/binary-search/assets/step_2.png)

![Binary Search Step 3](../../../algorithms/searching/binary-search/assets/step_3.png)

### Practical Challenge

- [Server Log Boundary Search](../../../challenges/binary-search/README.md)

---

## Key Takeaway

The most important thing I learned from this chapter is not the exact Python implementation of Binary Search.

It is this:

> **Algorithm design is about how intelligently I can reduce the amount of work required to solve a problem.**

Binary Search is a simple example, but it introduces an idea that will appear again and again:

**Do not process information that you can prove you no longer need.**