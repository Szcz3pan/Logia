def liczby(licz):
    row=[]
    w=[]
    for i in range(len(licz)):
        r=licz[i]
        for j in range(1,licz[i]+1):
            for k in range(1,licz[i]+1):
                if k<j:
                    if j*k==licz[i] and j-k<r:
                        r=j-k
                        x=k
                        y=j
                else:
                    if j*k==licz[i] and k-j<r:
                        r=k-j
                        x=j
                        y=k
        row.append(x)
        row.append(y)
        w.append(row)
        row=[]

    return w
