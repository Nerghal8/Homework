#___author___ "Макаров Александр Александрович"

#Задача №1
num1 = [3,5,15,47,13,7]
num2 = [x**2 for x in num1]
print(num2)

#Задача №2
lst1 = ["apple","banana","orange","kiwi"]
lst2 = ["kiwi","grapefruit","avokado","banana"]
lst3 = [x for x in lst1 if x in lst2] if len(lst1)>len(lst2) else [x for x in lst2 if x in lst1]
print(lst3)

#Задача №3
nums=[1,9,7,18,23,36,82,100]
nums2=[i for i in nums if i%3==0 and i>0 and i%4!=0]
print(nums2)