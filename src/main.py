import random as rndm
from Tile import Tile

def main():
    size = 3
    mine_number = 2
    game_table = Create_Matrix(size, mine_number)
    
    game_reult = 0
    game_in_course = True
    while(game_in_course==True and game_reult == 0):
        show_matrix(game_table)
        posX, posY = readKB()
        bomb_found = check_Matrix(game_table, posX, posY)
        rest_moves = check_rest(game_table)
        
        if bomb_found:
            game_in_course = False
            show_all(game_table, posX, posX)
        if rest_moves == mine_number:
            game_reult = "win"
    
    print("You win the game. All mine_number located") if game_reult == "win" else print("You touch a mine, you lose")

def check_Matrix(game_table, posX, posY):
    if(game_table[posX][posY].get_value() == 9 ):
        game_table[posX][posY].Visited()
        bomb_Found = True
    else:
        bomb_Found = False
    #tiles_Visited(game_table, posX, posY)
    reveal_Neighbours(game_table, posX, posY)
    return bomb_Found  

#def tiles_Visited(game_table, posX, posY):
    if game_table[posX][posY].get_value() == 9:
        None
    else:
       game_table[posX][posY].Visited()

def reveal_Neighbours(game_table, posX, posY):
    if posX < 0 or posX >= len(game_table) or posY < 0 or posY >= len(game_table[0]):
        return

    tile = game_table[posX][posY]
    if tile.is_visited():
        return

    tile.Visited()

    if tile.get_value() != 0:
        return

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue

            nx = posX + dx
            ny = posY + dy

            if 0 <= nx < len(game_table) and 0 <= ny < len(game_table[0]):
                neighbor = game_table[nx][ny]
                if not neighbor.is_visited() and neighbor.get_value() != 9:
                    reveal_Neighbours(game_table, nx, ny)

    return None
        
def Create_Matrix(size, num_Bombs):
    game_Tableboard = []

    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(Tile(0))
        game_Tableboard.append(row)

    Bombing(game_Tableboard,num_Bombs, size)
    Proximity(game_Tableboard)
    return game_Tableboard

def Bombing(game_Tableboard, num_Bombs, size):
    for _ in range(num_Bombs):
        bomb_setted = False
        while not bomb_setted:
            bombX = rndm.randint(0, size - 1)
            bombY = rndm.randint(0, size - 1)

            if game_Tableboard[bombX][bombY].get_value() == 0:
                game_Tableboard[bombX][bombY].set_value(9)
                bomb_setted = True

    return game_Tableboard

def Proximity(game_Tableboard):
    rows = len(game_Tableboard)
    cols = len(game_Tableboard[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            current = game_Tableboard[row][col]

            if current.get_value() == 9:
                continue

            bombs_around = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue

                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if game_Tableboard[nr][nc].get_value() == 9:
                             bombs_around += 1
                        

            current.set_value(bombs_around)

    return game_Tableboard

def show_matrix(game_table):
    print("Current tableboard: \n ")
    for row in range(len(game_table)):
        for col in range(len(game_table)):
            elem = game_table[row][col]
            if( not elem.is_visited()):
                print(" ? ")
            else:
                print(F%" {elem.get_value()} ")
                
    print("----------------------------------\n")

def show_all(game_table,posX,posY):
    for row in range(len(game_table)):
        for col in range(len(game_table)):
            elem = game_table[row][col]
            print("X") if ( row == posX and col == posY ) else print(elem.get_value())
                
def check_rest(game_table):
    moves = 0
    for row in game_table:
        for col in row:
            if game_table[row][col].is_visited():
                moves += 1
    
    return len(game_table)**2 - moves

def readKB():
    coords = input("Enter positition to check (Format: X,Y)") 
    row, col = map(int, coords.split(","))
    return row, col


if __name__ == "__main__":
    main()