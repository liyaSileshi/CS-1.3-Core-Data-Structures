#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)

def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

def linear_search_recursive(array, item, index=0):
    #implement linear search recursively here
    if index >= len(array):
        return None #not found

    if item == array[index]:
        return index #found
    else:
        index += 1
        return linear_search_recursive(array, item, index) #call it again 

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = round((left + right) / 2)
        # mid = (left+right)//2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            right = mid - 1

        elif array[mid] < item:
            left = mid + 1
    return None

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    arr = [1,2,3,4]
    # if len(args) == 1:
    #     num = int(args[0])
    # result = linear_search(arr, 3)
    result = binary_search_iterative(arr, 4)
        # print('linear_search({} in array {}) => index {}'.format(3, arr, result))
    print(result)
    # else:
    #     print('Usage: {} number'.format(sys.argv[0]))

if __name__ == '__main__':
    main()