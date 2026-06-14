import random

print("Alphabet 2048")
print("Rules: Combine same letters to get the next letter. Don't fill the entire board.")
print("Controls: Move up (W), left (A), down (S), right (D). Exit game (X).")
grid = [".", ".", ".", ".",
        ".", ".", ".", ".",
        ".", ".", ".", ".",
        ".", ".", ".", "."]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
turns = 0

while alphabet[len(alphabet)-1] not in grid:
    # Add A randomly on the grid if space available, else display game over
    empty_positions = []
    for i in range(len(grid)):
        if grid[i] == ".":
            empty_positions.append(i)

    if len(empty_positions) != 0:
        grid[empty_positions[random.randint(0, len(empty_positions)-1)]] = alphabet[random.randint(0,1)] if turns > 1 else alphabet[0]
    else:
        break
    
    # Display grid for next move
    score = 0
    for i in range(len(grid)):
        if grid[i] in alphabet:
            score += 2 ** (alphabet.index(grid[i]) + 1)

    print(f"\nTurns: {turns}, Score: {score}")

    for row in range(4):
        for column in range(4):
            print(grid[4 * row + column], end=" ")
        print()

    # Ask player for move
    move = input("Move: ").upper()
    while move not in ["W", "A", "S", "D", "X"]:
        move = input("\nInvalid move. Please use W, A, S, D, X only.\nMove: ").upper()

    # W (move up)
    if move == "W":
        for i in range(len(grid)-4):
            if grid[(len(grid)-1)-i] == ".":
                continue
            elif grid[(len(grid)-1)-i-4] == ".":
                grid[(len(grid)-1)-i-4] = grid[(len(grid)-1)-i]
                grid[(len(grid)-1)-i] = "."
            elif grid[(len(grid)-1)-i-4] == grid[(len(grid)-1)-i]:
                grid[(len(grid)-1)-i-4] = alphabet[alphabet.index(grid[(len(grid)-1)-i])+1]
                grid[(len(grid)-1)-i] = "."
            elif grid[(len(grid)-1)-i-4] != grid[(len(grid)-1)-i]:
                continue

    # A (move left)
    elif move == "A":
        for row in range(4):
            for column in [3, 2, 1]:
                if grid[4 * row + column] == ".":
                    continue
                elif grid[4 * row + column - 1] == ".":
                    grid[4 * row + column - 1] = grid[4 * row + column]
                    grid[4 * row + column] = "."
                elif grid[4 * row + column - 1] == grid[4 * row + column]:
                    grid[4 * row + column - 1] = alphabet[alphabet.index(grid[4 * row + column])+1]
                    grid[4 * row + column] = "."
                elif grid[4 * row + column - 1] != grid[4 * row + column]:
                    continue

    # S (move down)
    elif move == "S":
        for i in range(len(grid)-4):
            if grid[i] == ".":
                continue
            elif grid[i+4] == ".":
                grid[i+4] = grid[i]
                grid[i] = "."
            elif grid[i+4] == grid[i]:
                grid[i+4] = alphabet[alphabet.index(grid[i])+1]
                grid[i] = "."
            elif grid[i+4] != grid[i]:
                continue
    
    # D (move right)
    elif move == "D":
        for row in range(4):
            for column in range(3):
                if grid[4 * row + column] == ".":
                    continue
                elif grid[4 * row + column + 1] == ".":
                    grid[4 * row + column + 1] = grid[4 * row + column]
                    grid[4 * row + column] = "."
                elif grid[4 * row + column + 1] == grid[4 * row + column]:
                    grid[4 * row + column + 1] = alphabet[alphabet.index(grid[4 * row + column])+1]
                    grid[4 * row + column] = "."
                elif grid[4 * row + column + 1] != grid[4 * row + column]:
                    continue
                
    # X (end game)
    elif move == "X":
        break

    turns += 1

print("\nGame over!")
print(f"Final score: {score}")
