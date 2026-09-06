from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from visualize_steps import selection_sort_steps

# Paths
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
FRAMES_DIR = ASSETS_DIR / "frames"

# Create folders automatically
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
FRAMES_DIR.mkdir(parents=True, exist_ok=True)


numbers = [5, 3, 6, 2, 10]

steps = selection_sort_steps(numbers)

# Add the original state as step 0
all_steps = [
    {
        "picked": None,
        "sorted": [],
        "remaining": list(numbers),
    }
] + steps


def draw_step(ax, step, step_number):
    """Draw one step of selection sort."""

    sorted_part = step["sorted"]
    remaining_part = step["remaining"]

    current = sorted_part + remaining_part

    ax.clear()

    ax.bar(range(len(current)), current)

    if step_number == 0:
        ax.set_title("Selection Sort - Start")
    else:
        ax.set_title(
            f"Step {step_number} - Picked: {step['picked']}"
        )

    ax.set_xlabel("Position")
    ax.set_ylabel("Value")

    ax.set_xticks(range(len(current)))
    ax.set_xticklabels(current)

    ax.set_ylim(0, max(numbers) + 2)

    # Show where the sorted part ends
    if sorted_part and len(sorted_part) < len(current):
        ax.axvline(
            len(sorted_part) - 0.5,
            linestyle="--"
        )

    if sorted_part:
        ax.text(
            0,
            max(numbers) + 1,
            f"Sorted: {sorted_part}"
        )

    if remaining_part:
        ax.text(
            len(sorted_part),
            max(numbers) + 1,
            f"Remaining: {remaining_part}"
        )


# Save every step as PNG
for step_number, step in enumerate(all_steps):
    fig, ax = plt.subplots(figsize=(8, 5))

    draw_step(ax, step, step_number)

    fig.tight_layout()

    frame_path = (
        FRAMES_DIR
        / f"selection_sort_step_{step_number:02d}.png"
    )

    fig.savefig(
        frame_path,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Saved: {frame_path}")


# Save final state separately
fig, ax = plt.subplots(figsize=(8, 5))

draw_step(
    ax,
    all_steps[-1],
    len(all_steps) - 1
)

fig.tight_layout()

final_path = ASSETS_DIR / "selection_sort_final.png"

fig.savefig(
    final_path,
    dpi=150,
    bbox_inches="tight"
)

plt.close(fig)

print(f"Saved: {final_path}")


# Create GIF
fig, ax = plt.subplots(figsize=(8, 5))


def update(frame_number):
    draw_step(
        ax,
        all_steps[frame_number],
        frame_number
    )


animation = FuncAnimation(
    fig,
    update,
    frames=len(all_steps),
    interval=1200,
    repeat=True
)

gif_path = ASSETS_DIR / "selection_sort.gif"

animation.save(
    gif_path,
    writer=PillowWriter(fps=1)
)

plt.close(fig)

print(f"Saved GIF: {gif_path}")