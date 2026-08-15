[English](./README.md) | [فارسی](./README.fa.md)

# Data Structures Fundamentals

These are my notes on the basic data structures and complexity concepts I want to understand before going deeper into algorithms.

The goal of this document is not to cover every detail or implement every data structure from scratch. Instead, I want to build a clear mental model of the most common structures, understand how they behave, and know why I might choose one over another.

Later in this repository, I will study and implement many of these concepts in much more detail.

---

## 1. What Is a Data Structure?

A **data structure** is a way of organizing and storing data so that it can be used efficiently.

Programs constantly work with data:

* users
* products
* messages
* numbers
* files
* tasks
* locations
* relationships between objects

The way we organize that data affects how easily and efficiently we can work with it.

For example, imagine that we have one million user IDs and want to find a particular one.

Depending on how the data is stored and which algorithm we use, finding that user could be very fast or unnecessarily slow.

This is why data structures and algorithms are closely related.

A data structure answers questions such as:

* How should the data be stored?
* How can I access it?
* How can I search it?
* How can I insert new data?
* How can I remove data?

An algorithm answers a different question:

> What sequence of steps should I use to solve a problem?

### Simple Example

Suppose we have:

```text
[10, 20, 30, 40, 50]
```

This data is stored as a sequence.

If I want the third element, the structure allows me to access it directly by its position.

If I want to find the number `40`, I need an algorithm that searches through the data.

So, in simple terms:

> **Data structures organize data. Algorithms operate on data.**

---

# 2. Arrays and Lists

An array is one of the most fundamental data structures.

It stores multiple values in an ordered sequence.

For example:

```text
[10, 20, 30, 40]
```

Each element has a position called an **index**.

```text
Index:   0   1   2   3
Value:  10  20  30  40
```

So the value at index `2` is:

```text
30
```

In Python, I will often work with `list`:

```python
numbers = [10, 20, 30, 40]

print(numbers[2])
```

Output:

```text
30
```

Python lists are not exactly the same as low-level fixed-size arrays used in languages such as C or C++, but they provide a similar indexed sequence abstraction for many everyday operations.

## Why Arrays Are Useful

Arrays are useful when:

* order matters
* I need access by position
* I have many similar values
* I frequently iterate over all elements

Examples include:

```text
temperatures
user IDs
scores
product prices
coordinates
```

## Access

Accessing an element by index is very fast.

```python
numbers[3]
```

For an array-like structure, indexed access is generally:

```text
O(1)
```

The size of the array does not significantly change how many steps are needed to access a known index.

## Search

If the value's position is unknown, I may need to inspect elements one by one.

```text
[3, 8, 12, 19, 25]

Find 19:

3 → 8 → 12 → 19
```

A simple linear search can require:

```text
O(n)
```

operations.

## Insertion and Deletion

Insertion and deletion can be more expensive when elements need to be shifted.

For example:

```text
Before:

[10, 20, 30, 40]

Insert 15:

[10, 15, 20, 30, 40]
```

Some existing elements may need to move.

The exact behavior depends on the language and implementation.

## Mental Model

I think of an array as:

> A row of numbered boxes.

If I know the box number, I can go directly to it.

## Key Takeaway

Arrays are excellent when I need:

* ordered data
* fast indexed access
* straightforward iteration

---

# 3. Linked Lists

A **linked list** also stores a sequence of values, but it works differently from an array.

Instead of relying mainly on positions, a linked list is built from objects called **nodes**.

A simple linked list might look like:

```text
[10] → [20] → [30] → [40]
```

Each node usually contains:

```text
value
next
```

For example:

```text
Node
├── value: 20
└── next: reference to node containing 30
```

The nodes form a chain.

## What Is a Node?

A node is simply one element in a larger structure.

For example:

```text
[10] → [20] → [30]
```

There are three nodes.

Each one stores some data and a reference to another node.

## Traversal

With an array, I can often directly access something like:

```text
element at index 500
```

With a basic linked list, I usually start from the beginning and follow the links:

```text
10 → 20 → 30 → 40
```

This process is called **traversal**.

Finding an element by position may therefore require:

```text
O(n)
```

time.

## Why Use a Linked List?

Linked lists can be useful when elements need to be connected dynamically and when insertion or deletion at a known position should not require shifting many other elements.

For example:

```text
A → B → C
```

If I already have the right references, inserting `X` between `B` and `C` can conceptually become:

```text
A → B → X → C
```

Instead of shifting an entire sequence, the connections can be changed.

## Array vs Linked List

A simplified comparison:

| Operation                       |                Array |           Linked List |
| ------------------------------- | -------------------: | --------------------: |
| Access by index                 |                 Fast |                Slower |
| Sequential traversal            |                 Good |                  Good |
| Insert/delete at known location | May require shifting |      Can be efficient |
| Memory layout                   |      More contiguous | Nodes may be separate |

