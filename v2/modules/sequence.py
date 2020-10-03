class Sequence:
    def __init__(self, sequence):
        self.value = sequence

    def n_gram(self, n, split_type):
        v = self.value
        rslt = []
        if type(v) is str:
            if split_type is 'word':
                splited = v.split(' ')
                for i in range(0, len(splited)-(n-1)):
                    tmp = ' '.join(splited[i:i+n])
                    rslt.append(tmp)
                return rslt
            elif split_type is 'char':
                splited = v.replace(' ', '')
                for i in range(0, len(splited)-(n-1)):
                    tmp = splited[i:i+n]
                    rslt.append(tmp)
                return rslt
        elif type(v) is list:
            if split_type is 'word':
                for i in range(0, len(v)-(n-1)):
                    tmp = ' '.join(v[i:i+n])
                    rslt.append(tmp)
                return rslt
            elif split_type is 'char':
                s = ''.join(v)
                for i in range(0, len(s)-(n-1)):
                    tmp = s[i:i+n]
                    rslt.append(tmp)
                return rslt
        else:
            pass

    def bi_gram_word(self):
        return self.n_gram(2, 'word')

    def bi_gram_char(self):
        return self.n_gram(2, 'char')