'''
Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
'''

def binarySearch(arr, key):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def binarySearchRecursive(arr, key, l, r):
    if l > r:
        return -1
    mid = (l + r) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarySearchRecursive(arr, key, mid + 1, r)
    else:
        return binarySearchRecursive(arr, key, l, mid - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
l, r = 0, len(arr) - 1
for i in range(10):
    print(binarySearch(arr, i))
    print(binarySearchRecursive(arr, i, l, r))