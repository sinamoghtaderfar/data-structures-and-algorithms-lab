# Binary Search Benchmark

[فارسی](./BENCHMARK.fa.md)

This benchmark explores the practical difference between **Linear Search** and **Binary Search**.

The purpose was not only to repeat the theoretical complexities:

```text
Linear Search  -> O(n)
Binary Search  -> O(log n)
```

but to observe how those differences appear when the algorithms are actually executed.

Two things are measured:

1. the number of comparisons performed by each algorithm;
2. the actual execution time on the machine running the benchmark.

---

## Benchmark Scenario

For every input size, the search space is created using:

```python
array = range(size)
```

and the target is:

```python
target = size
```

Since `range(size)` contains values from `0` to `size - 1`, the target does not exist.

For example:

```python
array = range(1000)
target = 1000
```

This intentionally creates an **unsuccessful worst-case search**.

Linear Search has to inspect every element before it can conclude that the target is missing.

Binary Search repeatedly reduces the remaining search range by approximately half.

Using the same scenario for both algorithms makes their growth easier to compare.

---

## Why `range()` Instead of a List?

An earlier version of the experiment used:

```python
list(range(size))
```

This worked for smaller inputs, but very large lists consumed a significant amount of memory.

For example, creating tens or hundreds of millions of Python integers can require several gigabytes of RAM.

For this benchmark, storing all of those integers is unnecessary.

Python's `range()` supports everything needed here:

```python
len(array)
array[index]
iteration
```

while representing the sequence much more efficiently.

So the benchmark uses:

```python
range(size)
```

instead of materializing a large list.

---

## Comparison Count

The first part of the benchmark ignores execution time completely and counts how many values each algorithm examines.

A typical run produces results similar to:

| Input Size | Linear Search | Binary Search |
| ---------: | ------------: | ------------: |
|      1,000 |         1,000 |            10 |
|     10,000 |        10,000 |            14 |
|    100,000 |       100,000 |            17 |
|    500,000 |       500,000 |            19 |

The difference becomes large very quickly.

With Linear Search, increasing the input size directly increases the number of comparisons.

With Binary Search, even a large increase in input size only adds a few additional search steps.

For example:

```text
1,000 elements
Binary Search -> 10 comparisons

500,000 elements
Binary Search -> 19 comparisons
```

The input became 500 times larger, but Binary Search required only 9 additional comparisons.

This is the practical behavior behind:

```text
O(log n)
```

### Comparison Visualization

![Linear Search vs Binary Search comparisons](./assets/benchmark_comparisons.png)

Both axes use logarithmic scales so the very different growth rates can be displayed clearly on the same graph.

The Linear Search line follows the growth of the input, while the Binary Search line grows much more slowly.

---

## Runtime Measurement

Counting comparisons shows the algorithmic behavior directly, but I also wanted to see what happens when the algorithms run in Python.

Runtime is measured using:

```python
time.perf_counter_ns()
```

which provides a high-resolution timer suitable for short measurements.

However, measuring a very fast operation introduced another problem.

A Binary Search in this experiment can finish in only a few microseconds.

Timing a single call produced noticeably unstable values because the measurement could be affected by things unrelated to the algorithm itself, such as:

* operating system scheduling;
* interpreter overhead;
* CPU state;
* background processes;
* timer noise.

So the runtime benchmark needed a little more care.

---

## Warm-Up

Before collecting timing samples, the function is executed once without recording its runtime.

```python
func(array, target)
```

This warm-up prevents the first execution from having an unnecessarily large influence on the measurements.

It does not remove all runtime noise, but it makes the experiment more representative of repeated execution.

---

## Automatic Calibration

Timing Binary Search once is too short to produce a stable measurement.

Instead of choosing an arbitrary number such as "run everything 1,000 times", the benchmark automatically determines how many executions are needed.

It starts with:

```text
1
```

execution and repeatedly doubles the number:

```text
1
2
4
8
16
32
64
...
```

until the total measurement takes at least approximately:

