def maxMin(k, arr):
    unfair = sys.maxsize + 1
    arr = sorted(arr)

    for i in range(len(arr) - k + 1):
        if arr[i + k - 1] - arr[i] < unfair:
            unfair = arr[i + k - 1] - arr[i]

    return unfair