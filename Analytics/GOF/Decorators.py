"""
    This module is to show power of Decorators. We create decorator timer to time the performance of Insertion sort and
    Merge sort. We as well have one more deocrator for naming function.

    run: python Decorators < file.txt

    to get output into file.
"""

def indetifier(func):
    """
    Decorator for naming function.
    :param func:
    :return:
    """
    def w(l):
        from inspect import signature
        print(func.__name__ + " with parrameters length:" + str(signature(func)))
        func(l)
    return w


def timer(func):
    """
    Decorator for timing function.
    :param func:
    :return:
    """


    def wrapper(arr):
        from time import time
        t_start = time()
        func(arr)
        t_end = time()
        print("Function perform task in: " + str(t_end - t_start) + "\n")
    return wrapper


def create_random_array(start=-50000, end=1000000, length=1000):
    """
    Create random Array , unsorted.
    :param start:
    :param end:
    :param length:
    :return:
    """

    from random import randint
    return [randint(start,end ) for i in range(length)]



def merge_sort(alist):
    """
    Merge sort.
        algorithm merge(A, B) is
    inputs A, B : list
    returns list

    C := new empty list
    while A is not empty and B is not empty do
        if head(A) ≤ head(B) then
            append head(A) to C
            drop the head of A
        else
            append head(B) to C
            drop the head of B

    // By now, either A or B is empty. It remains to empty the other input list.
    while A is not empty do
        append head(A) to C
        drop the head of A
    while B is not empty do
        append head(B) to C
        drop the head of B

    return C


    :param alist:
    :return:
    """
    if len(alist) < 0:
        assert "This array cannot exist!!!"
        return -1
    elif 0 <= len(alist) <= 1:
        return alist
    else:
        lefthalf = alist[:int(len(alist)/2)]
        righthalf = alist[int((len(alist)+1)/2):]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    #print("Merging ", alist)
    return alist


def insertion_sort(alist):
    """
    Insertion sort
    i ← 1
    while i < length(A)
        j ← i
        while j > 0 and A[j - 1] > A[j]
            swap
            A[j] and A[j - 1]
            j ← j - 1
        end
        while
            i ← i + 1
    end
    while


    :param alist:
    :return:
    """




    for i,item in enumerate(alist):

        currentvalue = alist[i]
        position = i

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1


########################################################################################################################
### MAIN FUNCTION PREPARE ##############################################################################################
########################################################################################################################


@timer
def main_merge(array):
    merge_sort(array)

@timer
def main_insertion(array):
    insertion_sort(array)


@timer
def python_sort(array):
    sorted(array)

@indetifier
def main(length):
    array = create_random_array(-500000, 1000000,length )
    import copy
    oldarray = copy.copy(array)
    iarray = copy.copy(array)

    #print("old array: ")
    #print(oldarray)
    print("\n")
    print("merge sort time:")
    main_merge(array)
    #print("merge sorted array: ")
    #print(array)
    print("\n")
    print("insertion sort time:")
    main_insertion(iarray)
    #print("insertion sorted array: ")
    #print(iarray)
    print("Python sorted at: ")
    python_sort(array)
if __name__ == '__main__':

    print(10)
    main(10)
    print(100)
    main(100)
    print(1000)
    main(1000)
    print(5000)
    main(5000)
    print(10000)
    main(10000)
    #main(1000000)

