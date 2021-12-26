# not mine, ofc ... I wish I was so good ...
# i debugged the shit out of it in order to understand what the dude did here ... dude! wtf! what do you smoke?
# you're welcome for the mnemonic variables; delete all of those prints if you already figured out the whole thing

def countInversions(arr):
    print('\narr (as a function arg) = ', arr)

    if len(arr) == 1:
        return 0

    len_1st_half = len(arr) // 2
    len_2nd_half = len(arr) - len_1st_half

    st1_half = arr[:len_1st_half]
    nd2_half = arr[len_1st_half:]
    print('1st half =', st1_half)
    print('2nd half =', nd2_half)

    inversions = countInversions(st1_half) + countInversions(nd2_half)

    print('\ninversions =', inversions, '\n*************************')
    iter_1st = 0
    iter_2nd = 0

    print('arr just before the loop', arr, '\n')

    for i in range(len(arr)):
        print('i=', i, '\n------------------------')
        print('iter_1st =', iter_1st)
        print('iter_2nd =', iter_2nd, '\n')
        print('len 1st half =', len_1st_half, '-----len 2nd half =', len_2nd_half)
        if iter_1st < len_1st_half and (iter_2nd >= len_2nd_half or st1_half[iter_1st] <= nd2_half[iter_2nd]):
            print('arr before arrange-1st rule =', arr)
            arr[i] = st1_half[iter_1st]
            inversions += iter_2nd
            iter_1st += 1
            print('1st rule- arr =', arr)
            print('inversions =', inversions)
            print('iter_1st =', iter_1st, '\n')
        elif iter_2nd < len_2nd_half:
            print('arr before arrange-2nd rule =', arr)
            arr[i] = nd2_half[iter_2nd]
            iter_2nd += 1
            print('2nd rule- arr =', arr)
            print('iter_2nd =', iter_2nd, '\n')

    return inversions


a = [4, 2, 3, 5, 0]
print(countInversions(a))

# Merge Sort
#When we merge two sorted arrays, left and right, we must put the element from right into the new, sorted array if it is smaller than the element in left (i.e., out of order).
# This effectively indirectly shifts the element to the left by the number of elements remaining in the first array, but does it with a complexity of O(n * log(n)).
# Thus, we simply need to implement Merge Sort and add the shift whenever the element in the right array is less than the element in the left array.