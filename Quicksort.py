import random

def quicksort(lst):
    """Sorts the list via recursive quicksort, O(n^2), average case nlog(n)"""

#Base case if the list only has 1 or 0 element
    if len(lst) < 2:
        return lst

#Picks a pivot point by selecting the item in the middle, creates 3 empty lists
    pivot = lst[len(lst)//2]
    middle = []
    left = []
    right = []

#Puts numbers into sub-lists depending on whether they are
#bigger than, smaller than, or equal to the pivot
    for i in range(len(lst)):
        if lst[i] < pivot:
            left.append(lst[i])
        elif lst[i] > pivot:
            right.append(lst[i])
        else:
            middle.append(lst[i])

#Return statement combining the three sublists using recursive call
    return quicksort(left) + middle + quicksort(right)

#Test the algorithm using a randomly generated list of 10 numbers
lst = list(random.randint(0,1000) for i in range(10))
print("Original:               ", lst)
print("Python's sort function: ", sorted(lst))
print("Merge sort:             ", quicksort(lst))