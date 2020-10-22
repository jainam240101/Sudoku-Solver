board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def valid(bo, number, pos):
    # check on rows 
    for i in range(len(bo[0])):
        if (bo[pos[0]][i] == number and pos[1] != i):
            return False

    #check on cols 
    for i in range(len(bo[1])):
        if (bo[i][pos[1]] == number and pos[0] != i):
            return False

    #check for boxes
    box_x=pos[0]//3 
    box_y = pos[1] // 3
    for i in range(box_x * 3, box_x + 3):
        for j in range(box_y * 3, box_y + 3):
            if (bo[i][j] == number and (i, j) != pos):
                return False

    return True
    


def solve(bo):
    find = check_position(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if (valid(bo, i, (row, col))):
            bo[row][col] = i

            if (solve(bo)):
                return True

            bo[row][col] = 0

    return False


def check_position(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if (bo[i][j] == 0):
                return (i, j)

    return None


def print_bo(bo):

    for i in range(len(bo[0])):
        if (i % 3 == 0 and i != 0):
            print("------------------------------------")
        for j in range(len(bo[1])):
            if (j % 3 == 0 and j != 0):
                print(" | ", end=" ")
            if (j == 8):
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ", end=' ')


print_bo(board)
solve(board)
print("- - - - - -- - - - - - - - - - -- - - - - - - - - --")
print_bo(board)
