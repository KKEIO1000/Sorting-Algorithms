import random

def insertion_sort(lst):
    """Function to sort a list via insertion sort, O(n^2), Ω(n) if the list is already sorted"""

    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1

#Swap leftward until seeing a smaller number
        while j>=0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

    return lst

#Test the algorithm using a randomly generated list of 10 numbers
lst = list(random.randint(0,1000) for i in range(10))
print("Original:               ", lst)
print("Python's sort function: ", sorted(lst))
print("Insertion sort:         ", insertion_sort(lst))
