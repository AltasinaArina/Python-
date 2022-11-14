def comb(a):
    b = int(len(a)/1.247)
    while b > 0:
        c = 0
        i = 0
        while i+b < len(a):
            if a[i] > a[i+b]:
                a[i],a[i+b] = a[i+b],a[i]
            i += 1
        if b >= 0:
            b = int(b/1.247)
    return(a)
