import random

def selection_sort(lst):
    """Function to sort a list via insertion sort, O(n^2) always"""

    for i in range(len(lst)):
        minimum = i

#For each cycle, finds the next smallest number and assign to "minimum"
        for j in range(i+1, len(lst)):
            if lst[minimum] > lst[j]:
                minimum = j

#Swaps the i th number with the next smallest number
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst

#Test the algorithm using a randomly generated list of 10 numbers
lst = list(random.randint(0,1000) for i in range(10))
print("Original:               ", lst)
print("Python's sort function: ", sorted(lst))
print("Selection sort:         ", selection_sort(lst))