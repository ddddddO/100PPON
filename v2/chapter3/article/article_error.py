class ArticleError(Exception):
    pass

class NotExistArticleError(ArticleError):
    def __init__(self, message):
        self.message = message

class UnsupportedTypeError(ArticleError):
    def __init__(self, message):
        self.message = message
