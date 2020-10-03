from article.download import down_load_article_once
from article.article import Article

if __name__ == '__main__':
    wiki_path = './wiki'
    down_load_article_once(wiki_path)

    country = 'イギリス'
    england_article = Article(wiki_path, country)

    # 20. JSONデータの読み込み
    print(england_article.get_content())
    print('-' * 100)
    print(england_article.get_category_rows())
