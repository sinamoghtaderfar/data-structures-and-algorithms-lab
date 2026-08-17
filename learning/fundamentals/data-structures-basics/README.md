[فارسی](./README.fa.md)

# Data Structures Fundamentals

These are my foundation notes on data structures and complexity.

I am not trying to turn this document into a complete computer science textbook. The goal is simpler: build a strong mental model of the structures I will keep seeing while learning algorithms, understand their basic trade-offs, and know why I might choose one structure over another.

Later in this repository, I will implement and explore many of these structures in much more detail.

---

## 1. Data Structures vs Algorithms

A **data structure** is a way of organizing and storing data.

An **algorithm** is a sequence of steps used to solve a problem.

They are closely related, but they answer different questions.

A data structure helps answer questions like:

* How should I store the data?
* How do I access it?
* How expensive is insertion or deletion?
* How naturally can I represent relationships?
* What operations should be fast?

An algorithm asks:

> What steps should I perform to get the result I want?

For example:

```text
[10, 20, 30, 40, 50]
```

The sequence itself is a way of organizing the data.

If I already know that I want the value at index `3`, indexed access gives me:

```text
40
```

But if I only know that I want to find the value `40`, I need a search strategy.

That leads to one of the most useful mental models in this repository:

> **Data structures organize data. Algorithms operate on that data.**

Choosing the right combination of the two can dramatically change the performance and simplicity of a solution.

---

## 2. A Small Complexity Primer

Before comparing data structures, I need a basic way to describe how their cost grows as the amount of data grows.

That is where **Big O notation** becomes useful.

Some common complexities are:

| Complexity   | Rough idea                                              |
| ------------ | ------------------------------------------------------- |
| `O(1)`       | Constant work                                           |
| `O(log n)`   | The problem shrinks dramatically each step              |
| `O(n)`       | Work grows roughly with the number of elements          |
| `O(n log n)` | Common in efficient sorting algorithms                  |
| `O(n²)`      | Often involves comparing many elements with many others |

For example:

```text
Accessing arr[500]      -> O(1)
Scanning an entire list -> O(n)
Binary Search           -> O(log n)
```

Big O does not tell me the exact running time in milliseconds.

It tells me how the amount of work grows as the input becomes larger.

That distinction is important.

---

## 3. Arrays and Python Lists

An array stores values in an ordered sequence.

Conceptually:

```text
Index:   0   1   2   3
Value:  10  20  30  40
```

If I know the index, I can directly access the value:

```python
numbers = [10, 20, 30, 40]

print(numbers[2])
```

Output:

```text
30
```

### Python's `list`

Python's built-in `list` is implemented as a **dynamic array**.

That means it behaves differently from a low-level fixed-size array in languages like C, but it still gives me fast indexed access and dynamically grows when needed.

This distinction matters because I should not mentally treat every programming-language "list" as a linked list.

In Python:

```python
numbers = [10, 20, 30]
```

is an array-like dynamic sequence.

### Indexed Access

Access by index is normally:

```text
O(1)
```

Example:

```python
numbers[2]
```

The important idea is that Python does not need to start from the first element and walk through every previous item.

It can directly access the requested position.

### Searching

If I do not know the index and simply scan for a value:

```text
[3, 8, 12, 19, 25]

Find 19:

3 → 8 → 12 → 19
```

the search may require:

```text
O(n)
```

time.

A large list may therefore be excellent for indexed access while still being relatively expensive to search linearly.

### Insertion and Deletion

Inserting into the middle can require later elements to move.

```text
Before:

[10, 20, 30, 40]

Insert 15:

[10, 15, 20, 30, 40]
```

That shifting is one reason middle insertion is generally more expensive than direct indexed access.

### Mental Model

I think of an array as:

> **A row of numbered boxes.**

If I know the box number, I can go directly to it.

### Good Fit

Arrays are a strong choice when:

* order matters;
* indexed access matters;
* I frequently iterate over elements;
* data naturally belongs in a sequence.

