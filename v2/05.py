import modules.sequence as mod
#import modules.sequence_error as mod_err

src_0 = 'I am an NLPer'
print('input sequence: {value}'.format(value=src_0))
seq_0 = mod.Sequence(src_0)
print(seq_0.bi_gram_word())
print(seq_0.bi_gram_char())

print('-' * 70)

src_1 = ['I', 'am', 'not', 'an' , 'NLPer']
print('input sequence: {value}'.format(value=src_1))
seq_1 = mod.Sequence(src_1)
print(seq_1.bi_gram_word())
print(seq_1.bi_gram_char())

print('-' * 70)

try:
    seq_1.bi_gram_unsupported_split_type()
except Exception as err:
    print('raise exception!')
    print(err)
finally:
    print('Good bye')