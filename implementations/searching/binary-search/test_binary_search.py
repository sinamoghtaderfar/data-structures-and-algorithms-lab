from binary_search import binary_search


def test_target_exists():
    arr = [5, 10, 15, 20, 25, 30, 35]

    result = binary_search(arr, 25)

    assert result == 4

def test_target_does_not_exist():
    arr = [5, 10, 15, 20, 25, 30, 35]

    result = binary_search(arr, 100)

    assert result == -1

def test_first_element():
    arr = [5, 10, 15, 20, 25, 30, 35]

    result = binary_search(arr, 5)

    assert result == 0
    
def test_last_element():
    arr = [5, 10, 15, 20, 25, 30, 35]

    result = binary_search(arr, 35)
    
    assert result == 6

def test_empty_array():
    restult = binary_search([], 10)
    
    assert restult is None or restult == -1

def test_single_element_array():
    arr = [10]

    result = binary_search(arr, 10)

    assert result == 0
    
def test_single_elemente_not_found():
    result = binary_search([10], 5)
    
    assert result == -1 or result is None