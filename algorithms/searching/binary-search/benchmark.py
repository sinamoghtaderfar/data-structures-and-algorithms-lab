"""
Benchmark Linear Search against Binary Search.

This benchmark compares the two algorithms in two ways:

1. Number of comparisons
2. Actual runtime

The target is intentionally placed outside the search range so that
both algorithms are measured in a worst-case unsuccessful search.
"""

import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from binary_search import binary_search


# Input sizes used for the benchmark.
# range() is used instead of list() so large inputs do not consume
# unnecessary amounts of memory.
SIZES = [
    1_000,
    10_000,
    100_000,
    500_000,
    # 1_000_000,
    # 10_000_000,
]


def linear_search(array, target):
    """Search for a target by checking each element from left to right."""

    for index, value in enumerate(array):
        if value == target:
            return index

    return None


def linear_search_steps(array, target):
    """Count how many comparisons Linear Search performs."""

    count = 0

    for value in array:
        count += 1

        if value == target:
            return count

    return count


def binary_search_steps(array, target):
    """Count how many comparisons Binary Search performs."""

    low = 0
    high = len(array) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        count += 1

        if guess == target:
            return count

        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return count


def calibrate_iterations(func, array, target, min_time_ns=50_000_000):
    """
    Find a suitable number of iterations for timing.

    Very fast functions such as Binary Search can finish in only a few
    microseconds. Timing a single execution would therefore be noisy.

    The number of executions is doubled until the total runtime reaches
    at least 50 milliseconds.
    """

    iterations = 1

    while True:
        start = time.perf_counter_ns()

        for _ in range(iterations):
            func(array, target)

        end = time.perf_counter_ns()

        elapsed = end - start

        if elapsed >= min_time_ns:
            return iterations

        iterations *= 2


def measure_runtime(func, array, target, repeat=7):
    """
    Measure the median runtime of one function call.

    Each measurement runs the function multiple times using the number
    of iterations found during calibration. The total time is then
    divided by the number of executions.

    Taking the median of several measurements helps reduce the effect
    of occasional system noise.
    """

    times = []

    iterations = calibrate_iterations(
        func,
        array,
        target,
    )

    # Run once before measuring so the first execution does not
    # influence the benchmark as much.
    func(array, target)

    for _ in range(repeat):
        start = time.perf_counter_ns()

        for _ in range(iterations):
            func(array, target)

        end = time.perf_counter_ns()

        elapsed = end - start
        time_per_run = elapsed / iterations

        times.append(time_per_run)

    return statistics.median(times)


def run_benchmarks():
    """Run comparison-count and runtime benchmarks for every input size."""

    results = []

    for size in SIZES:
        # The values are already sorted, which is required by Binary Search.
        array = range(size)

        # range(size) contains values from 0 to size - 1.
        # Using size as the target guarantees an unsuccessful search,
        # giving us a useful worst-case scenario.
        target = size

        linear_comparisons = linear_search_steps(array, target)
        binary_comparisons = binary_search_steps(array, target)

        linear_runtime = measure_runtime(
            linear_search,
            array,
            target,
        )

        binary_runtime = measure_runtime(
            binary_search,
            array,
            target,
        )

        result = {
            "size": size,
            "linear_comparisons": linear_comparisons,
            "binary_comparisons": binary_comparisons,
            "linear_runtime_ns": linear_runtime,
            "binary_runtime_ns": binary_runtime,
        }

        results.append(result)

        print(f"Input size: {size:,}")
        print(f"Linear comparisons: {linear_comparisons:,}")
        print(f"Binary comparisons: {binary_comparisons:,}")
        print(f"Linear runtime: {linear_runtime:.2f} ns")
        print(f"Binary runtime: {binary_runtime:.2f} ns")
        print()

    return results


def plot_comparisons(results, assets_dir):
    """Create a chart comparing the number of comparisons."""

    input_sizes = [
        result["size"]
        for result in results
    ]

    linear_comparisons = [
        result["linear_comparisons"]
        for result in results
    ]

    binary_comparisons = [
        result["binary_comparisons"]
        for result in results
    ]

    plt.figure(figsize=(10, 6))

    plt.plot(
        input_sizes,
        linear_comparisons,
        marker="o",
        label="Linear Search",
    )

    plt.plot(
        input_sizes,
        binary_comparisons,
        marker="o",
        label="Binary Search",
    )

    plt.xlabel("Input Size")
    plt.ylabel("Number of Comparisons")
    plt.title("Linear Search vs Binary Search - Comparisons")

    # Logarithmic scales make the very different growth rates
    # easier to see on the same chart.
    plt.xscale("log")
    plt.yscale("log")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        assets_dir / "benchmark_comparisons.png",
        dpi=200,
        bbox_inches="tight",
    )

    plt.show()
    plt.close()


def plot_runtime(results, assets_dir):
    """Create a chart comparing median execution time."""

    input_sizes = [
        result["size"]
        for result in results
    ]

    # Convert nanoseconds to microseconds so the chart is easier to read.
    linear_runtimes_us = [
        result["linear_runtime_ns"] / 1_000
        for result in results
    ]

    binary_runtimes_us = [
        result["binary_runtime_ns"] / 1_000
        for result in results
    ]

    plt.figure(figsize=(10, 6))

    plt.plot(
        input_sizes,
        linear_runtimes_us,
        marker="o",
        label="Linear Search",
    )

    plt.plot(
        input_sizes,
        binary_runtimes_us,
        marker="o",
        label="Binary Search",
    )

    plt.xlabel("Input Size")
    plt.ylabel("Median Runtime (µs)")
    plt.title("Linear Search vs Binary Search - Runtime")

    plt.xscale("log")
    plt.yscale("log")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        assets_dir / "benchmark_runtime.png",
        dpi=200,
        bbox_inches="tight",
    )

    plt.show()
    plt.close()


def main():
    """Run the benchmark and generate its visualizations."""

    assets_dir = Path(__file__).resolve().parent / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    results = run_benchmarks()

    plot_comparisons(results, assets_dir)
    plot_runtime(results, assets_dir)


if __name__ == "__main__":
    main()