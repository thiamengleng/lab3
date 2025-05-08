import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_ten():
    input_arr = [1,2,3,4,5,56,6,7,8,9,10,12,13]

    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == 1)
    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == 1)

def test_zero():
    input_arr = []

    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == 0)
    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == 0)

def test_invalid():
    input_arr = [2.1, 5.2, 6.9, 5.6, 4.9]

    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == 2)
    assert(Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == 2)