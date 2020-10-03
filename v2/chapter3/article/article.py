class Article:
    def __init__(self, src, country):
        '''20. JSONデータの読み込み'''
        target_country = '{"title": "' + country + '",'
        for line in open(src, 'r').readlines():
            if target_country in line:
                self._content = line
                break

        self._extract_category_rows()

    def get_content(self):
        return self._content

    def get_category_rows(self):
        return self._category_rows

# -------- private methods --------

    def _extract_category_rows(self):
        '''21. カテゴリ名を含む行を抽出'''
        begin = self._content.find('[[Category')
        tmp = self._content[begin:]
        end = begin + tmp.find(']]"') + 2
        self._category_rows = self._content[begin:end].split('\\n')