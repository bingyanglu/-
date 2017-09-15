# 找到最小的元素
def findSmallest(arr):
#     定义变量用来存放最小的元素，初始值为数组中的第一个元素
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
#         如果有元素小于smallest 则将其赋值给smallest 返回值为下标
#         该函数用来找到最小的元素
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
#       使用函数找到最小的元素
        smallest = findSmallest(arr)
#     在原数组中删除，添加在新数组中  pop返回删除的元素
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5,8,9,10,6,15,2,1,3,4]))