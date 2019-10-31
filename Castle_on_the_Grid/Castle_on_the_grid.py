
import math
import os
import random
import re
import sys

def minimumMoves(grid, queue, goal, move, path):
    
    #print(grid, queue, goal, move, path)
    if len(queue) == 0:
        print("SAIU")
        return False
    #print("GOAL: ", goal)
    print("queue:", queue)
    current_move = move[0]
    position = queue[0]
    del move[0]
    del queue[0]

    positionX = position[0]
    positionY = position[1]
    print("\npositions from iteration (%i, %i)" % (positionX, positionY))
    
    row = grid[positionX]
    
    
    column = []
    for x in grid:
        column.append(x[positionY])
        
    print("\ncolumn:", column)
    column_limit = search_limit(column, positionX)
    print("column_limit:", column_limit)
    
    print("row:", row)
    row_limit = search_limit(row, positionY)
    print("row_limit:", row_limit)

    # Check if are new_moves and add in queue
    for horizontal_move in range (positionY-row_limit['up_limit'], positionY+row_limit['down_limit']+1):
        #new_move = x, positionY
        #pra analisar linha, não precisa deixar linha fixa e variar a coluna
        new_move = positionX, horizontal_move
        print(new_move)
        if new_move not in path:
            if new_move == goal:
                return current_move + 1

            move.append(current_move + 1)
            queue.append(new_move)
            path.add(new_move)
            
    #print("column_limit:", column_limit)
    for vertical_move in range (positionX-column_limit['up_limit'], positionX+column_limit['down_limit']+1):
        new_move = vertical_move, positionY
        print(new_move)
        if new_move not in path:
            if new_move == goal:
                return current_move + 1

            move.append(current_move + 1)
            queue.append(new_move)
            path.add(new_move)

    return minimumMoves(grid, queue, goal, move, path)

def search_limit(line, point):
    # Return the limit of the move in that line starting in point

    line_up = line[0:point]
    #print("line_up:", line_up)
    line_down = line[point+1:]
    #print("\nline_down:", line_down)
    
    #print("\npoint:", point)
    if 'x' in line_down:
        down_limit = line_down.index('x')
        
    else:
        #down_limit = 0
        #pq limite 0?
        down_limit = len(line_down)
    #print("down_limit:", down_limit)

    if 'x' in line_up:
        reverse_line_up = line_up[::-1]
        #print("index x: ", reverse_line_up.index('x'))
        #down_limit = len(line_down) - reverse_line_down.index('x')
        #pq colocar len(line_down, qnd o index ja te da o valor que pode correr até chegar em x?
        up_limit = reverse_line_up.index('x')

    else:
        up_limit = len(line_up)
    #print("up_limit:", up_limit)
    
    #print("\n----------------------------------\n")
    return({'down_limit':down_limit, 'up_limit':up_limit})

def main():
    # Main Code
    #n = int(input())

    grid = []
    grid = ['.X.',
            '.x.',
            '...'
            ]
    for i in range(len(grid)):
        grid[i] = grid[i].lower()
    print(grid)
#    for _ in range(n):
#        grid_item = input()
#        grid.append(grid_item)

#    startXStartY = input().split()

#    startX = int(startXStartY[0])
    startX = 0
    
#    startY = int(startXStartY[1])
    startY = 0

    start = [(startX, startY)]

#    goalX = int(startXStartY[2])
    goalX = 0
#    goalY = int(startXStartY[3])
    goalY = 2

    goal = (goalX, goalY)
    move = [0]
    path = set(start)

    result = minimumMoves(grid, start, goal, move, path)
    print(result)

if __name__ == '__main__':
    main()