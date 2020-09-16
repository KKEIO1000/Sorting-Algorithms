import random

def mergesort(lst):
    """Sorts the list via recursive mergesort, Θ(nlog(n))"""

#Base case if the list only has 1 element
    if len(lst) == 1:
        return lst

#Divides the list into two sorted halves using recursive call
    top = mergesort(lst[:len(lst)//2])
    bottom = mergesort(lst[len(lst)//2:])

#Joins the two halves using mergesort algorithm
    comb = []
    i, j, k = 0, 0, 0
    while i < len(top) and j < len(bottom):
        if top[i] < bottom[j]:
            comb.append(top[i])
            i += 1
        else:
            comb.append(bottom[j])
            j += 1

    if i < len(top):
        comb.extend(top[i:])
    else:
        comb.extend(bottom[j:])

#Return statement
    return comb

#Test the algorithm using a randomly generated list of 10 numbers
lst = list(random.randint(0,1000) for i in range(10))
print("Original:               ", lst)
print("Python's sort function: ", sorted(lst))
print("Merge sort:             ", mergesort(lst))