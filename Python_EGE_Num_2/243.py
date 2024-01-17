print("X Y Z W F")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = w and (y != (z <= x))
                print (x,y,z,w,int(F))
#ZWYX
