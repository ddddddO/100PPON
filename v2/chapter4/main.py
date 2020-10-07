from morpheme.morpheme import Morpheme

if __name__=='__main__':
    RAW_TXT_PATH = './neko.txt'
    MECAB_PARSED_TXT_PATH = './neko.txt.mecab'

    neko = Morpheme(RAW_TXT_PATH, MECAB_PARSED_TXT_PATH)
