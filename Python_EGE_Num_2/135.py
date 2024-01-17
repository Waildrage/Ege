print("X Y Z W")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (not y) and x and ((not z) or w )
                if F == 1:
                    print(x ,y,z,w)

#WXZY
