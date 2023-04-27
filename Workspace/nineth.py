def main(table):
    res = []
    # remove empty rows
    for i in table:
        if i != [None] * len(i):
            res.append(i)

    # try using fromkeys on a dictionary... dictionary has O(1) lookup time
    # and O(1) insertion time so it should be
    # faster than a set and it can act as a set, because of fromkeys, that
    # generates a dictionary of key:none (where)
    # key is the element in the list and none is the value of the key

    # also use zi to transpose the list of lists into a list of tuples,
    # use * to unpack the list of tuples into
    # a list of arguments for the zip function, then use list to turn
    # the zip object into a list of tuples

    # zip(*res) transposes the res
    temp_dict = dict.fromkeys(list(zip(*res)))
    res = list(temp_dict.keys())
    temp_dict = dict.fromkeys(list(zip(*res)))
    # doing it two times we remove duplicates
    res = list(temp_dict.keys())
    res = list(map(list, res))  # turn the tuples into lists
    # print(res)

    for i in range(len(res)):
        temp_set = set()

        # split one element in a row into two by '|'
        t = res[i][1].split('|')
        res[i].pop(1)
        res[i].insert(1, t[1])
        res[i].insert(1 + 1, t[0])

        # switch places of 3rd and 4th columns
        t = res[i][2]
        res[i][2] = res[i][3]
        res[i][3] = t

        # change status format
        res[i][1] = res[i][1].replace('Выполнено', 'Y').\
            replace('Не выполнено', 'N')

        # change date format
        t = res[i][0].split('-')
        res[i][0] = t[0][2:] + '/' + t[1] + '/' + t[2]

        # change percent format
        res[i][2] = round(float(res[i][2][:-1]) / 100, 3)
        res[i][2] = '{:.3f}'.format(res[i][2])

        # change phone format
        res[i][3] = res[i][3].replace('-', ' ', 1)
    return res


a = [[None, None, None, None],
     [None, None, None, None],
     ['2004-11-28', '173-412-7921|Выполнено', '96%', '96%'],
     ['1999-10-04', '236-559-2649|Выполнено', '64%', '64%'],
     ['2004-10-22', '413-025-0326|Выполнено', '87%', '87%'],
     ['2004-10-22', '413-025-0326|Выполнено', '87%', '87%']]

for i in main(a):
    print(i)
