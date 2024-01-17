print("X Y Z W")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = ((not x) or y or z)and((not x) or (not z))
            if not F:
                print(x,y,z)
#YZX                
