# _author_ = "Макаров Александр Александрович"

#Задача №1
count = [6,9,4,8,6]
i=max(count)
print(i)

#Задача №2
a=2,
b=6,
a,b=b,a
print(a)

#Задача №3
import math
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
discr = (b**2)-4*(a*c)
if discr > 0:
    x1=(-b+math.sqrt(discr)/(2*a))
    x2=(-b-math.sqrt(discr)/(2*a))
    print("Перый корень=",x1,"Второй корень=",x2)
elif discr==0:
    x=-b/(2*a)
    print("Корень равен:",x)
else:
    print("Корней нет")
