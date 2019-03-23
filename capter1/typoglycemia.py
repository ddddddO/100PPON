import sys

def generate(text):
    words = split_space(text)
    random_sorted_words = random_sort(words)

    return ' '.join(random_sorted_words)

def split_space(text):
    return text.split(' ')

def random_sort(words):
    return ''


if __name__=='__main__':
    text = sys.argv[1]
    print(generate(text))
    


    