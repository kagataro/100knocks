txt = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
txt = txt.replace(',', '') 
txt = txt.replace('.', '') 
words = txt.split() 
words_len = [len(x) for x in words]
print(words_len)