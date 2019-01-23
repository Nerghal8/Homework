#___author___ Макаров Александр Александрович

#Задача №1
import math
count=[2, -5, 8, 9, -25, 25, 4]
for i in count:
    if i>0 and (math.sqrt(i)-int(math.sqrt(i)))==0:
       print([i])

#Задача №2

date = ["10.12.2015"]
dic = {'10':'Десятое','12':'декабря'}
for key in date.keys:
    print(key,"2015 года.")