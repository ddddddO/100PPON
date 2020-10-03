from modules.sequence_error import UnsupportedTypeError, UnsupportedSplitTypeError

class Sequence:
    def __init__(self, sequence):
        self.value = sequence

    def _n_gram(self, n, split_type):
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
            else:
                raise UnsupportedSplitTypeError('Unsupported split type. Only \'word\' or \'char\'.')
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
                raise UnsupportedSplitTypeError('Unsupported split type. Only \'word\' or \'char\'.')
        else:
            raise UnsupportedTypeError('Unsupported type. Only str or list.')

    def bi_gram_word(self):
        return self._n_gram(2, 'word')

    def bi_gram_char(self):
        return self._n_gram(2, 'char')

    def bi_gram_unsupported_split_type(self):
        return self._n_gram(2, 'xxxxxx')