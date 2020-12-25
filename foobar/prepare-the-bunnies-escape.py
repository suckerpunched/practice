"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Test cases
==========
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11
"""

def shortest_path(sx, sy, map):
    h = len(map)
    w = len(map[0])
    b = [[None for i in range(w)] for i in range(h)]
    b[sx][sy] = 1

    a = [(sx, sy)]
    while a:
        x,y = a.pop(0)
        
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
            dx, dy = x+i[0], y+i[1]
            if 0 <= dx < h and 0 <= dy < w:
            
                if b[dx][dy] is None:
                    b[dx][dy] = b[x][y] + 1
                    if map[dx][dy] == 1: continue
                    a.append((dx, dy)) 
        
    return b

def solution(map):
    h = len(map)
    w = len(map[0])

    s = shortest_path(0, 0, map)
    f = shortest_path(h-1, w-1, map)
    board = []
    
    r = 2 ** 32-1
    for i in range(h):
        for j in range(w):
            if s[i][j] and f[i][j]: r = min(s[i][j]+f[i][j]-1, r)
    
    return r
