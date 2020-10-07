import os
from urllib.request import urlopen
import MeCab

class Morpheme:
# ------------------------ instance methods ------------------------

    def __init__(self, path_1, path_2):
        self._load_txt_once(path_1)
        self._parse_by_mecab_once(path_1, path_2)

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

        tagger = MeCab.Tagger()
        dest_file = open(dest, 'w')
        src_file = open(src, 'r')

        for line in src_file.readlines():
            parsed = tagger.parse(line).strip()
            dest_file.write(parsed)

        dest_file.close()
        src_file.close()
