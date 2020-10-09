import os
from urllib.request import urlopen
import MeCab
from morpheme.sentence import Sentence

class Analyzer:
# ------------------------ instance methods ------------------------

    def __init__(self, path_1, path_2):
        self._load_txt_once(path_1)
        self._parse_by_mecab_once(path_1, path_2)
        self._load_mecab_parsed_txt(path_2)

    def get_sentences(self):
        return self._sentences

    def get_frequency_of_appearance(self, top=0):
        self._calc_frequency_of_appearance()

        if top == 0:
            return self._frequency_of_appearance
        return self._frequency_of_appearance[:top]

# ------------------------ private methods ------------------------

    def _load_txt_once(self, dest):
        if os.path.isfile(dest):
            return

        # ダウンロード
        url = 'https://nlp100.github.io/data/neko.txt'
        response = urlopen(url)

        f = open(dest, 'wb')
        f.write(response.read())
        f.close()

    def _parse_by_mecab_once(self, src, dest):
        if os.path.isfile(dest):
            return

        # output: 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
        tagger = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
        dest_file = open(dest, 'w')
        src_file = open(src, 'r')

        for line in src_file.readlines():
            parsed = tagger.parse(line).strip()
            dest_file.write(parsed.replace('EOS', ''))

        dest_file.close()
        src_file.close()

    def _load_mecab_parsed_txt(self, src):
        f = open(src, 'r')

        self._sentences = []
        sentence = []
        for mecab_parsed_line in f.readlines():
            sentence.append(mecab_parsed_line)

            # 文末判定
            if mecab_parsed_line[0] == '。':
                s = Sentence(sentence)
                self._sentences.append(s)
                sentence = []
                continue

        f.close()

    def _calc_frequency_of_appearance(self):
        tmp_dict = {}
        for sentence in self._sentences:
            for mapped in sentence.get_mapped_morpheme():
                key = mapped['surface']
                if key not in tmp_dict:
                    tmp_dict[key] = 1
                else:
                    tmp_dict[key] = tmp_dict[key] + 1
        self._frequency_of_appearance = sorted(tmp_dict.items(), key = lambda x : x[1], reverse=True)
