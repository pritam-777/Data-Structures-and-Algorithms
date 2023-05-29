def find_pair(arr, x):
    n = len(arr)
    # find pivot element
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i + 1
            break
    left = pivot
    right = pivot - 1
    while left != right:
        if arr[left] + arr[right] == x:
            return True
        elif arr[left] + arr[right] < x:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n
    return False
 
arr = [11, 15, 6, 8, 9, 10]
x = 16
print(find_pair(arr, x))