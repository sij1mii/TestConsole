#2次元リストでコンソールアニメ
import os
import time
#import console

A = '● '
B = '□ '
C = '* '
D = '  '

def Loop1():
  while True:
    n = 0
    x = 11
    count = 0

    board = [[D for n in range(21)]for i in range(21)]
    #nが10以上になるとエラー
    #nが10になったら1を代入
    while count < 24:
      n += 1
      x -= 1
      count += 1

      #下から表示
      if count < 5:
        board[(x+10)-2][9+n]=A#右
        board[(x+10)-2][x]=A#左
      elif 4 < count < 7:
        board[(x+10)-2][13]=A
        board[(x+10)-2][7]=A
      elif 6 < count < 9:
        board[12][x+8]=A
        board[12][n+1]=A
      elif 8 < count < 10:
        board[13][10]=A

      #消す
      if 9 < count:
        board[18][10]=D 
      if 10 < count < 14:
        board[(x+10)-3][10+n]=D
        board[(x+10)-3][x-1]=D
      elif 13 < count < 16:
        board[x+7][13]=D
        board[x+7][7]=D
      elif 15 < count < 18:
        board[12][x+7]=D
        board[12][n+2]=D
      elif 17 < count < 19:
        board[13][10]=D

      #*上からから
      if 13 < count < 16:
      	board[x+5][n+6]=C
      	board[x+5][x+3]=C
      #elif 15 < count < 18:
      	#board[n-]
      	
      #*下から
      if 13 < count < 18:
        board[x+12][6+n]=C      
        board[x+12][x+3]=C
      	
      elif 17 < count < 21:
        board[x+12][14]=C
        board[x+12][6]=C
      elif 20 < count < 23:
        board[x+2][x+3]=C
        board[x+2][n+6]=C
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
	
Loop1()
