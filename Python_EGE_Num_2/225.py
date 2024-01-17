print("X Y Z W")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((y or x) == (y <= w)) or (not z)
                if (not F):
                    print(x,y,z,w)
#?
