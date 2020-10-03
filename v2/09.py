import random

def typoglycemia(origin):
    random.seed()

    generated = []
    words = origin.split(' ')
    for _, word in enumerate(words):
        if len(word) >= 4:
            begin_char = word[0]
            end_char = word[-1]
            seq = [i for i in range(1, len(word)-1)]
            random.shuffle(seq)

            shuffle_word = begin_char
            for i in seq:
                shuffle_word += word[i]
            shuffle_word += end_char

            generated.append(shuffle_word)
        else:
            generated.append(word)
    return ' '.join(generated)

src = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print('origin: \n{src}\n'.format(src=src))
print('typoglycemiazation: \n{gen}'.format(gen=typoglycemia(src)))