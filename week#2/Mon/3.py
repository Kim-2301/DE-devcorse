def solution1(L, x):
    ans = []
    id = -1 
    try:
        while True:
            id = L.index(x, id + 1)
            ans.append(id)
    except ValueError:
        if not ans:
            ans.append(-1)
    return ans

def solution2(L,x):
    ans = []
    for i in range(len(L)):
        if L[i]==x:
            ans.append(i)
    if not ans:
        ans.append(-1)
        
    return ans