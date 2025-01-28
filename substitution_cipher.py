
def z(s,k): #зашифрование строки s ключом k
    x=[a.index(i) for i in s] #преобразуем буквенную строчку в числовую
    y1=[k.index(i) for i in x] #шифруем каждый символ
    y2 = [a[i] for i in y1] #преобразуем числовую строчку в буквенную
    return y2

def r(s,k): # расшифрование строки s ключом k
    y1 = [a.index(i) for i in s] #преобразуем буквенную строчку в числовую
    x1 = [k[i] for i in y1] #расшифровываем каждый символ
    x2 = [a[i] for i in x1] #преобразуем числовую строчку в буквенную
    return x2

s=input("enter the text: ").lower()
k1 = input("enter the key: ").lower()

a="abcdefghijklmnopqrstuvwxyz "
k=[a.index(i) for i in k1] # преобразуем ключ из букв в числа

if input('''enter 1 to encrypt
enter 2 to decrypt
''')=='1':
    [print(i,end='') for i in z(s,k)]
else:
    [print(i,end='') for i in r(s,k)]

