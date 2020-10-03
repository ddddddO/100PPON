import os
import gzip
from urllib.request import urlopen

def down_load_article_once(dest):
    if _exist_article(dest):
        return

    url = 'https://nlp100.github.io/data/jawiki-country.json.gz'
    response = urlopen(url)

    gzip_file = gzip.GzipFile(fileobj=response)
    content = gzip_file.read()

    file = open(dest, 'w')
    file.write(content.decode('utf-8'))

def _exist_article(path):
    return os.path.isfile(path)