import os


#NUMBER 1

first_num = int (input ("Введите число: "))
second_num = first_num + 1
third_num = first_num + 2

print (first_num)
print (second_num)
print (third_num)

input ()

os.system('cls')


#NUMBER 2

first = int (input ("Число #1: "))
second = int (input ("Число #2: "))
third = int (input ("Число #3: "))

sum = first + second + third

print (sum)

input ()

os.system('cls')


#NUMBER 3

ребро = int (input ("Введите длину ребра: "))
Обьем = ребро ** 3
Площадь = 6 * (ребро ** 2)

print ("Обьем куба = ", Обьем)
print ("Площадь полной поверхности = ", Площадь)

input ()

os.system('cls')


#NUMBER 4

a = int (input ("Число #1: "))
b = int (input ("Число #2: "))
f = 3 * (a + b) ** 3 + 275 * b ** 2 -127 * a - 41

print (f)

input ()

os.system('cls')


#NUMBER 5

a = int (input ("Число #1: "))
f = a + 1
n = a - 1

print (f"Следущее за числом {a} число: {f}")
print (f"Предыдущее для числа {a} число:{n}")

input ()

os.system('cls')


#NUMBER 6

a = int (input ("Стоимость монитора: "))
b = int (input ("Стоимость системного блока: "))
c = int (input ("Стоимость клавиатуры: "))
d = int (input ("Стоимость мыши: "))

sum = int (a + b + c + d) * 3
print ("Стоимость покупки = ", sum)

input ()

os.system('cls')


#NUMBER 7

a_1 = int (input())
d = int (input())
n = int (input())
a_n = a_1 + d * (n - 1)

print ("n-ый член арифметической прогрессии: ", a_n)

input ()

os.system ('cls')


#NUMBER 8

x1 = int (input ("Введите число: "))
x2 = x1 * 2
x3 = x2 + x1
x4 = x3 + x1
x5 = x4 + x1

print(x1, x2, x3, x4, x5, sep = '---')

input ()

os.system('cls')


#NUMBER 9

n = int (input ("Количество школьников: "))
k = int (input ("Мандаринки: "))
one = n // k
two = n % k

print ("Количество мандаринок, которое досталось каждому школьнику: ", one)
print ("Количество мандаринок в корзине : ", two)

input ()

os.system('cls')


#NUMBER 10

a = int (input())

print (a // 2 + a%2)

input ()

os.system('cls')


#NUMBER 11

m = int (input ("Введите число: "))
h = m // 60
s = m % 60

print(m, "мин это - ", h, "час", s, "минут.")

input ()

os.system('cls')


#NUMBER 12

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100

print("Сумма цифр = ", c + b + a)
print("Произведение цифр = ", c * b * a)

input ()

os.system('cls')


#NUMBER 13

p = input()

print('    _~_    ' *int(p))
print('   (o o)   ' *int(p))
print('  /  V  \  ' *int(p))
print(' /(  _  )\ ' *int(p))
print('   ^^ ^^   ' *int(p))

input ()

os.system('cls')


#NUMBER 14

abc = int (input())
x = 1
n = (x // 10 ** k) % 10

print(n)

input ()

os.system('cls')


#NUMBER 15

a = int (input())
h = a % (60 * 24) // 60
m = a % 60

print(h, m)

input ()

os.system('cls')


#NUMBER 16

a = int (input())
print(1 - a)

input ()

os.system('cls')


#NUMBER 17

a = int (input())
print((a // 2 + 1) * 2)

input ()

os.system('cls')


#NUMBER 18

v = int(input())
t = int(input())
a = v * t
n = a // 109
print(-(109 * n - a))

input ()

os.system('cls')


#NUMBER 19

a = float (input ("#1: "))
b = float (input ("#2: "))
c = float (input ("#3: "))

print (int (1 + (a - c - 1) / (b - c)))

input ()

os.system('cls')