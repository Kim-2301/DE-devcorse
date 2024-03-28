def solution1(n, lost, reserve):
    uni = [1] * (n+2)
    for i in reserve:
        uni[i] += 1
    for i in lost:
        uni[i] -= 1
    for i in range(1,n+1):
        if uni[i] == 2 and uni[i-1] == 0:
            uni[i-1 : i+1] = [1,1]
        elif uni[i] == 2 and u[i+1] == 0:
            uni[i:i+2] = [1,1]
    cnt = [x for x in uni[1:-1] if uni[x]>0]
    return len(cnt)


def solution2(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s

    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    return n - len(l)