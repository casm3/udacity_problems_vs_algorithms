def sort_012(arr: list[int]):
    """
    Given an input array consisting on only 0, 1, and 2,
    sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low: int = 0
    high: int = len(arr) - 1
    pivot: int = 0

    while pivot <= high:
        if arr[pivot] == 0:
            arr[low], arr[pivot] = arr[pivot], arr[low]
            low += 1
            pivot += 1
        elif arr[pivot] == 1:
            pivot += 1
        else:
            arr[pivot], arr[high] = arr[high], arr[pivot]
            high -= 1
    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function(
    [
        2, 1, 2, 0, 0, 2, 1, 0, 1,
        0, 0, 2, 2, 2, 1, 2, 0, 0,
        0, 2, 1, 0, 2, 0, 0, 1
    ]
)
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0])
test_function([1])
test_function([])
