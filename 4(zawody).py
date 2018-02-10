def zawody(results):
    men=[]
    for i in range(len(results[0])):
        men.append(chr(i+65))
    for i in results:
        men.pop(i.index(min(i)))
    return(men[0])
        
