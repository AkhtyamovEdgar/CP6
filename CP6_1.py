def general(lst1, lst2):
    res = set()
    if len(lst1) >= len(lst2):
        for i in range(0, len(lst1)):
            if lst1[i] in lst2:
                if lst1[i] not in res:
                    res.add(lst1[i])
    else:
        for i in range(0, len(lst2)):
            if lst2[i] in lst1:
                if lst2[i] not in res:
                    res.add(lst2[i])
    print("Элементы, содержащиеся в обоих массивах: ", *res)

dimA = int(input('Введите размерность массива А: '))
A = []
for _ in range(dimA):
    variable = int(input('Введите элемент массива А: '))
    A.append(variable)
dimB = int(input('Введите размерность массива B: '))
B = []
for _ in range(dimB):
    variable = int(input('Введите элемент массива B: '))
    B.append(variable)
general(A, B)



