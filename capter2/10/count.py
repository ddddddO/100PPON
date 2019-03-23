print('鬮倡衍逵�')

#bytes_sjis = '鬮倡衍'.encode('shift_jis')
bytes_sjis = '逵�'.encode('shift_jis')

print(bytes_sjis)

print(bytes_sjis.decode(encoding='utf-8'))