```text
50 ms
```

For a slow operation, only a few executions may be required.

For a very fast operation such as Binary Search, thousands of executions may be used.

This means the benchmark adapts to the speed of the function being tested.

---

## Time Per Search

After calibration, the function is executed multiple times inside one timed block.

Conceptually:

```text
start timer

run search N times

stop timer
```

The total elapsed time is then divided by `N`:

```text
time per search =
total elapsed time / number of executions
```

This is more reliable than measuring one extremely short function call directly.

---

## Repeated Measurements and Median

Each calibrated measurement is repeated several times.

The benchmark currently uses:

```python
repeat = 7
```

Instead of using only one result, the median is calculated:

```python
statistics.median(times)
```

The median is useful because an occasional slow measurement caused by the operating system or another process has less influence on the final result.

---

## Runtime Results

The exact values change between runs and between machines, which is expected.

One run of the benchmark produced results in roughly this range:

| Input Size |        Linear Search | Binary Search |
| ---------: | -------------------: | ------------: |
|      1,000 |            ~50-60 µs |         ~2 µs |
|     10,000 |        ~500-1,000 µs |       ~2-3 µs |
|    100,000 |            ~5,000 µs |         ~3 µs |
|    500,000 | tens of milliseconds |       ~3-4 µs |

The exact numbers are less important than the overall behavior.

Linear Search becomes increasingly expensive as the collection grows.

Binary Search remains very fast because the number of operations increases logarithmically.

### Runtime Visualization

![Linear Search vs Binary Search runtime](./assets/benchmark_runtime.png)

The graph uses logarithmic scales for both axes.

This makes it possible to display runtimes that differ by several orders of magnitude without completely hiding the Binary Search measurements near the bottom of the chart.

---

## Runtime vs Algorithmic Complexity

The two graphs represent different things.

The comparison-count graph describes the algorithms themselves more directly:

```text
Linear Search  -> O(n)
Binary Search  -> O(log n)
```

The runtime graph is an **empirical measurement**.

Runtime depends on the environment, including:

```text
CPU
Python version
operating system
machine load
interpreter overhead
```

For that reason, the benchmark should not be interpreted as saying that Binary Search will always take a specific number of microseconds.

The important observation is how each algorithm scales as the input grows.

---

## Why Sorting Is Not Included

Binary Search requires sorted input.

This benchmark assumes that the data is **already sorted**, so sorting time is deliberately excluded.

The experiment is answering this question:

> Given an already sorted collection, how does Linear Search compare with Binary Search for lookup?

A different experiment would be required to answer:

> Is sorting the data first and then using Binary Search worthwhile for a particular workload?

That would depend on factors such as the number of searches being performed.

---

## What I Learned

This benchmark made the difference between `O(n)` and `O(log n)` much more concrete.

Reading that Binary Search can search around one billion values in roughly 30 comparisons sounds impressive, but seeing the comparison count grow from:

```text
10
14
17
19
```

while Linear Search grows from:

```text
1,000
10,000
100,000
500,000
```

made the difference much easier to understand.

I also learned that benchmarking is not just about placing a timer before and after a function.

For very fast operations, measurement itself becomes part of the problem.

During this experiment I had to think about:

* worst-case inputs;
* memory usage;
* high-resolution timers;
* runtime noise;
* warm-up runs;
* repeated measurements;
* median values;
* automatic calibration;
* logarithmic visualization.

The algorithm was simple.

Measuring it carefully was a separate problem.

That was probably the most useful part of this experiment.

---

## Running the Benchmark

From the repository root:

```bash
python algorithms/searching/binary-search/benchmark.py
```

The benchmark prints the comparison counts and runtime measurements and generates:

```text
assets/
├── benchmark_comparisons.png
└── benchmark_runtime.png
```

---

## Related Files

* [Binary Search implementation](./binary_search.py)
* [Binary Search tests](./test_binary_search.py)
* [Benchmark source](./benchmark.py)
* [Visualization documentation](./VISUALIZATION.md)
