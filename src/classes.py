class Square:
    def __init__(self):
        self.bomb = False
        self.number = 0


class Grid:
    def __init__(self, width, height, bombs):
        self.width = width
        self.height = height
        self.bombs = bombs
        self.squares = list()

        # create a list of list of Squares
        for i in range(height):
            tmp = list()
            for j in range(width):
                sq = Square()
                tmp.append(sq)
            self.squares.append(tmp)

    def __str__(self):
        for i in range(height):
            for j in range(width):
                if self.squares[i][j].bomb:
                    print("X")
                else
                    print(self.squares[i][j].number)
            print("\n")



        
