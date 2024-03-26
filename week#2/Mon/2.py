def solution1(L, x):
    L.append(x)
    L.sort()
    return L

def solution2(L, x):
    for i in range(len(L)):
        if L[i] >= x:
            L.insert(i, x)
            return L
    L.append(x)
    return L