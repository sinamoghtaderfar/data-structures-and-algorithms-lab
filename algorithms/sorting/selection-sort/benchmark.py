import random
import time
from pathlib import Path

import matplotlib.pyplot as plt
from selection_sort import selection_sort

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)


sizes = [200, 400, 800, 1600]

times = []

for size in sizes:
    numbers = [
        random.randint(0, 100_000)
        for _ in range(size)
    ]

    start = time.perf_counter()

    selection_sort(numbers)

    end = time.perf_counter()

    elapsed = end - start
    times.append(elapsed)

    print(
        f"Size: {size:<5} "
        f"Time: {elapsed:.6f} seconds"
    )


plt.figure(figsize=(8, 5))

plt.plot(
    sizes,
    times,
    marker="o"
)

plt.title("Selection Sort Benchmark")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")

plt.grid()

plt.tight_layout()

output_path = ASSETS_DIR / "selection_sort_benchmark.png"

plt.savefig(
    output_path,
    dpi=150,
    bbox_inches="tight"
)

plt.show()

print(f"Saved: {output_path}")