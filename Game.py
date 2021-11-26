from Terrain import *

class Game:
    def __init__(self, Army1, Army2):
        if Army1.points <= 500 and Army2.points <= 500:
            self.boardSize = (224,152)
        elif Army1.points <= 2000 and Army1.points <= 2000:
            self.boardSize = (224,305)
        else:
            self.boardSize = (224,457)
        self.board = [[0 for x in range(self.boardSize[0])]
                      for y in range(self.boardSize[1])]
        
        self.terrainList = []
    
    def displayBoard(self):
        with open('GameOutput.txt', 'a') as f:
            for y in range(self.boardSize[1]):
                f.write(str(self.board[y]))
                f.write("\n")
                
    def addTerrain(self, terrain):
        self.terrainList.append(terrain)
        if isinstance(terrain, Wall):
            drawWall(self.board, terrain.vertices)
        
        
def drawWall(board, vertices):
    for y in range(vertices[3][1], vertices[0][1] + 1):
        for x in range(vertices[0][0], vertices[1][0] + 1):
            board[y][x] = 1
    return