txt = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = txt.split()
dic = {}
for i in range(len(words)):
    if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        word = words[i][0]
    else:
        word = words[i][:2]
    dic[word] = i + 1
print(dic)