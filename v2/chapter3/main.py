from article.article import Article

if __name__ == '__main__':
    wiki_path = './wiki'
    Article.down_load_article_once(wiki_path)

    country = 'イギリス'
    england_article = Article(wiki_path, country)

    # 20. JSONデータの読み込み
    print('20. JSONデータの読み込み:\n{src}'.format(src=england_article.get_content()))
    print('-' * 100)

    # 21. カテゴリ名を含む行を抽出
    print('21. カテゴリ名を含む行を抽出:\n{src}'.format(src=england_article.get_category_rows()))
    print('-' * 100)

    # 22. カテゴリ名の抽出
    print('22. カテゴリ名の抽出:\n{src}'.format(src=england_article.get_categories()))
    print('-' * 100)

    # 23. セクション構造
    print('23. セクション構造:')
    england_article.show_section_and_level_in_content()
    print('-' * 100)

    # 24. ファイル参照の抽出
    print('24. ファイル参照の抽出:\n{src}'.format(src=england_article.get_media_file_paths()))
    print('-' * 100)

    # 25. テンプレートの抽出/26. 強調マークアップの除去
    print('25. テンプレートの抽出/26. 強調マークアップの除去:\n{src}'.format(src=england_article.get_base_info_map()))
    print('-' * 100)