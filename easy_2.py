a = [1, 3, 7, 12, 15, 19, 22]
b = [2, 3, 7, 9, 13, 16, 18, 21, 24]
c = [2, 4, 5, 8, 10, 11, 13, 14, 17, 21, 23]
d = [1, 2, 4, 6, 9, 13, 16, 19, 21, 22, 24, 25]

# лежит в (а или б) и в д, но не в с

ans = [i for i in d if i in a or i in b and i not in c]
print(*ans)
