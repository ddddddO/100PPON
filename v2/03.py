src = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = src.split(' ')
for i, word in enumerate(words):
    if ',' in word:
        words[i] = word.rstrip(',')
    if '.' in word:
        words[i] = word.rstrip('.')
print(words)

chars_num_list = [len(word) for word in words]
print(chars_num_list)
