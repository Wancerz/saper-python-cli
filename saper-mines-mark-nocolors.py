import random
import sys
from tkinter import E
import os

sys.setrecursionlimit(2000)
bombs_x = []
bombs_y = []
print(" * - hidden field \n 1-9 information about quantity of bombs around \n . - empty field(no bombs around)")
while 1:
    #menu start 
    while 1:
        try:
            print("Enter the size of the playing field (min 5, max 25):")
            size = int(input())
            if size not in range (5,26):
                print("Size value too low/high")
            else:
                print("Enter the number of mines, the maximum quantity:",size*size -1)
                mines_quantity = int(input())
                break
        except:
            print("The given value is not a number")
    
    if mines_quantity not in range (1,size*size):
        print("Bad quantity of mines")

    else:
        #mines generator
        bombs_y.append(random.randint(0, size - 1))
        bombs_x.append(random.randint(0, size - 1))

        while len(bombs_x) < mines_quantity :
            bomb_x_temp = random.randint(0, size - 1)
            bomb_y_temp = random.randint(0, size - 1)
            assignment = 0
            for x in range(1,len(bombs_x)):
                if bombs_x[x] == bomb_x_temp and  bombs_y[x] == bomb_y_temp:
                    assignment = 1
                    break
            if assignment == 0:
                bombs_x.append(bomb_x_temp)
                bombs_y.append(bomb_y_temp)
            assignment = 0     
        break

#visible area generator
visible_table = [["*" for x in range(size)] for y in range(size)]

#recursion function that counts bombs around a field
def show_block(x,y):
    count = 0
    for i,_ in enumerate(bombs_x):
        if bombs_x[i] == x and bombs_y[i] == y:
            return
    for i,_ in enumerate(bombs_x):
        if x > 0 and y > 0:
            if  x - 1 == bombs_x[i]  and   y - 1 == bombs_y[i]:
                count += 1
        if y > 0:
            if  x  == bombs_x[i]  and   y - 1 == bombs_y[i]:
                    count += 1
        if x < size -1 and y > 0:
            if  x + 1  == bombs_x[i]  and   y - 1 == bombs_y[i]:
                    count += 1
        if x > 0 and y < size -1:
            if  x -1  == bombs_x[i]  and   y + 1 == bombs_y[i]:
                    count += 1
        if y < size -1:
            if  x  == bombs_x[i]  and   y + 1 == bombs_y[i]:
                    count += 1
        if x < size -1 and y < size -1:
            if  x + 1 == bombs_x[i]  and   y + 1 == bombs_y[i]:
                    count += 1
        if x > 0:
            if  x -1  == bombs_x[i]  and   y  == bombs_y[i]:
                    count += 1
        if x < size -1:
            if  x + 1 == bombs_x[i]  and   y  == bombs_y[i]:
                    count += 1

        if count != 0:
            visible_table[y][x] = str(count)
        else:
            visible_table[y][x] = "."

    if count == 0:
        option(x,y)

#function that selects fields around a shoot 
def option(x,y):
    if x > 0 and y > 0 and visible_table[y-1][x-1] == "*" :
        show_block(x-1,y-1)
    if y > 0 and visible_table[y-1][x] == "*":
        show_block(x,y-1)
    if x < size -1 and y > 0 and visible_table[y-1][x+1] == "*":
        show_block(x+1,y-1)
    if x > 0 and y < size -1 and visible_table[y+1][x-1] == "*":
        show_block(x-1,y+1)
    if y < size -1 and visible_table[y+1][x] == "*":
        show_block(x,y+1)
    if x < size -1 and y < size -1 and visible_table[y+1][x+1] == "*":
        show_block(x+1,y+1)
    if x > 0 and visible_table[y][x-1] == "*":
        show_block(x-1,y)
    if x < size -1 and visible_table[y][x+1] == "*":
        show_block(x+1,y)
    
#main loop   
while 1:
    #drawing a board
    axis_x = "    "
    for x in range(0,size):
        if  x < 10:
            axis_x = axis_x + str(x) + "  " 
        else:
            axis_x = axis_x + str(x)+ " "
    axis_x = axis_x + " X"
    print(axis_x)
    axis_y = 0
    for x in range (len(visible_table)):
        if axis_y <10:
           print(axis_y," |", end= '')
        else:
            print(axis_y,"|", end= '')
        axis_y += 1

        for y in range (len(visible_table)):
            if visible_table[x][y] == "*":
                print("*  ", end='')
            else:
                print(visible_table[x][y]+"  ", end='')
        print('',end="\n")
    print("Y")

    while 1:
        #if statement for winning conditions
        if sum(x.count('*') for x in visible_table) + sum(x.count('B') for x in visible_table)  != mines_quantity:

            #pick menu
            while 1:
                try:   
                    print("Reveal field/Mark bomb(1/2)")
                    pick_mode = int(input())
                    if pick_mode in range(1,3): 
                        x_shot = int(input("Enter a coordinate of X: ")) 
                        y_shot = int(input("Enter a coordinate of Y: "))
                        break
                    else:
                        print("wrong choice")
                except:
                    print("The given value is not a number")


            if (x_shot and y_shot) in range(0,size):
                if  visible_table[y_shot][x_shot] == "*" or visible_table[y_shot][x_shot] == "B":
                    break
                else: 
                    print("The field is exposed, select the correct one")
            else:
                print("Coordinates outside the board")
        else:
            print("You won")
            os.system ('pause')
            sys.exit()
    
    #field changing 
    if pick_mode == 1:
        for i,_ in enumerate(bombs_x):
            
            if bombs_x[i] == x_shot and bombs_y[i] == y_shot:
                print("You lose")
                os.system('pause')
                sys.exit()
            else:
                show_block(x_shot,y_shot)
                option(x_shot,y_shot)
    else:
        if(visible_table[y_shot][x_shot] != "B"):
            visible_table[y_shot][x_shot] = "B"
        else:
            visible_table[y_shot][x_shot] = "*"