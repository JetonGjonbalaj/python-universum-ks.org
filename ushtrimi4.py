# d = 3
# a1 = 3

# def arithmeticRecursion(n):
#     if n <= 1:
#         # print('Numri eshte 1')
#         return 1
    
#     # print('Numri eshte ' + str(n))
#     return arithmeticRecursion(n - 1) + d

# def arithmeticRecursion(n):
#     if n <= 1:
#         # print('Numri eshte 1')
#         return a1
    
#     # print('Numri eshte ' + str(n))
#     return arithmeticRecursion(n - 1) + d

# a1 = 3
# n = 7
# d = 3

# def arithmeticRecursion(a1, n, d):
#     if n <= 1:
#         return a1
    
#     return arithmeticRecursion(a1, n-1, d) + d

# print('Numri i kthyer eshte: ' + str(arithmeticRecursion(a1, n, d)))

# a1 = 1
# r = 2
# n = 4

# def geometricRecusion(a1, n, r):
#         if n <= 1:
#             return a1
    
#         return geometricRecusion(a1, n-1, r) * r

# print('Numri i kthyer eshte: ' + str(geometricRecusion(a1, n, r)))

# a1 = 0
# a2 = 1

# for _ in range(int(input('Jepeni numrin: '))):
#     print(a1, end=', ')
#     a1, a2 = a2, a1 + a2

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# matrix2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

matrix3 = []
for i in range(len(matrix1)):
    temp = []
    for j in range(len(matrix1[i])):
        temp.append(matrix1[i][j] + matrix1[i][j])
    
    matrix3.append(temp)

print(matrix3)