class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        # Add a new node to the beginning
        new_item = Node(value)

        new_item.next = self.head
        self.head = new_item

        if self.tail is None:
            self.tail = new_item

    def append(self, value):
        # Add a new node to the end
        new_item = Node(value)

        if self.head is None:
            self.head = new_item
            self.tail = new_item
            return

        self.tail.next = new_item
        self.tail = new_item

    def traverse(self):
        # Walk through the list from the head
        node = self.head

        while node is not None:
            print(node.value)
            node = node.next

    def search(self, value):
        node = self.head

        while node is not None:
            if node.value == value:
                return node

            node = node.next

        return None

    def delete_first_item(self):
        if self.head is None:
            return None

        removed_value = self.head.value
        self.head = self.head.next

        # If the list became empty, reset tail too
        if self.head is None:
            self.tail = None

        return removed_value

    def delete(self, value):
        if self.head is None:
            return None

        # The first node is a special case
        if self.head.value == value:
            return self.delete_first_item()

        prev_node = self.head
        node = self.head.next

        while node is not None:
            if node.value == value:
                prev_node.next = node.next

                if node == self.tail:
                    self.tail = prev_node

                return node.value

            prev_node = node
            node = node.next

        return None