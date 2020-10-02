sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = sentence.replace(',', '').rstrip('.').split(' ')
pi = []
for w in words:
    pi.append(len(w))

print(pi)
