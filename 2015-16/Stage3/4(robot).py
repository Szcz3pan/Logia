def lnp(n, w, k):
    row=[]
    pp=[]
    for i in range(n):
        for i in range(n):
            row.append(0)
        pp.append(row)
        row=[]
    w-=1
    k-=1
    ki=1
    x=0
    flag=True
    while True:
        pp[w][k]=1
        if ki==1:
            if k+1<n and pp[w][k+1]!=1:
                flag=True
                k+=1
            elif flag:
                ki+=1
                flag=False
            else:
                break

        elif ki==2:
            if w+1<n and pp[w+1][k]!=1:
                flag=True
                w+=1
            elif flag:
                ki+=1
                flag=False
            else:
                break


        elif ki==3:
            if k>0 and pp[w][k-1]!=1:
                flag=True
                k-=1
            elif flag:
                ki+=1
                flag=False
            else:
                break


        elif ki==4:
            if w>0 and pp[w-1][k]!=1:
                flag=True
                w-=1
            elif flag:
                ki=1
                flag=False
            else:
                break
    for i in range(len(pp)):
        x+=pp[i].count(0)
    return x
