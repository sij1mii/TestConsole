#20x20表

a = int(input('カウント数入力 : '))
aa = a%10 #１の位抽出

c = 11 - aa #マイナスの場合

L = int(input('縦番号入力 : '))
xL = L - c #マイナスの場合
nL = L - aa #プラスの場合

W = int(input('横番号入力 : '))
xW = W -c #マイナスの場合
nW = W - aa #プラスの場合

print('x= -  n= +')
print('縦','xL+',xL,'nL+',nL)
print('横','xW+',xW,'nW+',nW)
