user_input = list(' ' * 9)
x_and_o = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
num_str = ['one', 'two', 'tree', 'four']
num = [1, 2, 3]

"""
input_ = input("Enter cells: ")
user = list(input_)

for i in user:
    if i == '_':
        user_input.append(' ')
    else:
        user_input.append(i)
"""

import random

while True:
    print("-" * 9)
    print("| " + user_input[0], user_input[1], user_input[2] + " |")
    print("| " + user_input[3], user_input[4], user_input[5] + " |")
    print("| " + user_input[6], user_input[7], user_input[8] + " |")
    print("-" * 9)

    ##--------------------------------------##

    if x_and_o[-1] == 'X':
        coordinates = (input("Enter the coordinates: ")).split()
        # print(coordinates)
        if coordinates[0] in num_str or coordinates[1] in num_str:
            print("You should enter numbers!")
            continue
        elif int(coordinates[0]) not in num or int(coordinates[1]) not in num:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            # print(coordinates)
            
            if coordinates == [1, 1]:
                if user_input[6] == ' ':
                    user_input[6] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [1, 2]:
                if user_input[3] == ' ':
                    user_input[3] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [1, 3]:
                if user_input[0] == ' ':
                    user_input[0] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [2, 1]:
                if user_input[7] == ' ':
                    user_input[7] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [2, 2]:
                if user_input[4] == ' ':
                    user_input[4] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [2, 3]:
                if user_input[1] == ' ':
                    user_input[1] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [3, 1]:
                if user_input[8] == ' ':
                    user_input[8] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [3, 2]:
                if user_input[5] == ' ':
                    user_input[5] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
            elif coordinates == [3, 3]:
                if user_input[2] == ' ':
                    user_input[2] = x_and_o[-1]
                    x_and_o.pop()
                    continue
                else:
                    print("This cell is occupied! Choose another one!")
    elif x_and_o[-1] == 'O':
        print('Making move level "easy"')
        break
