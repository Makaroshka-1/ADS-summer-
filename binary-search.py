def binary_search(arr,low, high, val):
    if high>=low:
        mid = high - (high-low)/2
        if arr[mid]==val:
            return mid
        elif arr[mid]<val:
            return binary_search(arr, low, mid-1,val)
        else:
            return binary_search(arr,mid+1,high, val)
    else:
        return -1
    