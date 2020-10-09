from morpheme.analyzer import Analyzer
import matplotlib.pyplot as plt

if __name__=='__main__':
    RAW_TXT_PATH = './neko.txt'
    MECAB_PARSED_TXT_PATH = './neko.txt.mecab'

    neko = Analyzer(RAW_TXT_PATH, MECAB_PARSED_TXT_PATH)
    sentences = neko.get_sentences()

    print('30. 形態素解析結果の読み込み')
    for sentence in sentences:
        print(sentence.get_mapped_morpheme())
    print('-' * 100)

    print('31. 動詞')
    for sentence in sentences:
        surfaces = sentence.get_surfaces_by_pos('動詞')
        if len(surfaces) == 0:
            continue
        print(surfaces)
    print('-' * 100)

    print('32. 動詞の原形')
    for sentence in sentences:
        bases = sentence.get_bases_by_pos('動詞')
        if len(bases) == 0:
            continue
        print(bases)
    print('-' * 100)

    print('33. 「AのB」')
    for sentence in sentences:
        noun_phrases = sentence.get_noun_phrases()
        if len(noun_phrases) == 0:
            continue
        print(noun_phrases)
    print('-' * 100)

    print('34. 名詞の連接')
    for sentence in sentences:
        noun_articulations = sentence.get_noun_articulations()
        if len(noun_articulations) == 0:
            continue
        print(noun_articulations)
    print('-' * 100)

    print('35. 単語の出現頻度')
    print(neko.get_frequency_of_appearance())
    print('-' * 100)

    # NOTE: .ipynd
    # print('36. 頻度上位10語')
    # tmp = neko.get_frequency_of_appearance(10)
    # x = range(0, len(tmp))
    # height = [tp[1] for tp in tmp]
    # label  = [tp[0] for tp in tmp]
    # plt.bar(x, height, tick_label = label)
    # print('-' * 100)