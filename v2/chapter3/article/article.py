import re
import os
import gzip
from urllib.request import urlopen

class Article:

# ------------------------ class method ------------------------

    @classmethod
    def down_load_article_once(cls, dest):
        if cls._exist_article(dest):
            return

        url = 'https://nlp100.github.io/data/jawiki-country.json.gz'
        response = urlopen(url)

        gzip_file = gzip.GzipFile(fileobj=response)
        content = gzip_file.read()

        file = open(dest, 'w')
        file.write(content.decode('utf-8'))

# ------------------------ instance methods ------------------------

    def __init__(self, src, country):
        self._load_json_data(src, country)
        self._extract_category_rows()
        self._extract_categories_in_rows()
        self._mapping_section_and_level()
        self._extract_media_file_paths()
        self._mapping_base_informateion()

    def get_content(self):
        return self._content

    def get_category_rows(self):
        return self._category_rows

    def get_categories(self):
        return self._categories

    def show_section_and_level_in_content(self):
        for k in self._section_lv_map:
            print('level: {lv}\nsections: {list}\n'.format(lv=k, list=self._section_lv_map[k]))

    def get_media_file_paths(self):
        return self._media_file_paths

    def get_base_info_map(self):
        return self._base_info_map

# ------------------------ private methods ------------------------

    @classmethod
    def _exist_article(cls, path):
        return os.path.isfile(path)

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
        compiled_category_pattern = re.compile(r'(?<=Category:).+(?=]])')
        categories = []
        for row in self._category_rows:
            serched_match = compiled_category_pattern.search(row)
            if serched_match is None:
                # TODO: raise exception
                pass
            categories.append(serched_match.group())
        self._categories = categories

    def _mapping_section_and_level(self):
        '''23. セクション構造'''
        compiled_section_lv1_pattern = re.compile(r'={2}([^(=\n)]+)={2}[^=]')
        compiled_section_lv2_pattern = re.compile(r'={3}([^(=\n)]+)={3}[^=]')
        compiled_section_lv3_pattern = re.compile(r'={4}([^(=\n)]+)={4}[^=]')

        section_lv1_list = compiled_section_lv1_pattern.findall(self._content)
        section_lv2_list = compiled_section_lv2_pattern.findall(self._content)
        section_lv3_list = compiled_section_lv3_pattern.findall(self._content)

        self._section_lv_map = {
            1: section_lv1_list,
            2: section_lv2_list,
            3: section_lv3_list,
        }

    def _extract_media_file_paths(self):
        '''24. ファイル参照の抽出'''
        # FIXME: 抜け漏れ正規表現
        compiled_media_file_path_pattern = re.compile(r'ファイル:(.+?)[]|\|]')
        self._media_file_paths = compiled_media_file_path_pattern.findall(self._content)

    def _mapping_base_informateion(self):
        '''25. テンプレートの抽出'''
        # インスタンス国記事から「基礎情報」を抜き出す
        compiled_base_info_pattern = re.compile(r'{{基礎情報(.+?)\\n}}')
        base_info = compiled_base_info_pattern.findall(self._content)[0]

        # 抜き出した「基礎情報」からkey/valueを抜き出す
        compiled_key_value_pattern = re.compile(r'\\n\|(.+?=.+?)(?=\\n)')
        base_info_kv_list = compiled_key_value_pattern.findall(base_info)

        # 抜き出したkey/valueを各々空白をトリムして辞書型変数に格納
        self._base_info_map = {}
        for kv in base_info_kv_list:
            tmp = kv.split('=')
            k = tmp[0].strip()
            v = self._trim(tmp[1])
            self._base_info_map[k] = v

    def _trim(self, value):
        tmp = self._trim_media_wiki_tag(
                self._trim_internal_link_tag(
                    self._trim_strong_tag(
                        value.strip()
                    )
                )
            )
        return tmp

    def _trim_strong_tag(self, value):
        '''26. 強調マークアップの除去'''
        tmp = re.sub('\'\'\'\'\'', '', value)
        tmp = re.sub('\'\'\'', '', tmp)
        tmp = re.sub('\'\'', '', tmp)
        return tmp

    def _trim_internal_link_tag(self, value):
        '''27. 内部リンクの除去'''
        tmp = re.sub(r'\[\[', '', value)
        tmp = re.sub(r'\]\]', '', tmp)
        return tmp

    def _trim_media_wiki_tag(self, value):
        '''28. MediaWikiマークアップの除去'''
        tmp = re.sub('{{', '', value)
        tmp = re.sub('}}', '', tmp)
        return tmp