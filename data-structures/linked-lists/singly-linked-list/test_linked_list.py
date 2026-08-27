from linked_list import LinkedList


def test_new_linked_list_is_empty():
    linked_list = LinkedList()

    assert linked_list.head is None
    assert linked_list.tail is None


def test_prepend_to_empty_list():
    linked_list = LinkedList()

    linked_list.prepend(10)

    assert linked_list.head.value == 10
    assert linked_list.tail.value == 10
    assert linked_list.head.next is None


def test_prepend_multiple_items():
    linked_list = LinkedList()

    linked_list.prepend(10)
    linked_list.prepend(20)
    linked_list.prepend(30)

    assert linked_list.head.value == 30
    assert linked_list.head.next.value == 20
    assert linked_list.head.next.next.value == 10

    assert linked_list.tail.value == 10


def test_append_to_empty_list():
    linked_list = LinkedList()

    linked_list.append(10)

    assert linked_list.head.value == 10
    assert linked_list.tail.value == 10
    assert linked_list.head.next is None


def test_append_multiple_items():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.head.value == 10
    assert linked_list.head.next.value == 20
    assert linked_list.head.next.next.value == 30

    assert linked_list.tail.value == 30
    assert linked_list.tail.next is None


def test_search_existing_value():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    result = linked_list.search(20)

    assert result is not None
    assert result.value == 20


def test_search_missing_value():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)

    result = linked_list.search(99)

    assert result is None


def test_delete_first_item():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    deleted = linked_list.delete_first_item()

    assert deleted == 10
    assert linked_list.head.value == 20
    assert linked_list.tail.value == 30


def test_delete_only_item():
    linked_list = LinkedList()

    linked_list.append(10)

    deleted = linked_list.delete_first_item()

    assert deleted == 10
    assert linked_list.head is None
    assert linked_list.tail is None


def test_delete_from_empty_list():
    linked_list = LinkedList()

    deleted = linked_list.delete_first_item()

    assert deleted is None


def test_delete_middle_item():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)

    deleted = linked_list.delete(30)

    assert deleted == 30

    assert linked_list.head.value == 10
    assert linked_list.head.next.value == 20
    assert linked_list.head.next.next.value == 40

    assert linked_list.tail.value == 40


def test_delete_head():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    deleted = linked_list.delete(10)

    assert deleted == 10
    assert linked_list.head.value == 20
    assert linked_list.tail.value == 30


def test_delete_tail():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    deleted = linked_list.delete(30)

    assert deleted == 30

    assert linked_list.head.value == 10
    assert linked_list.tail.value == 20
    assert linked_list.tail.next is None


def test_delete_missing_value():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    deleted = linked_list.delete(99)

    assert deleted is None

    assert linked_list.head.value == 10
    assert linked_list.tail.value == 30


def test_traverse(capsys):
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    linked_list.traverse()

    captured = capsys.readouterr()

    assert captured.out == "10\n20\n30\n"