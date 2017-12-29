"""Implement a bubble sort algorithm."""

import timeit

def bubble_sort(arr):
    """Sort iterable from smallest to largest."""
    l = len(arr)
    for i in range(l):
        for i in range(l - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

if __name__ == '__main__':
    user_input = input('Input comma seperated numbers: ')
    input_list = user_input.split(',')
    numbers = [int(i) for i in input_list]
    print(bubble_sort(numbers))
    print('Time: {}'.format(timeit.timeit("bubble_sort(numbers)", setup="from __main__ import bubble_sort, numbers")))