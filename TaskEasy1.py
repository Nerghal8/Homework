_author_ = "Макаров Александр Александрович"
#Задача №1
number = 21348
while number > 0:
    print(-number%10)
    number = (number // 10)

#Задача №2
a = input("Введите значение переменной a:")
b = input("Введите значение переменной b:")
c=b
b=a
a=c

#Задача №3
age=int(input("Укажите ваш возраст:"))
if age >= 18:
    print("Доступ разрешен.")
else:
    print("Извините, пользование данным ресурсом только с 18 лет.")
