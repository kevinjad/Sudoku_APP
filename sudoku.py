class sudoku:
    def __init__(self,board):
        self.board = board

    def print_board(self):
        for i in range(len(self.board)):
            
            for j in range(len(self.board[0])):
                if(j%3==0 and j!=0):
                    print('| ',end="")
                print(self.board[i][j],' ',end="")
            print("",end = '\n')
            if((i+1)%3==0 and i!=0):
                print('-----------------------------')

    def valid_fit(self,x,y,val):
        for i in range(len(self.board)):
            if ((self.board[x][i] == val)  and (i!=y)):
                return False
        for i in range(len(self.board)):
            if ((self.board[i][y] == val)  and (i!=x)):
                return False
        bx = (x//3) * 3
        by = (y//3) * 3

        for i in range(bx,bx+3):
            for j in range(by,by+3):
                if(self.board[i][j] == val and (i,j != x,y)):
                    return False
        return True

    def find_empty_box(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(self.board[i][j] == 0):
                    return (i,j)

    def solve(self):
        empty_box_pos = self.find_empty_box()
        if not empty_box_pos:
            return True
        x,y = empty_box_pos
        for i in range(1,10):
            if self.valid_fit(x,y,i):
                self.board[x][y] =i
                if self.solve():
                    return True
                self.board[x][y] = 0
        
        return False
