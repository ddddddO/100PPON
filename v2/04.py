src = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = src.replace('.', '').split(' ')

elements_dict = {}
for i, element in enumerate(words):
    n = i + 1
    if n in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        elements_dict[element[:1]] = n
    else:
        elements_dict[element[:2]] = n
print(elements_dict)