import sys
import random

def generate(text):
    words = split_space(text)
    random_sorted_words = random_sort(words)

    return ' '.join(random_sorted_words)

def split_space(text):
    return text.split(' ')

def random_sort(words):
    rslt_words = []
    for word in words:
        if len(word) > 4:
            chars = list(word)
            first = chars.pop(0)
            last = chars.pop(-1)

            random.shuffle(chars)
            chars.insert(0, first)
            chars.append(last)

            rslt_words.append(''.join(chars))
        else:
            rslt_words.append(word)

    return rslt_words


if __name__=='__main__':
    text = sys.argv[1]
    print(generate(text))
