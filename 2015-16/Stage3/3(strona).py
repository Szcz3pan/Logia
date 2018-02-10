def maxu(u):
    x=0
    m=0
    for i in range(len(u)):
        if sum(u[i])>x:
            x=sum(u[i])-1
            
    lu=[0 for i in range(x)]
    for i in range(len(u)):
        for j in range(u[i][0]-1, sum(u[i])-1):
            lu[j]+=1
            if lu[j]>m:
                m=lu[j]

    return m
    
    
