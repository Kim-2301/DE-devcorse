def solution(participant, completion):
    d = {}
    for x in  participant:
        d[x] = d.get(x,0)+1
        
    for x in completion:
        d[x] -= 1
        
    fail = [k for k,v in d.items() if v>0]
    
    return fail[0]