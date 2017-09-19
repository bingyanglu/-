def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quicksort(greater) + [pivot] + quicksort(less)

print(quicksort([10,5,2,9,4,6,8]))