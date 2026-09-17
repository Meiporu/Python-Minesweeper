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
        posX, posY = readKB(size)
        bomb_found = check_Matrix(game_table, posX, posY)
        safe_remain = check_rest(game_table)
        
        if bomb_found:
            game_in_course = False
            show_all(game_table, posX, posY)
        if safe_remain == 0:
            game_reult = "win"
    
    print("You win the game. All mine_number located") if game_reult == "win" else print("You touch a mine, you lose")

def check_Matrix(game_table, posX, posY):
    tile = game_table[posX][posY]

    if tile.get_value() == 9:
        tile.Visited()
        return True

    reveal_Neighbours(game_table, posX, posY)
    return False


def reveal_Neighbours(game_table, posX, posY):
    if posX < 0 or posX >= len(game_table) or posY < 0 or posY >= len(game_table[0]):
        return

    tile = game_table[posX][posY]
    if tile.is_visited() or tile.get_value() == 9:
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
        line = []
        for col in range(len(game_table[row])):
            elem = game_table[row][col]
            if not elem.is_visited():
                line.append("?")
            else:
                line.append(str(elem.get_value()))
        print(" ".join(line))

    print("----------------------------------\n")


# Debug method
def show_all(game_table, posX, posY):
    for row in range(len(game_table)):
        values = []
        for col in range(len(game_table[row])):
            if row == posX and col == posY:
                values.append("X")
            else:
                values.append(str(game_table[row][col].get_value()))
        print(" ".join(values))

                   
def check_rest(game_table):
    safe_remain = 0
    for row in game_table:
        for tile in row:
            if not tile.is_visited() and tile.get_value() != 9:
                safe_remain += 1
    
    return safe_remain

def readKB(size):
    correct_input = False
    while not correct_input:
        coords = input("Enter position to check (Format: X,Y): ").strip()
        try:
            row_str, col_str = coords.split(",")
            row = int(row_str)
            col = int(col_str)
        except (ValueError, TypeError):
            print("Invalid input. Use X,Y")
            continue
        
        if 0 <= row < size and 0 <= col < size:
            return row, col
        
        print(f"Coordinates out of range. Use values between 0 and {size - 1}.")
        
        
if __name__ == "__main__":
    main()