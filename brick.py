from headers import *
from board import getboard
from alarmexception import AlarmException
from getch import _getChUnix as getChar

class Brick:

    def __init__(self):
        

        self.rows, self.cols = (45, 80) 
        self.power = [[0]*self.cols]*self.rows 

        self.power[15][50 - 10] = 1
        self.power[15-1][50 - 10-5] = 1
        self.power[15-1][50 - 10+5] = 1
        self.power[15-2][50 - 10-10] = 1
        self.power[15-2][50 - 10+10] = 1
        self.power[15-3][50 - 10-15] = 1
        self.power[15-3][50 - 10+15] = 1
        self.power[15-4][50 - 10-20] = 1
        self.power[15-4][50 - 10+20] = 1
        self.power[15-5][50 - 10] = 1
        self.power[15-5-1][50 - 10-5] = 1
        self.power[15-5-1][50 - 10+5] = 1
        self.power[15-5-2][50 - 10-10] = 1
        self.power[15-5-2][50 - 10+10] = 1
        self.power[15-5-3][50 - 10-15] = 1
        self.power[15-5-3][50 - 10+15] = 1
        self.power[15-5-4][50 - 10-20] = 1
        self.power[15-5-4][50 - 10+20] = 1


        self.power[15+2][50 - 10] = 2
        self.power[15-1+2][50 - 10-5] = 2
        self.power[15-1+2][50 - 10+5] = 2
        self.power[15-2+2][50 - 10-10] = 2
        self.power[15-2+2][50 - 10+10] = 2
        self.power[15-3+2][50 - 10-15] = 2
        self.power[15-3+2][50 - 10+15] = 2
        self.power[15-4+2][50 - 10-20] = 2
        self.power[15-4+2][50 - 10+20] = 2
        self.power[15-1][50 - 10] = 2
        self.power[15-1-1][50 - 10-5] = 2
        self.power[15-1-1][50 - 10+5] = 2
        self.power[15-2-1][50 - 10-10] = 2
        self.power[15-2-1][50 - 10+10] = 2
        self.power[15-3-1][50 - 10-15] = 2
        self.power[15-3-1][50 - 10+15] = 2
        self.power[15-4-1][50 - 10-20] = 2
        self.power[15-4-1][50 - 10+20] = 2
        self.power[15-3][50 - 10] = 2
        self.power[15-3-1][50 - 10-5] = 2
        self.power[15-3-1][50 - 10+5] = 2
        self.power[15-3-2][50 - 10-10] = 2
        self.power[15-3-2][50 - 10+10] = 2
        self.power[15-3-3][50 - 10-15] = 2
        self.power[15-3-3][50 - 10+15] = 2
        self.power[15-3-4][50 - 10-20] = 2
        self.power[15-3-4][50 - 10+20] = 2

        self.power[15-1-1][50 - 10] = float("inf")
        self.power[15-1-1-1][50 - 10-5] = 3
        self.power[15-1-1-1][50 - 10+5] = 3
        self.power[15-2-1-1][50 - 10-10] = 3
        self.power[15-2-1-1][50 - 10+10] = 3
        self.power[15-3-1-1][50 - 10-15] = 3
        self.power[15-3-1-1][50 - 10+15] = 3
        self.power[15-4-1-1][50 - 10-20] = 3
        self.power[15-4-1-1][50 - 10+20] = 3
        self.power[15-3-1][50 - 10] = 3
        self.power[15-3-1-1][50 - 10-5] = 3
        self.power[15-3-1-1][50 - 10+5] = 3
        self.power[15-3-2-1][50 - 10-10] = 3
        self.power[15-3-2-1][50 - 10+10] = 3
        self.power[15-3-3-1][50 - 10-15] = 3
        self.power[15-3-3-1][50 - 10+15] = 3
        self.power[15-3-4-1][50 - 10-20] = 3
        self.power[15-3-4-1][50 - 10+20] = 3
        
    def assign_color(self):
        pass
        
    def green_brick(self,y,x):
        getboard.board[y][x]=Back.LIGHTGREEN_EX+")"+Back.RESET
        getboard.board[y][x-4]=Back.LIGHTGREEN_EX+"("+Back.RESET
        for i in range(1,4):
            getboard.board[y][x-i]=Back.LIGHTGREEN_EX+"$"+Back.RESET    
    
    def cyan_brick(self,y,x):
        getboard.board[y][x]=Back.LIGHTCYAN_EX+")"+Back.RESET
        getboard.board[y][x-4]=Back.LIGHTCYAN_EX+"("+Back.RESET
        for i in range(1,4):
            getboard.board[y][x-i]=Back.LIGHTCYAN_EX+"$"+Back.RESET    

    def red_brick(self,y,x):
            getboard.board[y][x]=Back.RED+")"+Back.RESET
            getboard.board[y][x-4]=Back.RED+"("+Back.RESET
            for i in range(1,4):
                getboard.board[y][x-i]=Back.RED+"$"+Back.RESET    
    
    def black_brick(self,y,x):
        getboard.board[y][x]=Back.BLACK+")"+Back.RESET
        getboard.board[y][x-4]=Back.BLACK+"("+Back.RESET
        for i in range(1,4):
            getboard.board[y][x-i]=Back.BLACK+"$"+Back.RESET    
    
    def yellow_brick(self,y,x):
        getboard.board[y][x]=Back.YELLOW+")"+Back.RESET
        getboard.board[y][x-4]=Back.YELLOW+"("+Back.RESET
        for i in range(1,4):
            getboard.board[y][x-i]=Back.YELLOW+"$"+Back.RESET    


