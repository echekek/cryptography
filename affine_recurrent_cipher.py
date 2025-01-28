def evk(a,b): #расширенный алгоритм евклида
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

def z(s,k1,k2): # функция для зашифрования
    x=[a.index(i) for i in s] #преобразуем буквенную строчку в числовую
    y1=[]
    for i in x:
        y1.append((i*k1[0]+k1[1])%len(a)) #шифруем и добавляем в ответ символ
        k=[k1[0]*k2[0],k1[1]+k2[1]] # формируем новый ключ
        k1=k2
        k2=k
    y2 = [a[i] for i in y1] #преобразуем числовую строчку в буквенную
    return y2

def r(s,k1,k2): # функция для расшифрования
    y1 = [a.index(i) for i in s] #преобразуем буквенную строчку в числовую
    x1=[]
    for i in y1:
        k1[0]=a_1(k1[0],len(a)) #найдем обратный элемент а
        if not k1[0]:
            return "incorrect key"
        x1.append((i-k1[1])*k1[0]%len(a)) #расшифруем и добавим в ответ символ
        k=[k1[0]*k2[0],k1[1]+k2[1]] # формируем новый ключ
        k1=k2
        k2=k
    x2 = [a[i] for i in x1] #преобразуем числовую строчку в буквенную
    return x2

s=input("enter the text: ").lower()
print("enter the keys (a,b): ")
k1 = [int(i) for i in input().split()]
k2 = [int(i) for i in input().split()]

a="abcdefghijklmnopqrstuvwxyz "

if input('''enter 1 to encrypt
enter 2 to decrypt
''')=='1':
    [print(i,end='') for i in z(s,k1,k2)]
else:
    [print(i,end='') for i in r(s,k1,k2)]
