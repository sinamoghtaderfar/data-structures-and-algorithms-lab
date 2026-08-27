# Singly Linked List

This folder contains my implementation of a singly linked list in Python.

I built it while studying linked lists to understand how nodes are connected and how insertion, traversal, search, and deletion work without relying on Python's built-in list.

## How it works

Each node stores two things:

- a `value`
- a reference to the next node

The list keeps references to both `head` and `tail`.

```text
head
 ↓
10 → 20 → 30 → None
          ↑
         tail
```

`head` points to the first node, while `tail` points to the last one.

Keeping a `tail` reference is useful because it lets the list append a new node without walking through every existing node first.

## Implementation

The implementation contains two classes:

- `Node` — represents one item in the list
- `LinkedList` — manages the chain of nodes

### `prepend(value)`

Adds a new node to the beginning of the list.

```text
10 → 20 → 30

prepend(5)

5 → 10 → 20 → 30
```

Because the list already knows where the first node is, this operation takes constant time.

### `append(value)`

Adds a new node to the end of the list.

Since the implementation keeps a `tail` reference, appending does not require a full traversal of the list.

### `traverse()`

Starts from `head` and follows each node's `next` reference until reaching `None`.

This shows one of the main properties of a linked list: values are reached sequentially rather than by direct index access.

### `search(value)`

Walks through the nodes until the requested value is found.

If a matching node exists, the method returns that `Node`. Otherwise, it returns `None`.

### `delete_first_item()`

Removes the first node by moving `head` to the next node.

If the removed node was the only node in the list, both `head` and `tail` become `None`.

### `delete(value)`

Finds the first node containing the requested value and removes it from the chain.

To remove a node from the middle, the previous node is connected directly to the node after the one being removed.

```text
Before:

10 → 20 → 30 → 40

Delete 30:

10 → 20 ─────→ 40
```

If the deleted node is the last node, `tail` is updated as well.

## Time Complexity

| Operation | Complexity |
| --- | --- |
| Prepend | `O(1)` |
| Append | `O(1)` |
| Traverse | `O(n)` |
| Search | `O(n)` |
| Delete first item | `O(1)` |
| Delete by value | `O(n)` |

The `tail` reference makes appending `O(1)`, but deleting the last node is still `O(n)` in a singly linked list when only the tail is known. The node before it still has to be found.

## Tests

The implementation is tested with `pytest`.

The tests cover empty lists, insertion at both ends, successful and unsuccessful searches, deleting the head, a middle node, and the tail, and keeping `head` and `tail` consistent after changes.

Run the tests with:

```bash
pytest data-structures/linked-lists/singly-linked-list/test_linked_list.py -v
```

## What I learned

Implementing the structure manually made references much clearer to me.

The most important idea was understanding that deleting a node does not require shifting the remaining elements. Instead, the links between nodes are changed.

It also made the trade-off with arrays easier to see: insertion at a known position can be cheap, while finding a value still requires walking through the list one node at a time.
