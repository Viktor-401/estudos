texto1 = 'aaaaaa#bbbbbbbbbbbbbbbbb#cccccccccc#dddddddddddddddddd#eeeeeeeeeeeeeeeeee#'

print(texto1[:texto1.index('#')])

print(texto1[texto1.index('#')+1:texto1.index('#',texto1.index('#')+1)])

print(texto1[texto1.index('#',texto1.index('#')+1)+1:texto1.index('#',texto1.index('#',texto1.index('#')+1)+1)])

print(texto1[texto1.index('#',texto1.index('#',texto1.index('#')+1)+1)+1:texto1.index('#',texto1.index('#',texto1.index('#',texto1.index('#')+1)+1)+1)])

print(texto1[texto1.index('#',texto1.index('#',texto1.index('#',texto1.index('#')+1)+1)+1)+1:texto1.index('#',texto1.index('#',texto1.index('#',texto1.index('#',texto1.index('#')+1)+1)+1)+1)])