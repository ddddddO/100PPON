from article.article import Article
from article.article_error import NotExistArticleError, UnsupportedTypeError

def run(articles):
    if len(articles) == 0:
        raise NotExistArticleError('Need to Generate Article.')

    for article in articles:
        if type(article) is not Article:
            raise UnsupportedTypeError('Only Article type.')

        # 20. JSONデータの読み込み
        print('20. JSONデータの読み込み:\n{src}'.format(src=article.get_content()))
        print('-' * 100)

        # 21. カテゴリ名を含む行を抽出
        print('21. カテゴリ名を含む行を抽出:\n{src}'.format(src=article.get_category_rows()))
        print('-' * 100)

        # 22. カテゴリ名の抽出
        print('22. カテゴリ名の抽出:\n{src}'.format(src=article.get_categories()))
        print('-' * 100)

        # 23. セクション構造
        print('23. セクション構造:')
        article.show_section_and_level_in_content()
        print('-' * 100)

        # 24. ファイル参照の抽出
        print('24. ファイル参照の抽出:\n{src}'.format(src=article.get_media_file_paths()))
        print('-' * 100)

        # 25. テンプレートの抽出/26. 強調マークアップの除去/27. 内部リンクの除去/28. MediaWikiマークアップの除去
        print('25. テンプレートの抽出/26. 強調マークアップの除去/27. 内部リンクの除去/28. MediaWikiマークアップの除去:\n{src}'.format(src=article.get_base_info_map()))
        print('-' * 100)

        # 29. 国旗画像のURLを取得する
        national_flag_image_name = article.get_base_info_map()['国旗画像']
        print('29. 国旗画像のURLを取得する:\n{src}'.format(src=article.get_image_url(national_flag_image_name)))

        print('-' * 100)
        print('-' * 100)
        print('-' * 100)


if __name__ == '__main__':
    try:
        WIKI_PATH = './wiki'
        Article.down_load_article_once(WIKI_PATH)

        articles = [
            Article(WIKI_PATH, 'イギリス'),
            Article(WIKI_PATH, 'トルコ'),
            Article(WIKI_PATH, '日本'),
        ]
        run(articles)

    except NotExistArticleError as err:
        print('NotExistArticleError!: {err}'.format(err=err))
    except UnsupportedTypeError as err:
        print('UnsupportedTypeError!: {err}'.format(err=err))
    except Exception as err:
        print('Exception!: {err}'.format(err=err))
    finally:
        print('Good bye...')