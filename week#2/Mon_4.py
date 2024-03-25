#리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 
#만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 
#리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 
#또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

def solution(L, x):
    low = 0
    up = len(L) - 1
    
    while low <= up:
        mid = (low + up) // 2
        
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            low = mid + 1
        else:
            up = mid - 1
            
    return -1