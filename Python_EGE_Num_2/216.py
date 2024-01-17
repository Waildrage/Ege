print("A B C D")
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                F = ((a and b) == (not c)) and (b <= d)
                if F:
                    print (a,b,c,d)
#CDAB
