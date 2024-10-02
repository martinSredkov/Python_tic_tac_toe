def print_field(matrix):
    for line in matrix:
        print(line)

def is_move_valid(move, size):
    input_row, input_col = int(move.split(" ")[0]), int(move.split(" ")[1])
    if not 0 < input_row <= size or not 0 < input_col <= size:
        return False
    return True

def is_result_draw(matrix):
    for line in matrix:
        for element in line:
            if element == "*":
                return False
    return True

def is_player_winner(matrix):
    result = []
    matrix_size = len(matrix)
    def win_check(lst):
        if len(set(lst)) == 1 and "*" not in lst:
            return  True
    # horizontal check
    for line in matrix:
        if win_check(line):
            return True
    #vertical check
    for k in range(matrix_size):
        for j in range(matrix_size):
            result.append(matrix[j][k])
        if win_check(result):
            return True
        result = []

    if win_check(result):
        return True
    #diagonal check left to right
    for l in range(matrix_size):
        result.append(matrix[l][l])
    if win_check(result):
        return True
    result = []
    #diagonal check right to left
    for m in range(matrix_size, 0, - 1):
        result.append(matrix[matrix_size - m][m - 1])
    if win_check(result):
        return True

field = []
field_size = int(input("Please enter field size:\n"))
for i in range(field_size):
    field.append([])
    for _ in range(field_size):
        field[i].append("*")
while True:
    player_one_turn = True
    while player_one_turn:
        print_field(field)
        player_one_move = input("Player one, please enter coordinates for your move:\n")
        if not is_move_valid(player_one_move, field_size):
            print("Invalid move, please enter unoccupied coordinates within the field: \n")
            continue
        row, col = int(player_one_move.split(" ")[0]) - 1, int(player_one_move.split(" ")[1]) - 1
        field[row][col] = "X"
        player_one_turn = False

    if is_player_winner(field):
        exit("Player one is winner.")
    if is_result_draw(field):
        exit("Result is draw")

    while not player_one_turn:
        print_field(field)
        player_two_move = input("Player two, please enter coordinates for your move:\n")
        if not is_move_valid(player_two_move, field_size):
            print("Invalid move, please enter unoccupied coordinates within the field: \n")
            continue
        row, col = int(player_two_move.split(" ")[0]) - 1, int(player_two_move.split(" ")[1]) - 1
        field[row][col] = "O"
        player_one_turn = True

    if is_player_winner(field):
        exit("Player two is winner.")
    if is_result_draw(field):
        exit("Result is draw")
