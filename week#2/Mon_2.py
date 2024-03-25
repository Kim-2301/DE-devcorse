#리스트 L 과 정수 x 가 인자로 주어질 때, 리스트 내의 올바른 위치에 x 를 삽입하여 그 결과 리스트를 반환하는 함수 solution 을 완성하세요.
#인자로 주어지는 리스트 L 은 정수 원소들로 이루어져 있으며 크기에 따라 (오름차순으로) 정렬되어 있다고 가정합니다.

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