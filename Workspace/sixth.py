import math


def main(x):
    lookup = {
        'ZIMPL': 12,
        'HTML_MINID_LFE': 11,
        'HTML_MINID_SWIFT': 10,
        'HTML_MINID_NIM': 9,
        'HTML_VUE': 8,
        'HTML_JFLEX': 7,
        'GRACE_MINID': 6,
        'GRACE_VUE_LFE': 5,
        'GRACE_VUE_SWIFT': 4,
        'GRACE_VUE_NIM': 3,
        'GRACE_JFLEX_LFE': 2,
        'GRACE_JFLEX_SWIFT': 1,
        'GRACE_JFLEX_NIM': 0
    }

    key = x[3] + '_' + x[2] + '_' + x[1]
    res = next((k for k in lookup if key.startswith(k)), None)
    return lookup[res]


a = ['IO', 'NIM', 'VUE', 'HTML']
print(main(a))
