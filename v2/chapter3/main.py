import article.download as dl
import article.article as al

if __name__ == '__main__':
    wiki_path = './wiki'
    dl.down_load_article_once(wiki_path)

    country = 'イギリス'
    england_article = al.Article(wiki_path, country)

    # 20. JSONデータの読み込み
    print(england_article.get_content())
    print('-' * 100)
    print(england_article.get_category_rows())
