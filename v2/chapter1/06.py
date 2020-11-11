import modules.sequence as mod

def to_set(src):
    seq = mod.Sequence(src)
    seq_bi_gram_list = seq.bi_gram_char()
    return set(seq_bi_gram_list)

src_x = 'paraparaparadise'
src_y = 'paragraph'
src_x_set = to_set(src_x)
src_y_set = to_set(src_y)

print('src_x_set: {sx}'.format(sx = src_x_set))
print('src_y_set: {sy}'.format(sy = src_y_set))

print('-' * 70)

print('Union: {union}'.format(union = src_x_set | src_y_set))
print('Intersection: {intersection}'.format(intersection = src_x_set & src_y_set))
print('Difference Set(x-y): {difference}'.format(difference = src_x_set - src_y_set))
print('Difference Set(y-x): {difference}'.format(difference = src_y_set - src_x_set))

print('-' * 70)

def exist(s, src_set):
    ans = ''
    if s <= src_set:
        ans = 'yes'
    else:
        ans = 'no'
    return ans

ans_x = exist({'se'}, src_x_set)
ans_y = exist({'se'}, src_y_set)
print('"se" in x?: {ans}'.format(ans = ans_x))
print('"se" in y?: {ans}'.format(ans = ans_y))