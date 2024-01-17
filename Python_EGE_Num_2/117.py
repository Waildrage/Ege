print("A B C F")
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            print(a,b,c,int((a and (not c))or ((not b)and(not c))))
#ABC
