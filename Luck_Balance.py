def luckBalance(k, contests):
    imp = []
    unimp = []
    # Write your code here
    for elem in contests:
        if elem[1] == 1:
            imp.append(elem[0])
        else:
            unimp.append(elem[0])
    imp = sorted(imp)
    k = min(k, len(imp))

    return sum(unimp) + sum(imp[len(imp) - k:]) - sum(imp[:len(imp) - k])