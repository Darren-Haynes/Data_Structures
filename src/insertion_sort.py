"""Sort a list using the insertion sort algorithm."""

import timeit

def insertion_sort(lst):
    """Insertion sort."""

    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i+1]:
            # import pdb; pdb.set_trace()
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            j = i
            if j - 1 != -1:
                while lst[j] < lst[j - 1]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                    if j - 1 == 0:
                        break
                    j = j - 1
    return lst

if __name__ == '__main__':
