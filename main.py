from colorama import Fore, Back, Style


# prints the field in the current state
def print_matrix(matrix):
    for line in matrix:
        print(*line)

# checks if move is valid - in range, not occupied
def is_move_valid(move, size, current_state_field):
    try:
        input_row, input_col = move.split(" ")
        if input_row.isdigit() and input_col.isdigit():
            input_row = int(input_row) - 1
            input_col = int(input_col) - 1
            return 0 <= input_row <= size and 0 <= input_col <= size and current_state_field[input_row][input_col] == "-"
    except ValueError:
        return False

# checks if result is draw by searching for unoccupied spaces
def is_field_full(matrix):
    for line in matrix:
        for element in line:
            if element == "-":
                return False
    return True

# universal win condition check
def win_check(lst):
    if len(set(lst)) == 1 and "-" not in lst:
        return  True

# adds elements of rows, columns and diagonals to separate lists and passes them to win_check function
def is_player_winner(matrix):
    result = []
    matrix_size = len(matrix)

    # checks if winning conditions are met in rows
    for line in matrix:
        if win_check(line):
            return True
    # checks if winning conditions are met in columns
    for k in range(matrix_size):
        for j in range(matrix_size):
            result.append(matrix[j][k])
        if win_check(result):
            return True
        result = []

    if win_check(result):
        return True
    # checks if winning conditions are met in left to right diagonal
    for l in range(matrix_size):
        result.append(matrix[l][l])
    if win_check(result):
        return True
    result = []
    # checks if winning conditions are met in right to left diagonal
    for m in range(matrix_size, 0, - 1):
        result.append(matrix[matrix_size - m][m - 1])
    if win_check(result):
        return True
# starts the game
if __name__ == "__main__":
    current_player = 0
    player_markers = []
    field = []
    # User input for number of players and validation of given input
    total_players = input("Please, enter number of players:\n")
    while not total_players.isdigit():
        total_players = input(Fore.RED + "Enter valid number of players:\n")
        print(Style.RESET_ALL)
    while not 1 < int(total_players):
        total_players = input(Fore.RED + "At least two players are needed to play the game:\n")
        print(Style.RESET_ALL)
    # Generating a list of markers for given number of players
    for n in range(int(total_players) + 1):
        player_markers.append(n + 1)
    # User input for field size and validation of given input
    field_size = input(f"Please enter field size(must be greater than or equals to {total_players}):\n")
    while not field_size.isdigit():
        field_size = input(Fore.RED + "Please enter valid field size:\n")
        print(Style.RESET_ALL)
    while field_size < total_players:
        field_size = input(Fore.RED + f"Field size must be bigger or equals to {total_players}:\n")
        print(Style.RESET_ALL)
    field_size = int(field_size)
    while field_size <= 1:
        field_size = input(Fore.RED + "Please enter valid field size bigger than 1:\n")
        print(Style.RESET_ALL)
    # Generating the play field
    for i in range(field_size):
        field.append([])
        [field[i].append("-") for _ in range(field_size)]
    # Player move input, validating given input and updating the field
    while True:
        print_matrix(field)
        player_one_move = input(f"Player {current_player + 1}, please enter coordinates for your move:\n")
        if not is_move_valid(player_one_move, field_size, field):
            print(Fore.RED + "Invalid move, please enter unoccupied coordinates within the field: \n")
            print(Style.RESET_ALL)
            continue
        row, col = player_one_move.split(" ")
        row = int(row) - 1
        col = int(col) - 1
        field[row][col] = player_markers[current_player]
        # Checking if current player is winner
        if is_player_winner(field):
            print(Back.GREEN + f"Player {current_player + 1} is winner")
            print_matrix(field)
            exit(0)
        # Checking if result is draw - no empty spaces left and current player is not winner
        if is_field_full(field):
            print(Back.GREEN + "Result is draw")
            print_matrix(field)
            exit(0)
        # Switching to next player if current is not winner and result isn't draw
        current_player += 1
        if current_player > int(total_players) - 1:
            current_player = 0

