def n_gram(txt, n):
    res = []
    if len(txt) < n:
        return res
    for i in range(len(txt) - n + 1):
        res.append(txt[i:i+n])
    return res

txt1 = "paraparaparadise"
txt2 = "paragraph"
X = set(n_gram(txt1, 2))
Y = set(n_gram(txt2, 2))
print('X: ', X)
print('Y: ', Y)
print('和集合: ', X | Y)
print('積集合: ', X & Y)
print('差集合: ', X - Y)
print("'se'がXに含まれるか？: ", 'se' in X)
print("'se'がYに含まれるか？: ", 'se' in Y)