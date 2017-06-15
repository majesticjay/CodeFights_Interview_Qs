def sumOfTwo(a, b, v):

    a = sorted(a)
    b = set(b)

    for x in a:
        if x > v: return False
        c = v-x
        if c in b:
            return True

    return False
