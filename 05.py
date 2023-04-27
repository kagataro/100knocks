def n_gram(txt, n):
    res = []
    if len(txt) < n:
        return res
    for i in range(len(txt) - n + 1):
        res.append(txt[i:i+n])
    return res


txt = "I am an NLPer"
print('文字bi-gram: ', n_gram(txt, 2))
print('単語bi-gram: ', n_gram(txt.split(), 2))