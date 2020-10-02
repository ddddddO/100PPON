# coding:UTF-8

# http://yono.cc/python/python_basics/japanese.html unicode変換
target = "パタトクカシーー"
u_target = unicode(target, 'utf-8')

char_list = list(u_target)
print(char_list[0] + char_list[2] + char_list[4] + char_list[6])