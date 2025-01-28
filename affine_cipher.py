def evk(a,b): # расширенный алгоритм евклида
    if b>a:
        a,b=b,a
    x2=1
    x1=0
    y2=0
    y1=1
    while b!=0:
        q=a//b
        r=a-q*b
        x=x2-q*x1
        y=y2-q*y1

        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
    return (a,x2,y2) #НОД,х,у из ax+by=НОД

def a_1(a,m): # нахождение обратного элемента a по mod m
    d,x,y=evk(m,a)
    if d>1:
        return 0
    elif d==1:
        return y%m

def z(s,k): # функция для зашифрования
    x=[a.index(i) for i in s] #преобразуем буквенную строчку в числовую
    y1=[(i*k[0]+k[1])%len(a) for i in x] #шифруем каждый символ
    y2 = [a[i] for i in y1] #преобразуем числовую строчку в буквенную
    return y2

def r(s,k): # функция для расшифрования
    y1 = [a.index(i) for i in s] #преобразуем буквенную строчку в числовую
    k[0]=a_1(k[0],len(a)) #найдем обратный элемент а
    if not k[0]:
        return "incorrect key"
    x1=[(i-k[1])*k[0]%len(a) for i in y1]  #расшифровываем каждый символ
    x2 = [a[i] for i in x1] #преобразуем числовую строчку в буквенную
    return x2

s=input("enter the text: ").lower()
print("enter the key (a,b): ")
k = [int(i) for i in input().split()]

a="abcdefghijklmnopqrstuvwxyz "

if input('''enter 1 to encrypt
enter 2 to decrypt
''')=='1':
    [print(i,end='') for i in z(s,k)]
else:
    [print(i,end='') for i in r(s,k)]
