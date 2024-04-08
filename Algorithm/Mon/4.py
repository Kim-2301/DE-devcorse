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