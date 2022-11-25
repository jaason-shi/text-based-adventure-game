def make_board(rows, columns):
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = "Johnson"
            if column == 1:
                print("\n")
            print(board)


            # print(row, column)# ["Welcome to the pit of doom", None]
    return board

print(make_board(10,10))