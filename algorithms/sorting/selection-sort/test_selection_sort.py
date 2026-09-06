from selection_sort import find_smallest, selection_sort


def test_find_smallest():
    numbers = [5, 3, 6, 2, 10]

    result = find_smallest(numbers)

    assert result == 3


def test_selection_sort():
    numbers = [5, 3, 6, 2, 10]

    result = selection_sort(numbers)

    assert result == [2, 3, 5, 6, 10]


def test_selection_sort_empty_list():
    numbers = []

    result = selection_sort(numbers)

    assert result == []


def test_selection_sort_single_item():
    numbers = [7]

    result = selection_sort(numbers)

    assert result == [7]


def test_selection_sort_already_sorted():
    numbers = [1, 2, 3, 4, 5]

    result = selection_sort(numbers)

    assert result == [1, 2, 3, 4, 5]


def test_selection_sort_reverse_order():
    numbers = [5, 4, 3, 2, 1]

    result = selection_sort(numbers)

    assert result == [1, 2, 3, 4, 5]


def test_selection_sort_with_duplicates():
    numbers = [4, 2, 4, 1, 2]

    result = selection_sort(numbers)

    assert result == [1, 2, 2, 4, 4]


def test_selection_sort_with_negative_numbers():
    numbers = [3, -1, 5, -10, 0]

    result = selection_sort(numbers)

    assert result == [-10, -1, 0, 3, 5]


def test_selection_sort_does_not_modify_original_list():
    numbers = [5, 3, 6, 2, 10]
    original = numbers.copy()

    selection_sort(numbers)

    assert numbers == original