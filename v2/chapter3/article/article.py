class Article:
    def __init__(self, src, country):
        '''20. JSONデータの読み込み'''

        target_country = '{"title": "' + country + '",'
        for line in open(src, 'r').readlines():
            if target_country in line:
                self.content = line
                return
        #raise

    def get_content(self):
        return self.content