[فارسی](./README.fa.md)

# Data Structures & Algorithms Lab

This repository is my personal workspace for studying and practicing **Data Structures and Algorithms**.

I created it to keep what I learn from different books and resources organized in one place, while connecting the concepts I study with implementation, testing, and practice.

Learning material is kept separate from the main implementations. This allows me to study the same concept from different books while keeping the code organized by topic.

---

## How I Study

My general learning process is:

```text
Learn
  ↓
Implement
  ↓
Test
  ↓
Explore
  ↓
Apply
```

I start by studying the concept and its time and space complexity, then implement it in Python and test its behavior.

When useful, I use visualizations or benchmarks to explore the concept further, and challenges to practice applying it to different problems.

---

## Repository Structure

```text
.
├── algorithms/
├── data-structures/
├── challenges/
├── learning/
├── README.md
├── README.fa.md
├── requirements.txt
├── SOURCES.md
└── LICENSE
```

Each part of the repository has a specific purpose.

### `learning/`

Contains material created while studying books and other learning resources.

Each book can have its own directory:

```text
learning/
├── fundamentals/
├── grokking-algorithms/
└── <book-name>/
```

Notes, explanations, and exercises that belong to a specific book or chapter stay here.

This keeps the learning material connected to the source it came from.

---

### `algorithms/`

Contains the main implementations of algorithms I study.

Algorithms are organized by topic rather than by book:

```text
algorithms/
├── searching/
├── sorting/
├── graph/
└── ...
```

Each algorithm can have its own directory:

```text
algorithms/
└── searching/
    └── binary-search/
        ├── implementation
        ├── tests
        ├── documentation
        └── visualization
```

The current Binary Search implementation is an example of this structure:

[`algorithms/searching/binary-search/`](./algorithms/searching/binary-search/)

If I study the same algorithm again from another book, the new learning material stays under `learning/`, while the main implementation remains organized here.

---

### `data-structures/`

Contains implementations and exploration of data structures.

Data structures are organized by concept:

```text
data-structures/
├── linked-lists/
├── stacks/
├── queues/
├── hash-tables/
├── trees/
├── graphs/
└── ...
```

Like algorithms, data structures are kept independent from the books where I study them.

---

### `challenges/`

Contains problems where I practice and apply concepts I have already studied.

```text
challenges/
├── binary-search/
├── sorting/
└── ...
```

Exercises that belong directly to a specific book or chapter stay under `learning/`.

`challenges/` is for problems where I practice or apply a concept independently from a specific book.

Challenges are grouped by their primary concept. A challenge may involve several algorithms or data structures, but it is placed under the topic it is mainly intended to practice.

---

### [`SOURCES.md`](./SOURCES.md)

Contains the books and other resources used throughout my studies.

Keeping sources in a separate file makes it easier to track the material behind the learning notes without tying the main repository structure to a specific book.

---

## How the Repository Is Organized

```text
Books & Resources
       │
       ▼
    learning/
       │
       ▼
Knowledge & Practice
       │
   ┌───┴────────────┐
   ▼                ▼
algorithms/   data-structures/
   │                │
   └───────┬────────┘
           ▼
       challenges/
```

In simple terms:

- `learning/` — where I study and keep book-specific material
- `algorithms/` — where I implement algorithms
- `data-structures/` — where I implement and explore data structures
- `challenges/` — where I practice applying what I have learned

This diagram describes how content is organized in the repository.

For the learning process itself — **Learn → Implement → Test → Explore → Apply** — see the [How I Study](#how-i-study) section above.

This structure keeps the repository independent from any single book and gives each type of material a clear place.

---

## Running the Project

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

---

## License

This project is available under the [MIT License](./LICENSE).