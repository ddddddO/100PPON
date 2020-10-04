import re

class Article:
    _compiled_category_pattern = re.compile(r'(?<=Category:).+(?=]])')

    def __init__(self, src, country):
        self._load_json_data(src, country)
        self._extract_category_rows()
        self._extract_categories_in_rows()

    def get_content(self):
        return self._content

    def get_category_rows(self):
        return self._category_rows

    def get_categories(self):
        return self._categories

# ------------------------ private methods ------------------------

    def _load_json_data(self, src, country):
        '''20. JSONデータの読み込み'''
        target_country = '{"title": "' + country + '",'
        for line in open(src, 'r').readlines():
            if target_country in line:
                self._content = line
                return

    def _extract_category_rows(self):
        '''21. カテゴリ名を含む行を抽出'''
        begin = self._content.find('[[Category')
        tmp = self._content[begin:]
        end = begin + tmp.find(']]"') + 2
        self._category_rows = self._content[begin:end].split('\\n')

    def _extract_categories_in_rows(self):
        '''22. カテゴリ名の抽出'''
        categories = []
        for row in self._category_rows:
            serched_match = self._compiled_category_pattern.search(row)
            if serched_match is None:
                # TODO: raise exception
                pass
            categories.append(serched_match.group())
        self._categories = categories
