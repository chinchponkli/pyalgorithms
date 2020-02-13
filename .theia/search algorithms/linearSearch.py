def linearSearch(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(10):
    print (linearSearch(arr, i))