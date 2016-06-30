def printTable(table):
    colWidth = [0] * len(table)

    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > colWidth[i]:
                colWidth[i] = len(table[i][j])

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidth[j], ' '), end=" ")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