Real implementations have additional details, but this comparison is enough for my current level.

## Mental Model

I think of a linked list as:

> A treasure hunt where every location tells me where the next location is.

I cannot necessarily jump directly to the tenth node. I follow the chain.

## Key Takeaway

A linked list is a sequence of connected nodes.

The important concepts are:

* node
* value
* next reference
* traversal

---

# 4. Stacks

A **stack** is a data structure that follows:

```text
LIFO
```

which means:

> **Last In, First Out**

The easiest analogy is a stack of plates.

If I place plates like this:

```text
C
B
A
```

`C` was placed last.

It is also the first plate I remove.

## Main Operations

### Push

Add an item to the top.

```text
Before:

B
A

push(C)

After:

C
B
A
```

### Pop

Remove the top item.

```text
C
B
A

pop()

returns C
```

### Peek / Top

Look at the top element without removing it.

## Python Example

A Python list can be used as a simple stack:

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

last_item = stack.pop()

print(last_item)
```

Output:

```text
C
```

## Common Uses

Stacks appear in many areas of programming.

Examples:

* function calls
* recursion
* undo functionality
* expression parsing
* syntax processing
* depth-first search
* browser-like navigation history

## Stack and Function Calls

When one function calls another function, the program needs to remember where it should return afterward.

Conceptually, this behavior is closely related to a stack.

This becomes particularly important when learning recursion.

## Mental Model

I think of a stack as:

> The most recent unfinished thing gets handled first.

## Key Takeaway

Remember:

```text
Stack = LIFO
```

Last in, first out.

---

# 5. Queues

A **queue** follows the opposite idea:

```text
FIFO
```

which means:

> **First In, First Out**

The easiest example is a real-world queue.

Suppose people arrive in this order:

```text
A → B → C → D
```

`A` arrived first, so `A` should normally be processed first.

## Main Operations

### Enqueue

Add something to the end of the queue.

### Dequeue

Remove something from the front of the queue.

Conceptually:

```text
Front                 Back
  ↓                     ↓

A → B → C → D
```

After one dequeue:

```text
B → C → D
```

## Common Uses

Queues are useful when work should happen in arrival order.

Examples:

* task processing
* print jobs
* request handling
* message processing
* scheduling
* Breadth-First Search (BFS)

## Stack vs Queue

This distinction is important:

```text
Stack
Last In → First Out

Queue
First In → First Out
```

## Mental Model

I think of a queue as:

> People waiting in line.

The person who arrived first should usually be served first.

## Key Takeaway

Remember:

```text
Queue = FIFO
```

First in, first out.

---

# 6. Hash Tables

A **hash table** stores data using **keys and values**.

For example:

```text
name → Sina
city → Bamberg
age  → 25
```

Instead of saying:

> Give me the third element.

I can say:

> Give me the value associated with the key `name`.

In Python, dictionaries are based on this general idea.

```python
user = {
    "name": "Sina",
    "city": "Bamberg",
    "age": 25,
}

print(user["name"])
```

Output:

```text
Sina
```

## Why Is This Useful?

Imagine storing product prices:

```python
prices = {
    "apple": 2.50,
    "banana": 1.80,
    "orange": 2.10,
}
```

To retrieve the apple price:

```python
prices["apple"]
```

I do not conceptually need to search every product one by one.

Hash tables are designed to make this kind of lookup very efficient.

## Hash Function

Behind a hash table is the idea of a **hash function**.

Very roughly:

```text
key
 ↓
hash function
 ↓
location
```

The hash function helps determine where the value associated with a key should be stored.

I do not need to understand the internal implementation deeply yet.

The important idea is:

> A key can be transformed into information that helps locate its value efficiently.

## Complexity

Average-case lookup in a well-designed hash table is usually described as:

```text
O(1)
```

The same is generally true for insertion and deletion in the average case.

However, `O(1)` here does not mean that absolutely every possible operation always takes exactly the same amount of time.

There are implementation details and edge cases.

## Collision

Sometimes two different keys can map to the same internal location.

This is called a **collision**.

Hash tables have strategies for handling collisions.

For now, knowing that collisions exist is enough.

## Common Uses

Hash tables are everywhere:

* dictionaries
* caches
* configuration values
* counting frequencies
* lookup tables
* user data
* indexes
* sets

## Mental Model

I think of a hash table as:

> A labeled storage system.

Instead of remembering a numerical position, I use a meaningful key.

## Key Takeaway

A hash table stores:

```text
key → value
```

and is designed for very fast lookup by key.

---

# 7. Trees

A **tree** is a hierarchical data structure.

Unlike a simple sequence, elements can have parent-child relationships.

Example:

```text
        A
       / \
      B   C
     / \
    D   E
