import random

def bubble_sort(lst):
    """Function to sort a list via optimized bubble sort, O(n^2), Ω(n) if the list is already sorted"""

#Sets a flag so if no swap happened, the loop exits
    sort = True

#Main body of the iterative loop
    while sort:
        sort = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sort = True

    return lst


#Test the algorithm using a randomly generated list of 10 numbers
lst = list(random.randint(0,1000) for i in range(10))
print("Original:               ", lst)
print("Python's sort function: ", sorted(lst))
print("Bubble sort:            ", bubble_sort(lst))