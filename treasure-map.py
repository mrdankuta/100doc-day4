row1 = ["___","___","___"]
row2 = ["___","___","___"]
row3 = ["___","___","___"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? Enter a row number, a comma, and a column number \n").split(", ")

pos1 = int(position[0])
pos2 = int(position[1])

map[pos1 - 1][pos2 - 1] = "_x_"

print(f"{map[0]}\n{map[1]}\n{map[2]}")


# More Elegant Solution

# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"
