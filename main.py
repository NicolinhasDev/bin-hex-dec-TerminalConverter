import os

#conversor decimal ---> outras bases
def conversor(x,y,a):
    p = x
    nc = []
    while x > 0:
        r = x // y
        if x%y == 10:
            nc.append('A')
        elif x%y == 11:
            nc.append('B')
        elif x%y == 12:
            nc.append('C')
        elif x%y == 13:
            nc.append('D')
        elif x%y == 14:
            nc.append('E')
        elif x%y == 15:
            nc.append('F')
        else:
            nc.append(x%y)
        x = r
    nc.reverse()
    i = len(nc)
    #saída
    print('O número ({}){} na base {} vale: {}'.format(p, 10, y, a) + ''.join(map(str,nc)))

#conversor outras bases ---> decimal

def conversor2(x,y,z,a):
    p = x
    hexDict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10, 'B':11,'C':12,'D':13,'E':14,'F':15}
    if y == 16:
        res = 0
        xs = x.upper().strip()
        nd = len(xs) -1
        for digit in xs:
            res += hexDict[digit]*16**nd
            nd -= 1
    else:
        n = int(x)
        res = 0
        for m in range(0, z+1):
            i = n
            u = n // 10
            i = i - (u * 10)
            c = i * (y ** m)
            res = res + c
            n = u
    #saída
    print('O número ({}){} na base {} vale: {}{}'.format(p, y, 10, a, res))

#início programa

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t\tCalculadora de Bases Numéricas\n[1]Decimal ---> Outras Bases\n[2]Outras Bases ---> Decimal\n[0]Sair')

    c = int(input('Digite a função desejada: '))
    if c == 0:
        break
    if c == 1:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\t\tCalculadora de Bases Numéricas\n[1]Decimal ---> Binário\t[2]Decimal ---> Octal\t[3]Decimal ---> Hexadecimal')
            
            c = int(input('Digite a função desejada: '))

            if c == 1:
                b = 2
                a = '0b'
            elif c == 2:
                b = 8
                a = '0o'
            elif c == 3:
                b = 16
                a = '0x'

            n = int(input('Digite o número a ser convertido: '))

            conversor(n, b, a)
            break
    elif c == 2:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\t\tCalculadora de Bases Numéricas\n[1]Binário ---> Decimal\n[2]Octal ---> Decimal\n[3]Hexadecimal ---> Decimal')
            
            c = int(input('Digite a função desejada: '))
            
            if c == 1:
                b = 2
                a = '0b'
            elif c == 2:
                b = 8
                a = '0o'
            elif c == 3:
                b = 16
                a = '0x'

            n = input('Digite o número a ser convertido: ')
            t = len(str(n))
            conversor2(n, b, t, a)
            break
    break
    