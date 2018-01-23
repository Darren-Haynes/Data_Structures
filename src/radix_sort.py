"""Implement radix sort algorithm."""

from random import randint, shuffle
from timeit import timeit


def radix_sort(arr):
    """Sort list of numberes with radix sort."""
    if len(arr) > 1:
        buckets = [[] for x in range(10)]
        lst = arr
        output = []
        t = 0
        m = len(str(max(arr)))
        while m > t:
            for num in lst:
                if len(str(num)) >= t + 1:
                    for b_num in range(10):
                        idx = num // 10**t % 10
                        if idx == b_num:
                            buckets[b_num].append(num)
                            break
                else:
                    output.append(num)
            lst = []
            for bucket in buckets:
                lst += bucket
            buckets = [[] for x in range(10)]
            t += 1
        output += lst
        return output
    else:
        return arr


def timings():  # pragma: no cover
    """Generate timings report for insertion sort."""
    import_sort = 'from radix_sort import radix_sort'
    print("""
    Timings for best, average and worst case scenarios for the radix sort.
    --------------------------------------------------------------------------

    """)

    print("3 Best Case Scenarios - sorted except for one value")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst[6], rand_lst[-1] = rand_lst[-1], rand_lst[6]
        best_time = timeit('radix_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))


    print("\n3 Average Case Scenarios - Moderately sorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        shuffle(rand_lst)
        best_time = timeit('radix_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))


    print("\n3 Worst Case Scenarios - Completely unsorted")
    for i in range(3):
        lst_len = randint(9, 50)
        rand_lst = [i for i in range(lst_len)]
        rand_lst = rand_lst[::-1]
        best_time = timeit('radix_sort({})'.format(rand_lst), import_sort)
        print('List {}: length={}; time = {}'.format(i + 1, lst_len, best_time))


if __name__ == '__main__':  # pragma: no cover
    timings()