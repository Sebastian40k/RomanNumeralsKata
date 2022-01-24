M = 0
D = 0
C = 0
L = 0
X = 0
V = 0
I = 0

Total = int(input())
M = int(Total/1000)
Ml = Total % 1000
if(Ml != -0):
    D = int(Ml/500)
    Dl = Ml % 500
    if(Dl != 0):
        C = int(Dl/100)
        Cl = Dl % 100
        if(Cl != 0):
            L = int(Cl/50)
            Ll = Cl % 50
            if(Ll != 0):
                X = int(Ll/10)
                Xl = Ll % 10
                if(Xl != 0):
                    V = int(Xl/5)
                    I = Xl % 5
for x in range(M):
    print("M", end='')
if(D == 1 and C == 4):
    print('CM', end='')
else:
    if(D > 0):
        print('D', end='')
    for x in range(C):
        print('C', end='')
if(L == 1 and X == 4):
    print('XC', end='')
else:
    if(L > 0):
        print('L', end='')
    for x in range(X):
        print('X', end='')
if(V == 1 and I == 4):
    print('IX', end='')
else:
    if(V > 0):
        print('V', end='')
    for x in range(I):
        print('I', end='')
print()
