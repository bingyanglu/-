

print (selectionSort([5,8,9,10,6,15,2,1,3,4]))
def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(1,len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
#     print(biggest_index)
    return biggest_index
​
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        biggest = findBiggest(arr)
        newArr.append(arr.pop(biggest))
    return newArr
​
print (selectionSort([5,8,9,10,6,15,2,1,3,4]))
