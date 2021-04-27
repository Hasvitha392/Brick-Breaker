from headers import *
from board import getboard
from paddle import Paddle
from brick import Brick
from brick import getbrick
from ball import *
from powerup import *
from ballcollision import *
from colors import *
from config import flag
from takeinput import input_to,Get
os.system('clear')
PADDLE = Paddle(30,38,0,34,37)
PADDLE.createpaddle()
BALL = Ball(34,37,1,-1,5,0)
BALL.createball()
BRICK = Brick()
POWER1 = Power1()
POWER1.assign_color()
POWER2 = Power2()
POWER2.assign_color()
POWER3 = Power3()
POWER3.assign_color()
POWERINF = Powerinf()
POWERINF.assign_color()
EXPLOADBRICK = Exploadbrick()
EXPLOADBRICK.assign_color()
BALLCOLLISION = getballcollision
BOARD = getboard
BOARD.printboard()


start_time = time.time()
screen_time=time.time()
x=time.time()
flag = 0
rainbow = 0
while True:
   os.system("tput reset")
  

   #print board
   BOARD.printboard()
   newtime =(round(time.time()) - round(start_time))
   print(  Fore.GREEN+"time:"+Back.RESET , newtime,  Fore.CYAN+"   lives remaining :"+Back.RESET, BALLCOLLISION.lives,  Fore.RED+"   score :"+Back.RESET, BALLCOLLISION.score)
   #print (newtime) 

   
   get = Get()
   inp = input_to(get.__call__)
   
   if inp == 'k' and flag == 0:
      flag = 1
      LEVEL2 = level2()
      LEVEL2_POWER1 = level2_Power1()

      LEVEL2_POWER1.assign_color()
      LEVEL2_POWER1.clearbricks()
      LEVEL2_POWER2 = level2_Power2()
      LEVEL2_POWER2.assign_color()
      LEVEL2_POWER3 = level2_Power3()
      LEVEL2_POWER3.assign_color()
      LEVEL2_POWERINF = level2_Powerinf()
      LEVEL2_POWERINF.assign_color()
      #LEVEL2_EXPLOADBRICK = level2_Exploadbrick()
      #LEVEL2_EXPLOADBRICK.assign_color()   
   
   
   
   '''
   if newtime > 10:
      if newtime%5 == 0:
         factor = int((newtime - 10)/5) 
         j = 36
         while j>3:
            for i in range(4,75):
               if getbrick.power[j][i]>0:
                  getbrick.power[j+factor][i]=getbrick.power[j][i]
                  getbrick.power[j][i]=0
                  for k in range(0,5):
                     getboard.board[j+factor][i-k]=getboard.board[j][i-k]
                     getboard.board[j][i-k] = " "
            j -= 1
   '''
   
   #move paddle
   PADDLE.move_paddle()
   if PADDLE.flag == 1:
      BALLCOLLISION.moveball()

   #rainbow
   if rainbow == 0:
      if(int(newtime%3) == 1):
         getbrick.power[14][60] = 1
         getboard.board[14][60] = Back.LIGHTGREEN_EX+")"+Back.RESET
         getboard.board[14][56] = Back.LIGHTGREEN_EX+"("+Back.RESET
         getboard.board[14][57] = Back.LIGHTGREEN_EX+"$"+Back.RESET 
         getboard.board[14][58] = Back.LIGHTGREEN_EX+"$"+Back.RESET 
         getboard.board[14][59] = Back.LIGHTGREEN_EX+"$"+Back.RESET 
      if(int(newtime%3) == 2):
         getbrick.power[14][60] = 2
         getboard.board[14][60] = Back.LIGHTCYAN_EX+")"+Back.RESET
         getboard.board[14][56] = Back.LIGHTCYAN_EX+"("+Back.RESET
         getboard.board[14][57] = Back.LIGHTCYAN_EX+"$"+Back.RESET 
         getboard.board[14][58] = Back.LIGHTCYAN_EX+"$"+Back.RESET 
         getboard.board[14][59] = Back.LIGHTCYAN_EX+"$"+Back.RESET 
      if(int(newtime%3) == 0):
         getbrick.power[14][60] = 3
         getboard.board[14][60] = Back.RED+")"+Back.RESET
         getboard.board[14][56] = Back.RED+"("+Back.RESET
         getboard.board[14][57] = Back.RED+"$"+Back.RESET 
         getboard.board[14][58] = Back.RED+"$"+Back.RESET 
         getboard.board[14][59] = Back.RED+"$"+Back.RESET 
   
   if BALLCOLLISION.y + BALLCOLLISION.yv == 14   and BALLCOLLISION.x+ BALLCOLLISION.xv < 61 and BALLCOLLISION.x+ BALLCOLLISION.xv > 55:
      #os.system('aplay -q ./sounds/explosion.wav&')
      rainbow = 1
      
   