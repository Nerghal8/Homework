__author__ =  "Макаров Александр Александрович"
import os
import sys
from shutil import copyfile

#Задача №1
def makedir(dirr=os.getcwd()):
    for i in range(10):
        try:
         path=os.path.join(dirr + "dir" +str(i))
         os.mkdir(path)
        except FileExistsError:
            print("Такая дирректория уже существует!")

def remove_dir(dirname = str(input("Введите название папки:"))):
    try:
        if dirname!=None:
         os.removedirs(dirname)
    except FileNotFoundError:
        print("Дирректория не существует!")
    except PermissionError:
        print("Нет доступа")

#Задача №2
def getdir (dirsaw=os.getcwd()):
    def get_folders_cuttent_dir(path=os.getcwd()):
        return [i for i in os.listdir(path) if not os.path.isfile(os.path.join(path, i))]

#Задача №3
def copir(file = sys.argv[0]):
    try:
        os.mkdir(os.path.join(os.getcwd(),"copy"))
    except FileExistsError:
        print('Директория уже существует')
    try:
        for i in range(float("inf")):
         i += 1
         print(os.path.join(os.getcwd(),sys.argv[0]))
         new_file = str.split(sys.argv[0],".")[0] + i +".py"
         copyfile(file, os.path.join(file, new_file))
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print('Нет доступа.')