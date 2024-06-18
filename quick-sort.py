import sys 
sys.setrecursionlimit = 1000000

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 
    for j in range(low, high):

        if arr[j] <=pivot:
            i+=1
            (arr[i],arr[j])=(arr[j],arr[i])
    
    (arr[i+1],arr[high]) = (arr[high],arr[i+1])
    return (i + 1)

def quicksort(arr, low, high):
    if low<high:
        pi = partition(arr,low,high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi+1, high)

nums = [9,7,6,8,9,4,3,5,6,10]

quicksort(nums,0, len(nums)-1)
for i in nums:
    print(i,end=' ')