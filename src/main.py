import random as rndm

def main():
    size = 3
    bombs = 2
    game_table = Create_Matrix(size, bombs)
    
    game_reult = 0
    game_in_course = 1
    while(game_in_course==1):
        show_matrix(game_table)
        coords = readKB()
        posX, posY = coords[1],coords[2]
        result = check_Matrix(game_table, posX, posY)
        rest_moves = check_rest(game_table)
        
        if result == 1:
            game_reult = 1
        if rest_moves == bombs:
            game_reult = 1
    
    print("You win the game ") if game_reult == 2 else print("You touch a mine, you lose")

def check_Matrix(game_table, posX, posY):
    if(game_table[posX][posY] == "M" ):
        bomb_Found = 1
    else:
        bomb_Found = 0
    edit_Matrix(game_table, posX, posY)
        
    return bomb_Found  

def edit_Matrix(game_table, posX, posY):
    if game_table[posX][posY] == "9":
        game_table[posX][posY] = "B"
    elif game_table[posX][posY] == "0":
       game_table[posX][posY] = "1"


        
def Create_Matrix(size, num_Bombs):
    game_Tableboard = []

    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(" ")
        game_Tableboard.append(row)

    Bombing(game_Tableboard,num_Bombs, size)
    return game_Tableboard

def Bombing(game_Tableboard, num_Bombs, size):
    for _ in range(num_Bombs):
        bomb_setted = False
        while not bomb_setted:
            bombX = rndm.randint(0, size - 1)
            bombY = rndm.randint(0, size - 1)

            if game_Tableboard[bombX][bombY] == " ":
                game_Tableboard[bombX][bombY] = "M"
                bomb_setted = True

    return game_Tableboard

def  show_matrix(game_table):
    print("Current tableboard: \n ")
    for row in game_table:
       for col in row:
          elem = game_table[row][col]
          if(elem == "0"):
              print(" ? ")
          elif(elem == "1"):
              print(" O ")
          else:
              print(" X ")
    print("----------------------------------\n")

def check_rest(game_table):
    moves = 0
    for row in game_table:
        for col in row:
            moves += 1 if game_table[row][col] == 0 else None
    
    return moves

def readKB():
    coords = input("Enter positition to check (Format: X,Y)") 
    coords = coords.replace(",", "").split()   
    return coords[1], coords[2]


if __name__ == "__main__":
    main()