row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
row4 = ["⬜️", "⬜️", "⬜️"]
row5 = ["⬜️", "⬜️", "⬜️"]
row6 = ["⬜️", "⬜️", "⬜️"]
row7 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3, row4 , row5, row6, row7]
print(f"{row1}\n{row2}\n{row3}{row4}\n{row5}\n{row6}\n{row7}\n")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = "X"

print(f"{row1}\n{row2}\n{row3}{row4}\n{row5}\n{row6}\n{row7}\n")
