# vlera = True

# if vlera:
#     print("Ka jepur true")
# else:
#     print("Ka jepur true")

# array = [6876, "kldsjfklds", 90.9, True]

# for i in array:
#     print('vlera eshte: ' + str(i))
# i = 0

# while i != 3:
#     i += 1
#     print(i)


# def printojeVleren(vlera):
#     print("Vlera eshte " + str(vlera))

# printojeVleren(93042309)
# printojeVleren("ldksjfdsl")

# print("Vlera eshte " + str(93042309))

# print("Vlera eshte " + str("LKDSJF"))

def numrat(arr):
    for i in arr:
        if i <= 2:
            return False
    return True

def numrat2(arr, numri):
    # for i in arr:
    #     if i == numri:
    #         return True

    if numri in arr:
        return True

    return False



array = [3, 14, 7, 1, 105]

# print(numrat(array))
print(numrat2(array, 7))
