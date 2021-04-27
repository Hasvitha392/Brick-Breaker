from headers import *
from brick import * 

class Power1(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self):
        self.green_brick(15,40)
        self.green_brick(14,45)
        self.green_brick(14,35)
        self.green_brick(13,50)
        self.green_brick(13,30)
        self.green_brick(12,55)
        self.green_brick(12,25)
        self.green_brick(11,60)
        self.green_brick(11,20)

        self.green_brick(10,40)
        self.green_brick(9,45)
        self.green_brick(9,35)
        self.green_brick(8,50)
        self.green_brick(8,30)
        self.green_brick(7,55)
        self.green_brick(7,25)
        self.green_brick(6,60)
        self.green_brick(6,20)
        
       
class Power2(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self):
        self.cyan_brick(14,40)
        self.cyan_brick(13,45)
        self.cyan_brick(13,35)
        self.cyan_brick(12,50)
        self.cyan_brick(12,30)
        self.cyan_brick(11,55)
        self.cyan_brick(11,25)
        self.cyan_brick(10,60)
        self.cyan_brick(10,20)

        self.cyan_brick(12,40)
        self.cyan_brick(11,45)
        self.cyan_brick(11,35)
        self.cyan_brick(10,50)
        self.cyan_brick(10,30)
        self.cyan_brick(9,55)
        self.cyan_brick(9,25)
        self.cyan_brick(8,60)
        self.cyan_brick(8,20)

        

            
class Power3(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self): 
        self.red_brick(12,45)
        self.red_brick(12,35)
        self.red_brick(11,50)
        self.red_brick(11,30)
        self.red_brick(10,55)
        self.red_brick(10,25)
        self.red_brick(9,60)
        self.red_brick(9,20)

        self.red_brick(11,40)
        self.red_brick(10,45)
        self.red_brick(10,35)
        self.red_brick(9,50)
        self.red_brick(9,30)
        self.red_brick(8,55)
        self.red_brick(8,25)
        self.red_brick(7,60)
        self.red_brick(7,20)

        self.red_brick(17,40)
        self.red_brick(16,45)
        self.red_brick(16,35)
        self.red_brick(15,50)
        self.red_brick(15,30)
        self.red_brick(14,55)
        self.red_brick(14,25)
        self.red_brick(13,60)
        self.red_brick(13,20)
        

class Powerinf(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self):    
        self.black_brick(13,40)
        

class Exploadbrick(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self):      
        self.yellow_brick(16,40)
        self.yellow_brick(15,45)
        self.yellow_brick(15,35)
        self.yellow_brick(14,50)
        self.yellow_brick(14,30)
        self.yellow_brick(13,55)
        self.yellow_brick(13,25)
        self.yellow_brick(12,60)
        self.yellow_brick(12,20)


class level2_Power1(Brick):
    def __init__(self):
        Brick.__init__(self)

    def clearbricks(self):
        for i in range(15,61):
            for j in range(6,18):
                getboard.board[j][i] = " "
    
    def assign_color(self):
        
        self.green_brick(17,45)
        self.green_brick(17,35)
        self.green_brick(17,50)
        self.green_brick(17,30)
        self.green_brick(17,55)
        self.green_brick(17,25)
        self.green_brick(17,60)
        self.green_brick(17,20)
        self.green_brick(17,65)
        self.green_brick(17,15)

        self.green_brick(19,40)
        self.green_brick(19,45)
        self.green_brick(19,35)

        self.green_brick(20,40)
        self.green_brick(20,45)
        self.green_brick(20,35)

        self.green_brick(12,40)
        self.green_brick(12,45)
        self.green_brick(12,35)

        self.green_brick(13,40)
        self.green_brick(13,45)
        self.green_brick(13,35)

        
        
       
class level2_Power2(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self):
        self.cyan_brick(16,40)
        self.cyan_brick(16,45)
        self.cyan_brick(16,35)
        self.cyan_brick(16,50)
        self.cyan_brick(16,30)
        self.cyan_brick(16,55)
        self.cyan_brick(16,25)
        self.cyan_brick(16,20)
        self.cyan_brick(16,60)
        self.cyan_brick(16,15)
        self.cyan_brick(16,65)

        self.cyan_brick(21,40)
        self.cyan_brick(21,45)
        self.cyan_brick(21,35)

        self.cyan_brick(22,40)
        self.cyan_brick(22,45)
        self.cyan_brick(22,35)

        
        

            
class level2_Power3(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self): 
        self.red_brick(18,40)
        self.red_brick(18,45)
        self.red_brick(18,35)
        self.red_brick(18,50)
        self.red_brick(18,30)
        self.red_brick(18,55)
        self.red_brick(18,25)
        self.red_brick(18,60)
        self.red_brick(18,20)
        self.red_brick(18,65)
        self.red_brick(18,15)

        self.red_brick(14,40)
        self.red_brick(14,45)
        self.red_brick(14,35)

        self.red_brick(15,40)
        self.red_brick(15,45)
        self.red_brick(15,35)
        
        

class level2_Powerinf(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self):    
        self.black_brick(17,40)
        
'''
class level2_Exploadbrick(Brick):
    def __init__(self):
        Brick.__init__(self)
    
    def assign_color(self):      
        self.yellow_brick(16,40)
        self.yellow_brick(15,45)
        self.yellow_brick(15,35)
        self.yellow_brick(14,50)
        self.yellow_brick(14,30)
        self.yellow_brick(13,55)
        self.yellow_brick(13,25)
        self.yellow_brick(12,60)
        self.yellow_brick(12,20)
'''
