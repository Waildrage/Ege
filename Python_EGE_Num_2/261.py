print("X Y Z W F2 F")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F1 = (w <= y) == (z <= x)
                F2 = (w <= y) and ((not x) == z)
                print (x,y,z,w,int(F1),"",int(F2))
#XZYW
