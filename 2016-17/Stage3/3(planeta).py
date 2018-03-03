def distance(size, address1, address2):
    dist=0
    dist+=min(abs(address1[0]-address2[0]), address1[0]+size-address2[0], size-address1[0]+address2[0])
    dist+=min(abs(address1[1]-address2[1]), address1[1]+size-address2[1], size-address1[0]+address2[0])
    return dist

def planeta(size, address):
    districts=[]
    for x,y in enumerate(address):
        for j in address[x:]:
            flag=True
            if distance(size, y, j)<=5:
                for k in districts:
                    if y in k or j in k:
                        flag=False
                        k.append(y)
                        k.append(j)
                if flag:
                    districts.append([])
                    districts[-1].append(y)
                    districts[-1].append(j)
    temp2=[]
    maxlen=0
    for i in districts:
        temp=[]
        for j in i:
            if j not in temp:
                temp.append(j)
        temp2.append(temp)
        if len(temp)>maxlen:
            maxlen=len(temp)
            
    return maxlen
