#https://kotobank.jp/word/N%E3%82%B0%E3%83%A9%E3%83%A0-1702302

def bi_gram_word(target):
    words = target.replace(',', '').rstrip('.').split(' ')
    bi_gram_list = []

    for i in range(len(words)-1):
        bi_gram = words[i] + words[i+1]
        bi_gram_list.append(bi_gram)

    return bi_gram_list

def bi_gram_char(target):
    text = target.replace(' ', '')
    bi_gram_list = []

    for i in range(len(text)-1):
         bi_gram = text[i:i+2]
         bi_gram_list.append(bi_gram)

    return bi_gram_list


if __name__=='__main__':
    target = "I am an NLPer"

    print('src: {}'.format(target))
    print(bi_gram_word(target))
    print(bi_gram_char(target))
