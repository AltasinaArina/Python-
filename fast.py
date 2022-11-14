def sort(a, start, end):
    if end - start > 1:
        c = fast(a, start, end)
        sort(a, start, c)
        sort(a, c + 1, end)
def fast(a, start, end):
    b = a[start]
    i = start + 1
    j = end - 1
    while True:
        while (i <= j and a[i] <= b):
            i = i + 1
        while (i <= j and a[j] >= b):
            j = j - 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            a[start], a[j] = a[j], a[start]
            return j