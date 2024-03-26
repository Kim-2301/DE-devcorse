#인자로 주어지는 리스트 L 내에서, 또한 인자로 주어지는 원소 x 가 발견되는 모든 인덱스를 구하여 이 인덱스들로 이루어진 리스트를 반환하는 함수 solution 을 완성하세요.
#리스트 L 은 정수들로 이루어져 있고 그 순서는 임의로 부여되어 있다고 가정하며, 동일한 원소가 반복하여 들어 있을 수 있습니다. 
#이 안에 정수 x 가 존재하면 그것들을 모두 발견하여 해당 인덱스들을 리스트로 만들어 반환하고, 만약 존재하지 않으면 하나의 원소로 이루어진 리스트 [-1] 를 반환하는 함수를 완성하세요.

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