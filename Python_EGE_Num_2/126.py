print("A B C F")
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            F = (a or (not c)) and ((not a) or b or c)
            print (a,b,c,int(F))
#CBA
            
