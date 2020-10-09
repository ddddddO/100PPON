class Sentence:
# ------------------------ instance methods ------------------------

    def __init__(self, parsed_list):
        self._mecab_parsed_sentence = parsed_list
        self._mapped_morpheme_a_sentence = self._mapping()

    def get_mapped_morpheme(self):
        return self._mapped_morpheme_a_sentence

    def get_surfaces_by_pos(self, pos):
        l = []
        for mapped in self._mapped_morpheme_a_sentence:
            # TODO: '動詞'以外も増やす
            if mapped['pos'] == '動詞':
                l.append(mapped['surface'])
        return l

    def get_bases_by_pos(self, pos):
        l = []
        for mapped in self._mapped_morpheme_a_sentence:
            # TODO: '動詞'以外も増やす
            if mapped['pos'] == '動詞':
                l.append(mapped['base'])
        return l

    def get_noun_phrases(self):
        l = []
        for i, mapped in enumerate(self._mapped_morpheme_a_sentence):
            if i == 0:
                continue
            if mapped['base'] == 'の' and mapped['pos1'] == '連体化':
                noun_phrase = self._mapped_morpheme_a_sentence[i-1]['surface'] + 'の' + self._mapped_morpheme_a_sentence[i+1]['surface']
                l.append(noun_phrase)
        return l

    def get_noun_articulations(self):
        l = []
        tmp = ''
        for mapped in self._mapped_morpheme_a_sentence:
            if mapped['pos'] == '名詞':
                tmp += mapped['surface']
            else:
                if tmp == '':
                    continue
                l.append(tmp)
                tmp = ''
        return l



# ------------------------ private methods ------------------------

    def _mapping(self):
        l = []
        for parsed in self._mecab_parsed_sentence:
            if parsed[:5] == '記号,空白':
                continue

            morpheme_map = {}
            tmp = parsed.split('\t')
            morpheme_map['surface'] = tmp[0]             # 表層形
            tmp = parsed.split(',')
            morpheme_map['base'] = tmp[6]                # 基本形
            morpheme_map['pos'] = tmp[0].split('\t')[1]  # 品詞
            morpheme_map['pos1'] = tmp[1]                # 品詞細分類1

            l.append(morpheme_map)
        return l