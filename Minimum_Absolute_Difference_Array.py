def minimumAbsoluteDifference(arr):
    # Write your code here
    if len(arr) != len(set(arr)):
        return 0

    arr = sorted(arr)

    macs = sys.maxsize + 1

    for i in range(len(arr) - 1):

        if abs(arr[i] - arr[i + 1]) < macs:
            macs = abs(arr[i] - arr[i + 1])

    return macs