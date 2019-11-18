def eshteNenbashksi(a, b):
    for value in a:
        if not(value not in a or value in b):
            return False

    return True

def eshteBashkesi(a, b):
    return eshteNenbashksi(a,b) and eshteNenbashksi(b, a)

def gjatesia(a):
    return "Bashkesia i ka " + str(len(a)) + " elemente"

def produktiKartezian(a, b):
    lista = []
    for i in a:
        for j in b:
            lista.append([i, j])

    return lista

def unioni(a, b):
    a.extend(b)
    return a

a = [1, 2, 3, 4, 45]
b = [1, 2, 3, 4, 6]

# tuples = tuple(1, 2, 3)

print(max(a))