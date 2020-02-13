def linearSearch(arr, key, l, r):
    if l > r:
        return -1
    if arr[l] == key:
        return l
    if arr[r] == key:
        return r
    return linearSearch(arr, key, l + 1, r - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
for i in arr:
    print(linearSearch(arr, i, 0, len(arr) - 1))