from article.article import Article
from unittest import TestCase

class TestArticle(TestCase):
    def setUp(self):
        self.article = Article('./chapter3/tests/fixtures/wiki_data', 'イギリス')

    def test_get_content(self):
        self.assertTrue(len(self.article.get_content()) > 0)

    def test_get_category_rows(self):
        self.assertTrue(len(self.article.get_category_rows()) > 0)