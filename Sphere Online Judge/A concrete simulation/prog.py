from sys import stdin

def simulate(queries):
    """
    You are given a matrix M of type 1234x5678.
    It is initially filled with integers 1...1234x5678 in row major order.
    Your task is to process a list of commands manipulating M. There are 4 types of commands:

    "R x y" swap the x-th and y-th row of M ;
    "C x y" swap the x-th and y-th column of M ;
    "Q x y" write out M(x,y) ;
    "W z" write out x and y where z=M(x,y).
    """

    rowMap = [i for i in range(1235)]
    colMap = [i for i in range(5679)]
    undoRowMap = [i for i in range(1235)]
    undoColMap = [i for i in range(5679)]

    for q in queries:
        if q[0] == "R":
            undoRowMap[rowMap[q[1]]], undoRowMap[rowMap[q[2]]] = undoRowMap[rowMap[q[2]]], undoRowMap[rowMap[q[1]]]
            rowMap[q[1]], rowMap[q[2]] = rowMap[q[2]], rowMap[q[1]]
            
        elif q[0] == "C":
            undoColMap[colMap[q[1]]], undoColMap[colMap[q[2]]] = undoColMap[colMap[q[2]]], undoColMap[colMap[q[1]]]
            colMap[q[1]], colMap[q[2]] = colMap[q[2]], colMap[q[1]]
        elif q[0] == "Q":
            row = rowMap[q[1]]
            col = colMap[q[2]]
            print((row-1)*5678+col)
        else:
            num = q[1]
            y = (num % 5678) if num % 5678 != 0 else 5678
            x = (num-y)//5678 + 1
            row = undoRowMap[x]
            col = undoColMap[y]
            print(f"{row} {col}")

if __name__ == "__main__":
    queries = []
    for line in stdin:
        queries.append(line.split())

    for i in range(len(queries)):
        for j in range(1, len(queries[i])):
            queries[i][j] = int(queries[i][j])

    simulate(queries)
