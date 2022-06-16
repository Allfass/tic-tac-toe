def check_player_choice(game_deck, sign):
    while True:
        user_row_input = int(input("Enter,row index: ")) - 1
        user_col_input = int(input("Enter,col index: ")) - 1
        if not (0 <= int(user_row_input) < 3 and 0 <= int(user_col_input) < 3):  # check out of bounds the matrix
            print("Uncorrected input")
            continue
        if not (game_deck[user_row_input][user_col_input] == ' '):
            print("This place has sign. Re-choice coordinate")
        else:
            break
    return user_row_input, user_col_input


def mark_play_deck(game_deck_status, user_input, player="X"):
    game_deck_status[user_input[0]][user_input[1]] = "X" if player == "X" else "O"
    #  print(game_deck_status)  # debug


def show_game_deck(game_deck_status):
    print("|    row    |")
    print("| 1 | 2 | 3 |")
    print(' --- --- --- ')
    for row in range(len(game_deck_status)):
        print('|', end=' ')
        for col in game_deck_status[row]:
            print(col, '| ', end='')
        if row < 2:
            print('\n|---|---|---|')
    print('\n')


def transposition(matrix):
    result = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            result[j][i] = matrix[i][j]
    return result


def is_win(game_deck_status, sign='X'):
    for i in range(3):  # check rows
        if game_deck_status[i] == [sign, sign, sign]:
            return True
    if all(i == sign for i in (game_deck_status[i][i] for i in range(3))):
        return True  # check main diagonal
    if all(i == sign for i in (game_deck_status[i][2 - i] for i in range(3))):
        return True  # check secondary diagonal
    transposition_matrix = transposition(game_deck_status)
    for i in range(3):  # check col
        if transposition_matrix[i] == [sign, sign, sign]:
            return True


def main():
    game_deck_status = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    endgame_counter = 0
    # print(is_win(game_deck_status))  # debug
    show_game_deck(game_deck_status)
    while True:
        endgame_counter = endgame_counter + 1  # check endgame move
        player_x_choice = check_player_choice(game_deck_status, "X")  # X - player move
        mark_play_deck(game_deck_status, player_x_choice, "X")
        show_game_deck(game_deck_status)
        if is_win(game_deck_status, 'X'):
            print("X win")
            break
        if endgame_counter == 5:  # every turn player do two move, odd move player X will be last
            print('draw')
            break
        player_y_choice = check_player_choice(game_deck_status, "O")  # O - player move
        mark_play_deck(game_deck_status, player_y_choice, "O")
        show_game_deck(game_deck_status)
        if is_win(game_deck_status, 'O'):
            print("O win")
            break


if __name__ == '__main__':
    main()
