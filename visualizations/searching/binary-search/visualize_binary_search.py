from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt


def gui_available():
    """
    Returns True if Matplotlib has a GUI backend available.
    """
    backend = matplotlib.get_backend().lower()

    non_gui_backends = {
        "agg",
        "pdf",
        "svg",
        "ps",
        "cairo",
        "template",
    }

    return backend not in non_gui_backends


def visualize_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    step = 1

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    has_gui = gui_available()

    print(f"Matplotlib backend: {matplotlib.get_backend()}")

    if has_gui:
        print("GUI available → charts will be displayed.")
        plt.ion()
    else:
        print("No GUI available → images will only be saved.")

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        # Create figure
        fig, ax = plt.subplots(figsize=(10, 3))

        # Draw array
        for i, value in enumerate(arr):
            ax.scatter(i, 0, s=800)

            ax.text(
                i,
                0,
                str(value),
                ha="center",
                va="center",
            )

        # Current search range
        ax.axvspan(
            low - 0.5,
            high + 0.5,
            alpha=0.15,
        )

        # LOW / MID / HIGH
        ax.text(
            low,
            -0.25,
            "LOW",
            ha="center",
        )

        ax.text(
            mid,
            0.25,
            "MID",
            ha="center",
        )

        ax.text(
            high,
            -0.25,
            "HIGH",
            ha="center",
        )

        # Status
        if guess == target:
            status = f"FOUND at index {mid}"

        elif guess > target:
            status = "Guess too high → search left"

        else:
            status = "Guess too low → search right"

        ax.set_title(
            f"Binary Search - Step {step}\n"
            f"Target: {target} | Guess: {guess} | {status}"
        )

        ax.set_xlim(-1, len(arr))
        ax.set_ylim(-1, 1)

        ax.set_xticks(range(len(arr)))
        ax.set_yticks([])

        ax.set_xlabel("Array Index")

        # Save PNG
        filename = output_dir / f"step_{step}.png"

        fig.savefig(
            filename,
            bbox_inches="tight",
        )

        print(f"Saved: {filename}")

        # Show chart if GUI exists
        if has_gui:
            plt.show(block=False)
            plt.pause(1.5)

        plt.close(fig)

        # Binary Search logic
        if guess == target:
            print(
                f"Target {target} found at index {mid}"
            )

            if has_gui:
                plt.ioff()

            return mid

        elif guess > target:
            high = mid - 1

        else:
            low = mid + 1

        step += 1

    print(f"Target {target} was not found.")

    if has_gui:
        plt.ioff()

    return None


if __name__ == "__main__":
    arr = [5, 10, 15, 20, 25, 30, 35]

    visualize_binary_search(arr, 25)