---

## 4. Linked Lists

A **linked list** also represents a sequence, but the elements are connected differently.

Instead of relying on contiguous indexed positions, a linked list consists of **nodes**.

A simple singly linked list:

```text
[10] → [20] → [30] → [40] → None
```

Each node usually stores:

```text
value
next
```

Conceptually:

```text
Node
├── value: 20
└── next: reference to the next node
```

### Traversal

If I want the fourth node, I normally cannot jump directly to it.

I follow the chain:

```text
10 → 20 → 30 → 40
```

That means accessing an arbitrary position usually requires:

```text
O(n)
```

time.

### Insertion

Suppose I already have a reference to node `B`:

```text
A → B → C
```

To insert `X`:

```text
A → B → X → C
```

the link updates themselves can be performed in:

```text
O(1)
```

However, there is an important detail:

> If I first need to search for `B`, finding it may still require `O(n)` time.

That distinction is easy to miss.

### Array vs Linked List

| Operation                      |        Dynamic Array |       Linked List |
| ------------------------------ | -------------------: | ----------------: |
| Indexed access                 |               `O(1)` |            `O(n)` |
| Search                         |               `O(n)` |            `O(n)` |
| Insert/delete at known node    | May require shifting |     Can be `O(1)` |
| Memory locality                |         Usually good |    Usually poorer |
| Extra pointer/reference memory |                  Low | Required per node |

### Mental Model

I think of a linked list as:

> **A treasure hunt where every location tells me where the next location is.**

I cannot magically jump to node number 500. I follow the links.

---

## 5. Stacks

A **stack** follows:

```text
LIFO
```

meaning:

> **Last In, First Out**

A stack of plates is the classic example.

```text
Top
 ↓
 C
 B
 A
```

`C` was added last, so it is removed first.

### Main Operations

Push:

```text
push(C)
```

adds an item to the top.

Pop:

```text
pop()
```

removes the top item.

Peek:

```text
peek()
```

reads the top item without removing it.

### Python Example

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

item = stack.pop()

print(item)
```

Output:

```text
C
```

Using the end of a Python list this way gives efficient stack behavior.

### Where Stacks Appear

Stacks are used in:

* function calls;
* recursion;
* undo systems;
* parsing;
* expression evaluation;
* Depth-First Search;
* backtracking.

### Mental Model

> **The most recently added unfinished task gets handled first.**

---

## 6. Queues

A **queue** follows:

```text
FIFO
```

meaning:

> **First In, First Out**

Conceptually:

```text
Front                 Back
  ↓                     ↓

A → B → C → D
```

`A` arrived first, so `A` leaves first.

### Main Operations

Enqueue:

```text
add to the back
```

Dequeue:

```text
remove from the front
```

### Python Example

For a real queue in Python, `collections.deque` is usually a better choice than repeatedly removing the first element of a list.

```python
from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

first = queue.popleft()

print(first)
```

Output:

```text
A
```

### Where Queues Appear

Queues are useful in:

* task scheduling;
* message processing;
* request handling;
* print jobs;
* Breadth-First Search;
* producer/consumer systems.

### Stack vs Queue

```text
Stack -> LIFO
Queue -> FIFO
```

That small distinction changes the behavior of entire algorithms.

---

## 7. Hash Tables

A **hash table** stores data using keys and values.

Conceptually:

```text
name → Sina
city → Bamberg
role → developer
```

Python's `dict` is built around this idea.

```python
user = {
    "name": "Sina",
    "city": "Bamberg",
}

print(user["name"])
```

Output:

```text
Sina
```

### Why Hash Tables Are Powerful

Suppose I have:

```python
prices = {
    "apple": 2.50,
    "banana": 1.80,
    "orange": 2.10,
}
```

I can ask directly for:

```python
prices["apple"]
```

Instead of conceptually scanning all products one by one.

### Hash Function

Very roughly:

```text
key
 ↓