```

## Important Terms

### Root

The top node.

In the example:

```text
A
```

is the root.

### Parent

A node that has nodes below it.

For example:

```text
B
```

is the parent of `D` and `E`.

### Child

A node directly below another node.

`D` and `E` are children of `B`.

### Leaf

A node with no children.

In the example:

```text
D
E
C
```

are leaves.

## Real-World Example

A directory structure can be thought of as a tree:

```text
Projects
├── backend
│   ├── api
│   └── database
│
└── frontend
    ├── components
    └── pages
```

Other hierarchical systems also naturally resemble trees.

## Binary Tree

A **binary tree** is a tree where each node can have at most two children.

For example:

```text
        10
       /  \
      5    20
```

I only need to recognize this concept for now.

## Binary Search Tree

A **Binary Search Tree (BST)** adds an ordering rule.

A simplified version is:

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

I will study tree algorithms and BST behavior in more detail later.

## Mental Model

I think of a tree as:

> A hierarchy where one thing can branch into several smaller things.

## Key Takeaway

For now, I need to understand:

* node
* root
* parent
* child
* leaf
* hierarchy

---

# 8. Graphs

A **graph** represents relationships between objects.

Graphs consist mainly of:

```text
Vertices / Nodes
Edges
```

A graph might look like:

```text
A ----- B
|       |
|       |
C ----- D
```

`A`, `B`, `C`, and `D` are vertices.

The lines between them are edges.

## Why Graphs Matter

Many real-world problems are naturally graphs.

Examples:

* road networks
* social networks
* computer networks
* airline routes
* recommendation systems
* dependencies
* website links

## Social Network Example

Suppose:

```text
Sina ----- Ali
  |
  |
 Reza ---- Sara
```

People are nodes.

Relationships are edges.

## Undirected Graph

An undirected connection has no direction.

```text
A ----- B
```

Conceptually:

```text
A is connected to B
B is connected to A
```

## Directed Graph

A directed graph uses arrows.

```text
A → B
```

This relationship does not necessarily imply:

```text
B → A
```

A following relationship on a social platform is a good example.

One user can follow another without being followed back.

## Weighted Graph

Some graphs assign values to edges.

For example:

```text
Berlin ---- 190 km ---- Leipzig
```

The weight might represent:

* distance
* time
* cost
* risk
* capacity

Weighted graphs become important for algorithms such as shortest-path algorithms.

## Graph Algorithms

Later, I will study algorithms such as:

```text
Breadth-First Search (BFS)
Depth-First Search (DFS)
Dijkstra's Algorithm
```

These algorithms answer questions such as:

* Can I reach one node from another?
* What nodes are connected?
* What is the shortest path?
* What should I visit first?

## Mental Model

I think of a graph as:

> Things plus relationships between those things.

## Key Takeaway

A graph consists of:

```text
nodes + connections
```

and is especially useful for modeling relationships and networks.

---

# 9. Common Data Structure Operations

Different data structures support different operations with different performance characteristics.

These terms appear frequently when studying algorithms.

## Access

Retrieve an element when its location or key is already known.

Example:

```python
numbers[3]
```

## Search

Find an element when its location is unknown.

Example:

```text
Find 42 inside a collection.
```

## Insert

Add a new element.

Example:

```text
Before:

[10, 20, 30]

After inserting 15:

[10, 15, 20, 30]
```

## Delete

Remove an element.

Example:

```text
Before:

[10, 20, 30]

Delete 20:

[10, 30]
```

## Traverse

Visit elements one after another.

For example:

```text
A → B → C → D
```

Traversal becomes especially important in:

* linked lists
* trees
* graphs

## Why These Operations Matter

When choosing a data structure, I should not only ask:

> Can this structure store my data?

I should also ask:

> Which operations will my program perform most often?

For example, one structure might provide very fast lookup but be less convenient for another operation.

There is usually a trade-off.

---

# 10. Big O Basics

When comparing algorithms and data structures, I need a way to describe how their work grows as the input grows.

This is where **Big O notation** becomes useful.

Big O is not mainly about measuring exact execution time in seconds.

Instead, it describes how the amount of work grows when the input size grows.

Suppose:

```text
n = number of items
```

---

## O(1) — Constant Time

Example:

```python
numbers[5]
```

If I already know the index, accessing that position does not require searching through every previous value.

Conceptually:

```text
10 items       → roughly constant work
1,000 items    → roughly constant work
1,000,000 items → roughly constant work
```

This is called:

```text
O(1)
```

### Mental Model

> I know exactly where to go.

---

## O(log n) — Logarithmic Time

A common example is **Binary Search**.

Instead of checking every item, Binary Search repeatedly removes about half of the remaining possibilities.

Imagine one million sorted values.

A linear approach may inspect a huge number of elements.

Binary Search only needs roughly:

```text
20 comparisons
```

in the worst-case scale for around one million values.

That is extremely powerful.

### Mental Model

> Every step removes a large part of the remaining problem.

---

## O(n) — Linear Time

Suppose I search through a list one element at a time:

```python
for number in numbers:
    if number == target:
        break
