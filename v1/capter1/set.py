# coding:UTF-8
import ngram

target_x = "paraparaparadise"
target_y = "paragraph"

x = ngram.bi_gram_char(target_x)
y = ngram.bi_gram_char(target_y)

# 集合
set_x = set(x)
set_y = set(y)

print('集合')
print(set_x)
print(set_y)
print('')

# 和差積集合　https://www.sejuku.net/blog/21923
# 和集合
union_xy = set_x | set_y
union_xy1 = set_x.union(set_y)

print('和集合')
print(union_xy)
print(union_xy1)
print('')

# 差集合
difference_xy = set_x - set_y
difference_xy1 = set_x.difference(set_y)

print('差集合')
print(difference_xy)
print(difference_xy1)
print('')

# 積集合
intersection_xy = set_x & set_y
intersection_xy1 = set_x.intersection(set_y)

print('差集合')
print(intersection_xy)
print(intersection_xy1)
print('')

# in 'se'?
def search_se(s):
    if 'se' in s:
        print('in se')
    else:
        print('not in se')

search_se(set_x)
search_se(set_y)
