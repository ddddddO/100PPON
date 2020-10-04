from article.download import down_load_article_once
from article.article import Article

if __name__ == '__main__':
    wiki_path = './wiki'
    down_load_article_once(wiki_path)

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
