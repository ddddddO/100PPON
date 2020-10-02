# coding:UTF-8
# https://docs.python.org/ja/3.5/library/string.html

from string import Template

def ret_tenki(x, y, z):
    t = Template('$time時の$textは$temp')
    return t.safe_substitute(time=x, text=y, temp=z)

print(ret_tenki(x=12, y="気温", z=22.4))
