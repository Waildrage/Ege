print("X Y Z W")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = (x <= (not z)) and (y <= x)
            if F:
                print (x,y,z)
#YZX
