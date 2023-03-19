import math
import re


def main(stri):
    stri = stri.replace(' ', '')
    stri = stri.replace('\n', '')
    stri = stri.replace('\t', '')
    res = []
    for i in re.findall(r'set@"(.*?)"<=\'(.*?)\'', stri):
        res.append(i)
    return res


a = 'do<sect> set @"isedor" <= \'riqu\'</sect>, <sect> set @"dige_966" <=' \
    '\'onoris_94\' </sect>, <sect>set @"sogele_278"<= \'maerle\'</sect>, done'
print(main(a))
