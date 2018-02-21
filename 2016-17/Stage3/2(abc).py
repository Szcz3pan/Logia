def abc(order):
    order=[char for char in order if char in ['n','c','z']]
    for i in range(len(order)):
        if order[i]=='n':
            order[i]=1
        elif order[i]=='c':
            order[i]=2
        else:
            order[i]=3
    
    inc=[1]*len(order)
    for i in range(1, len(order)):
        for j in range(i):
            if order[i]>=order[j] and inc[i]<=inc[j]:
                inc[i]=inc[j]+1
    
    return len(order)-max(inc)