hash function
 ↓
internal location
```

The hash function helps determine where information should be stored or looked up.

### Complexity

Average-case lookup, insertion, and deletion are commonly described as:

```text
O(1)
```

But this is an **average-case** expectation.

In pathological situations, performance can degrade, and worst-case lookup can reach:

```text
O(n)
```

### Collision

Two different keys can sometimes map to the same internal area.

That is called a:

```text
collision
```

Real hash tables use collision-handling strategies internally.

### Mental Model

> **A labeled storage system where I ask for data by key instead of position.**

---

## 8. Trees

A **tree** represents hierarchical relationships.

Example:

```text
        A
       / \
      B   C
     / \
    D   E
```

Some important terms:

```text
A -> root
B -> parent of D and E
D -> child of B
C, D, E -> leaves
```

### Real Example

A filesystem naturally looks tree-like:

```text
projects/
├── backend/
│   ├── api/
│   └── database/
└── frontend/
    ├── components/
    └── pages/
```

### Binary Tree

A binary tree allows each node to have at most two children.

```text
       10
      /  \
     5    20
```

### Binary Search Tree

A Binary Search Tree adds an ordering relationship.

A simplified rule:

```text
smaller values ← node → larger values
```

Example:

```text
        10
       /  \
      5    20
     / \
    2   7
```

The important point for now is not memorizing every tree operation.

It is recognizing that trees are useful when data naturally has **hierarchy or ordered branching**.

---

## 9. Graphs

A **graph** represents relationships between entities.

Graphs contain:

```text
vertices / nodes
edges
```

Example:

```text
A ----- B
|       |
|       |
C ----- D
```

### Why Graphs Matter

Graphs appear in:

* road networks;
* social networks;
* computer networks;
* dependency systems;
* flight routes;
* recommendation systems;
* web links.

### Undirected Graph

```text
A ----- B
```

The connection exists both ways.

### Directed Graph

```text
A → B
```

The relationship has a direction.

For example, one account can follow another without being followed back.

### Weighted Graph

Edges can also carry values:

```text
A --5--> B
```

That value could represent:

* distance;
* cost;
* travel time;
* latency;
* risk.

This is where algorithms such as Dijkstra's algorithm become important later.

### Mental Model

> **Nodes are things. Edges describe relationships between those things.**

---

## 10. Quick Comparison

| Structure     | Main Strength             | Typical Cost / Idea                            |
| ------------- | ------------------------- | ---------------------------------------------- |
| Dynamic Array | Fast indexed access       | Index access `O(1)`                            |
| Linked List   | Flexible node connections | Access `O(n)`                                  |
| Stack         | LIFO processing           | Push/pop `O(1)`                                |
| Queue         | FIFO processing           | Enqueue/dequeue `O(1)` with suitable structure |
| Hash Table    | Fast lookup by key        | Average `O(1)`                                 |
| Tree          | Hierarchical organization | Depends on tree type                           |
| Graph         | Modeling relationships    | Depends on representation and algorithm        |

There is no universally "best" data structure.

The useful question is:

> **Which operations matter most for this problem?**

A structure that is perfect for one workload can be a poor choice for another.

---

## 11. What I Want to Remember

If I forget the details, these are the ideas I want to keep:

```text
Array       -> numbered positions
Linked List -> connected nodes
Stack       -> LIFO
Queue       -> FIFO
Hash Table  -> key → value
Tree        -> hierarchy
Graph       -> relationships
```

More importantly:

> Choosing a data structure is about trade-offs.

Fast access, fast insertion, memory usage, ordering, and relationships all push the design in different directions.

---

## 12. Where This Goes Next

This document is only the foundation.

As I move deeper into the repository, I will study individual structures and algorithms separately, implement them, test them, visualize them where useful, and apply them to practical problems.

The goal is not to memorize definitions.

The goal is to understand the behavior well enough that, when I see a problem, I can begin asking:

> **What structure fits this problem, and why?**
