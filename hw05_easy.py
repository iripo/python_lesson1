# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.


import os
def mdir1_9():
    for i in range(9):
        i=i+1
        fname=('{}''{}''{}').format('dir', "_",i)
        dir_path = os.path.join(os.getcwd(), fname)
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')
        i+=1
		

        
		

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def shdir1():
	dir_list=next(os.walk('.'))[1]
	return dir_list

def shdir2():
    dir_list=[]
    for i in os.listdir():
        if os.path.isdir(os.path.join(os.getcwd(),i)):
            all_items.append(i)
    return dir_list

# И второй скрипт, удаляющий эти папки.

def remdir1_9():
    for i in range(9):
        i=i+1
        fname=('{}''{}''{}').format('dir', "_",i)
        dir_path = os.path.join(os.getcwd(), fname)
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print('Такой директории не существует')
        i+=1




# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import os
import shutil
shutil.copy(sys.argv[0],os.path.join(os.getcwd(),'script_copy.py'))

#For normal hw

def chdir(fname):
    dir_path = os.path.join(os.getcwd(), fname)
    try:
        os.chdir(dir_path)
        print(('Вы перешли в папку ''{}').format(dir_path))
    except FileNotFoundError:
        print('Такой директории не существует')

def remdir(fname):
    dir_path = os.path.join(os.getcwd(), fname)
    try:
        os.rmdir(dir_path)
        print(('Папка ''{}'' удалена.').format(fname))
    except FileNotFoundError:
        print('Такой директории не существует')

def mdir(fname):
    dir_path = os.path.join(os.getcwd(), fname)
    try:
        os.mkdir(dir_path)
        print(('Папка ''{}'' создана.').format(fname))
    except FileExistsError:
        print('Такая директория уже существует')

def shdir():
	dir_list=next(os.walk('.'))[1]
	print(('Cодержимое текущей папки: ''{}').format(dir_list))