from unittest import result


word_p = "パトカー"
word_t = "タクシー"

result = ""
for i in range (len(word_p)):
    result += word_p[i] + word_t[i]
    print(result)
