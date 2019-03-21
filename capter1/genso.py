sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = sentence.replace('.', '').split(' ')

genso = {}
tmp = []
for i, word in enumerate(words):
    distinct = i + 1    
    if distinct in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        genso[word[0]] = distinct
    else:
        genso[word[:2]] = distinct

print(genso)
