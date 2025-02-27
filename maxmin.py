def find_min_max(array):
    # lowest number initiated as positive infinity, highest as lowest infinity
    high = float('-inf')
    low = float('inf')
    # for each number in array, the lowest and highest number so far is updated when the following conditions are met
    for num in array:
        if num > high:
            high = num
        elif num < low:
            low = num
    return [low, high]


if __name__ == '__main__':
    test_arr1 = [2, 4, 1, 0, 2, -1]
    test_arr2 = [20, 50, 12, 6, 14, 8]
    test_arr3 = [100, -100]

    print(f'Test array 1: {test_arr1}')
    print(f'{find_min_max(test_arr1)}')

    print(f'Test array 2: {test_arr2}')
    print(f'{find_min_max(test_arr2)}')

    print(f'Test array 3: {test_arr3}')
    print(f'{find_min_max(test_arr3)}')