```

If there are more elements, there may be proportionally more work.

```text
10 items      → up to about 10 checks
100 items     → up to about 100 checks
1,000 items   → up to about 1,000 checks
```

This is:

```text
O(n)
```

### Mental Model

> I may need to look at everything once.

---

## O(n log n)

This complexity appears in several efficient sorting algorithms.

Examples include:

```text
Merge Sort
Heap Sort
Quicksort — average case
```

I do not need to understand the mathematical details yet.

For now, I only need to recognize that:

```text
O(n log n)
```

usually scales much better than:

```text
O(n²)
```

for large inputs.

---

## O(n²) — Quadratic Time

A common example is a nested loop:

```python
for x in numbers:
    for y in numbers:
        pass
```

If the list contains `n` items, the inner work may happen approximately `n × n` times.

For example:

```text
100 items
100 × 100
= 10,000 operations
```

With:

```text
1,000 items
```

we may reach roughly:

```text
1,000,000 operations
```

This can become expensive quickly.

### Mental Model

> For every item, I may need to process every item again.

---

# 11. Comparing Growth Rates

A simplified order from better scaling to worse scaling is:

```text
O(1)
 ↓
O(log n)
 ↓
O(n)
 ↓
O(n log n)
 ↓
O(n²)
```

For very large datasets, these differences matter a lot.

An algorithm that looks perfectly fine with 100 elements may behave very differently with 100 million elements.

That is why I should not only ask:

> Does my code work?

I should also ask:

> How does my solution behave when the input becomes much larger?

---

# 12. Quick Comparison

This is only a simplified overview. Exact complexity depends on the implementation.

| Structure    | Main Idea               | Typical Strength                   |
| ------------ | ----------------------- | ---------------------------------- |
| Array / List | Ordered sequence        | Fast indexed access                |
| Linked List  | Connected nodes         | Flexible node insertion/deletion   |
| Stack        | LIFO                    | Process most recent item first     |
| Queue        | FIFO                    | Process items in arrival order     |
| Hash Table   | Key-value mapping       | Fast lookup by key                 |
| Tree         | Hierarchical nodes      | Represent hierarchy                |
| Graph        | Nodes and relationships | Represent networks and connections |

---

# 13. Mental Models

These simple mental models help me remember the structures.

### Array

```text
A row of numbered boxes.
```

### Linked List

```text
A chain where every node knows the next node.
```

### Stack

```text
A stack of plates.
Last added → first removed.
```

### Queue

```text
People waiting in line.
First arrived → first served.
```

### Hash Table

```text
A storage system with labels.
Key → Value
```

### Tree

```text
A hierarchy that branches downward.
```

### Graph

```text
Objects connected by relationships.
```

---

# 14. What I Need to Remember Before Studying Algorithms

At this point, I do not need to implement every data structure from memory.

Before moving deeper into algorithms, I mainly want to remember the following:

### Arrays / Lists

* ordered collection
* index
* fast indexed access
* searching may require traversal

### Linked Lists

* made of nodes
* nodes point to other nodes
* no normal direct indexed access
* traversal follows links

### Stacks

```text
LIFO
```

### Queues

```text
FIFO
```

### Hash Tables

```text
key → value
```

Average lookup is usually very fast.

### Trees

Understand:

```text
root
parent
child
leaf
```

### Graphs

Understand:

```text
vertex / node
edge
directed
undirected
weighted
```

### Big O

Recognize:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
```

---

# 15. Final Takeaway

The most important lesson for me is that there is no single data structure that is always the best choice.

Each structure makes certain operations easier or faster and introduces its own trade-offs.

Before choosing a structure, I should think about:

```text
What data am I storing?

How will I access it?

Will I search frequently?

Will I insert or delete frequently?

Does order matter?

Are there relationships between the values?

How large could the data become?
```

Understanding these questions will make it easier to understand why different algorithms use different data structures.

My next step is to study algorithms more deeply and gradually turn these concepts into real implementations, tests, visualizations, and performance experiments.

---

## Study Status

This document covers only the fundamentals I want to know before going deeper into Data Structures and Algorithms.

More advanced topics such as the following will be studied separately:

* doubly linked lists
* circular linked lists
* deques
* heaps
* priority queues
* binary search trees
* balanced trees
* AVL trees
* red-black trees
* tries
* disjoint sets / union-find
* graph representations
* advanced hashing techniques

These topics are intentionally outside the scope of this introductory note.
