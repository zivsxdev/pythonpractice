def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = [3,4,5,6,77]
print(find_largest(arr))
