print("This is a Tic Tac Toe game!!")
def print_board():
    print("  1 2 3")
    for i in range(1, 4):
        print(i, end=" ")
        for j in range(1, 4):
            if [i, j] in x_pos:
                print("x", end=" ")
            elif [i, j] in o_pos:
                print("o", end=" ")
            else:
                print(" ", end=" ")
        print()

def check_win(player_pos):
    # Winning combinations
    win_combinations = [
        [[1, 1], [1, 2], [1, 3]],  # First row
        [[2, 1], [2, 2], [2, 3]],  # Second row
        [[3, 1], [3, 2], [3, 3]],  # Third row
        [[1, 1], [2, 1], [3, 1]],  # First column
        [[1, 2], [2, 2], [3, 2]],  # Second column
        [[1, 3], [2, 3], [3, 3]],  # Third column
        [[1, 1], [2, 2], [3, 3]],  # Diagonal from top-left to bottom-right
        [[1, 3], [2, 2], [3, 1]]   # Diagonal from top-right to bottom-left
    ]
    
    for combination in win_combinations:
        if all(pos in player_pos for pos in combination):
            return True
    return False

def check_draw():
    return len(x_pos) + len(o_pos) == 9  # If all cells are filled and no winner

x_pos = []
o_pos = []
current_player = "x"

while True:
    print_board()
    row = int(input(f"Enter row for {current_player} (1-3): "))
    col = int(input(f"Enter col for {current_player} (1-3): "))
    
    if [row, col] in x_pos or [row, col] in o_pos:
        print("Position already taken! Choose another.")
        continue
    
    if current_player == "x":
        x_pos.append([row, col])
        if check_win(x_pos):
            print_board()
            print("Player 'x' wins!")
            break
        current_player = "o"
    else:
        o_pos.append([row, col])
        if check_win(o_pos):
            print_board()
            print("Player 'o' wins!")
            break
        current_player = "x"
    
    if check_draw():
        print_board()
        print("It's a draw!")
        break
