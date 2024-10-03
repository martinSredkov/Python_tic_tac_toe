from colorama import Fore, Back, Style


# prints the field in the current state
def print_matrix(matrix):
    for line in matrix:
        line = [str(el) for el in line]
        print(f"|{'|'.join(line)}|")

# checks if user input is valid
def validate_user_input(user_input, min_value):
    return user_input.isdigit() and int(user_input) >= int(min_value)

# checks if move is valid - in range, not occupied
def is_move_in_range_and_free(user_row, user_col, current_state_field):
    size = len(current_state_field)
    if validate_user_input(user_row, 1) and validate_user_input(user_col, 1):
        user_row = int(user_row) - 1
        user_col = int(user_col) - 1
        if user_row <= size and user_col <= size:
            return current_state_field[user_row][user_col] == "-"

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

# checks if number of player is valid
def total_players_input(players_input):
    while not validate_user_input(players_input, MIN_PLAYERS):
        players_input = input(Fore.RED + "Enter valid number of players(at least 2):\n")
        print(Style.RESET_ALL)
    return players_input

# checks if field size is valid
def field_size_input(user_input):
    while not validate_user_input(user_input, total_players):
        user_input = input(Fore.RED + "Please enter valid field size(Bigger or equals to number of players):\n")
        print(Style.RESET_ALL)
    return int(user_input)


MIN_PLAYERS = 2
MIN_ROW_COL_VALUE = 1
# starts the game
if __name__ == "__main__":
    current_player = 0
    player_markers = []
    field = []
    # user input for number of players and validation of given input
    total_players = total_players_input(input("Please, enter number of players:\n"))
    # generating a list of markers for given number of players
    for n in range(int(total_players) + 1):
        player_markers.append(n + 1)
    # user input for field size and validation of given input
    field_size = field_size_input(input(f"Please enter field size(must be greater than or equals to {total_players}):\n"))
    # generating the play field
    for i in range(field_size):
        field.append([])
        [field[i].append("-") for _ in range(field_size)]
    # player move input, validating given input and updating the field
    while True:
        print_matrix(field)
        player_row = input(f"Player {current_player + 1}, please enter row for your move:\n")
        if not validate_user_input(player_row, MIN_ROW_COL_VALUE):
            print(Fore.RED + "Invalid input, please enter row in range of the field size: \n")
            print(Style.RESET_ALL)
            continue
        player_col = input(f"Player {current_player + 1}, please enter column for your move:\n")
        if not validate_user_input(player_col, MIN_ROW_COL_VALUE):
            print(Fore.RED + "Invalid input, please enter column in range of the field size: \n")
            print(Style.RESET_ALL)
            continue
        if is_move_in_range_and_free(player_row, player_col, field):
            player_row = int(player_row) - 1
            player_col = int(player_col) - 1
            field[player_row][player_col] = player_markers[current_player]
            # checking if current player is winner
            if is_player_winner(field):
                print(Back.GREEN + f"Player {current_player + 1} is winner")
                print_matrix(field)
                exit(0)
            # checking if result is draw - no empty spaces left and current player is not winner
            if is_field_full(field):
                print(Back.GREEN + "Result is draw")
                print_matrix(field)
                exit(0)
            # switching to next player if current is not winner and result isn't draw
            current_player += 1
            if current_player > int(total_players) - 1:
                current_player = 0
        else:
            print(Fore.RED + "Given coordinates are occupied or out of range.")
            print(Style.RESET_ALL)
            continue


