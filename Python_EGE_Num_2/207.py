print("A B C D")
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                F = (not (b <= a)) and (c <= d) and (not (a and b and c and (not d)))
                if F:
                    print(a,b,c,d)
    $#BDCA
