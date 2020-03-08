#2次元リストでコンソールアニメ
import os
import time
#import console

class LoopAnime():
  def __init__(self):
    self.A = '● '
    self.B = '□ '
    self.C = '* '
    self.D = '  '

  def Loop1(self):
    while True:
      n = 0
      x = 11
      count = 0

      board = [[self.D for n in range(21)]for i in range(21)]
      #nが20以上になるとエラー
      #nが20になったら1を代入
      while count < 20:
        n += 1
        x -= 1
        count += 1

        #下から表示
        if count < 5:
          board[(x+10)-2][9+n]=self.A#右
          board[(x+10)-2][x]=self.A#左
        elif 4 < count < 7:
          board[(x+10)-2][13]=self.A
          board[(x+10)-2][7]=self.A
        elif 6 < count < 9:
          board[12][x+8]=self.A
          board[12][n+1]=self.A
        elif 8 < count < 10:
          board[13][10]=self.A

        #消す
        if 9 < count < 11:
          board[18][10]=self.D
        elif 10 < count < 14:
          board[(x+10)-3][10+n]=self.D
          board[(x+10)-3][x-1]=self.D
        elif 13 < count < 16:
          board[x+7][13]=self.D
          board[x+7][7]=self.D
        elif 15 < count < 18:
          board[12][x+7]=self.D
          board[12][n+2]=self.D
        elif 17 < count < 19:
          board[13][10]=self.D

        #*上からから
        if 13 < count < 16:
          board[x+5][n+6]=self.C
          board[x+5][x+3]=self.C

        elif 15 < count < 18:
          board[n+5][x+3]=self.C
          board[n+5][n+6]=self.C
        elif 17 < count:
          board[13][6]=self.C
          board[13][14]=self.C
          
        #*下から
        if 13 < count < 18:
          board[x+12][6+n]=self.C      
          board[x+12][x+3]=self.C      	
        elif 17 < count < 20:
          board[x+12][14]=self.C
          board[x+12][6]=self.C
        #elif 20 < count < 23:
          #board[x+2][x+3]=C
          #board[x+2][n+6]=C
        #elif 22 < count < 25:
          #board[n+8][x+3]=C
          #board[n+8][n+6]=C

        #リストの括弧など非表示 ボード表示
        for board2 in board:
          print(' '.join(board2))

        print('n=',n)
        print('x=',x)
        print(count)
        time.sleep(0.3)
        #console.clear()
        #os.system('clear')

        if n == 10:
          n = 0
        if x == 1:
          x = 11
	
if __name__=='__main__':

  loopani = LoopAnime()
  loopani.Loop1()

