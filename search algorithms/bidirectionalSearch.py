def recursiveBidirectionalSearch(arr, key, l, r):
    if l > r:
        return -1
    if arr[l] == key:
        return l
    if arr[r] == key:
        return r
    return recursiveBidirectionalSearch(arr, key, l + 1, r - 1)

def bidirectionalSearch(arr, key):
    l, r = 0, len(arr) - 1
    while l <= r:
        if arr[l] == key:
            return l
        if arr[r] == key:
            return r
        l, r = l + 1, r - 1
        
arr = [1, 2, 3, 4, 5, 6, 7, 8]
for i in arr:
    print(bidirectionalSearch(arr, i))