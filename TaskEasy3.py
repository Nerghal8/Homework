#__Author__ = Макаров Александр Алексаднрович

#Задача №1
km = 1
def convert(km):
    miles = km*0.609
    return miles
dist = convert(264)
print(dist)

#Задача №2
def my_round(number):
    number = round(number)
    ndigits = (number % 1)
    summ=(number)+(ndigits)
    if ndigits >= 5:
        summ=summ+0.41
    return summ
res=my_round(2.645)
print("sum =>",res)

#Задача №3
def lucky_ticket(num):
    num=(list(map(int, list(str(num)))))
    if sum(num[:3]) == sum(num[3:]):
        print("True")
    else:
        print("False")
    return num
ticket=lucky_ticket(123321)