class level2(Brick):
     def __init__(self):
        def clearbricks(self):
            for i in range(15,61):
                for j in range(6,18):
                    self.power[j][i] = 0
        self.rows, self.cols = (45, 80) 
        self.power = [[0]*self.cols]*self.rows 

        self.power[17][40] = float("inf")


        self.power[17][40 - 5] = 1
        self.power[17][40 + 5] = 1
        self.power[17][40 - 10] = 1
        self.power[17][40 + 10] = 1
        self.power[17][40 - 15] = 1
        self.power[17][40 + 15] = 1
        self.power[17][40 - 20] = 1
        self.power[17][40 + 20] = 1
        self.power[17][40 - 25] = 1
        self.power[17][40 + 25] = 1

        self.power[19][40] = 1
        self.power[19][40 - 5] = 1
        self.power[19][40 + 5] = 1

        self.power[20][40] = 1
        self.power[20][40 - 5] = 1
        self.power[20][40 + 5] = 1

        self.power[12][40] = 1
        self.power[12][40 - 5] = 1
        self.power[12][40 + 5] = 1

        self.power[13][40] = 1
        self.power[13][40 - 5] = 1
        self.power[13][40 + 5] = 1
        

        self.power[16][40] = 2
        self.power[16][40 - 5] = 2
        self.power[16][40 + 5] = 2
        self.power[16][40 - 10] = 2
        self.power[16][40 + 10] = 2
        self.power[16][40 - 15] = 2
        self.power[16][40 + 15] = 2
        self.power[16][40 - 20] = 2
        self.power[16][40 + 20] = 2
        self.power[16][40 - 25] = 2
        self.power[16][40 + 25] = 2

        self.power[21][40] = 2
        self.power[21][40 - 5] = 2
        self.power[21][40 + 5] = 2

        self.power[22][40] = 2
        self.power[22][40 - 5] = 2
        self.power[22][40 + 5] = 2


        self.power[18][40] = 3
        self.power[18][40 - 5] = 3
        self.power[18][40 + 5] = 3
        self.power[18][40 - 10] = 3
        self.power[18][40 + 10] = 3
        self.power[18][40 - 15] = 3
        self.power[18][40 + 15] = 3
        self.power[18][40 - 20] = 3
        self.power[18][40 + 20] = 3
        self.power[18][40 - 25] = 3
        self.power[18][40 + 25] = 3

        self.power[14][40] = 3
        self.power[14][40 - 5] = 3
        self.power[14][40 + 5] = 3

        self.power[15][40] = 3
        self.power[15][40 - 5] = 3
        self.power[15][40 + 5] = 3



        
         

    
getbrick = Brick()