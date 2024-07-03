
def merge(array, left, mid, right):
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid

    leftArray = [0] * subArrayOne
    rightArray = [0] * subArrayTwo

    for i in range(subArrayOne):
        leftArray[i] = array[left + i]

    for j in range(subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    index1 = 0  
    index2 = 0  
    index_merged = left  

    while index1 < subArrayOne and index2 < subArrayTwo:
        if leftArray[index1] <= rightArray[index2]:
            array[index_merged] = leftArray[index1]
            index1 += 1
        else:
            array[index_merged] = rightArray[index2]
            index2 += 1
        index_merged += 1

    while index1 < subArrayOne:
        array[index_merged] = leftArray[index1]
        index1 += 1
        index_merged += 1

    while index2 < subArrayTwo:
        array[index_merged] = rightArray[index2]
        index2 += 1
        index_merged += 1


def mergeSort(array, begin, end):
    if begin >= end:
        return

    mid = begin + (end - begin) // 2
    mergeSort(array, begin, mid)
    mergeSort(array, mid + 1, end)
    merge(array, begin, mid, end)

def printArray(array, size):
    for i in range(size):
        print(array[i], end=" ")
    print()


