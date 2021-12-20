from file_manager import *
import os
import shutil
import send2trash
import pytest

file_name = 'Test.txt'
file_content = 'Hello world '
test_name = 'ABTest'
test_name2 = 'File_here'
change_directory = 'Move_to_Dir'
original_name = 'Rename_my.txt'
Second_name = 'Renamed_file.txt'


@pytest.fixture()
def file_edit():
    global file_name, file_content
    touch(file_name)
    edit_file(file_name, file_content)
    return os.path.getsize(file_name)

def test_file_edit(file_edit):
    global file_name
    assert file_edit != 0
    rm(file_name)


#Запись в файл + просмотр содержимого
@pytest.fixture()
def file_cont():
    global file_name, file_content
    touch(file_name)
    edit_file(file_name, file_content)

    with open(file_name,'r',encoding='utf-8') as content:
        content = content.read()
        print(content)
    return content

def test_file_cont(file_cont):
    global file_content, file_name
    assert file_cont == file_content and os.path.getsize(file_name) != 0


#Создание пустого файла по имени
@pytest.fixture()
def File_creation():
    global file_name
    touch(file_name)
    return file_name

def test_File_creation(File_creation):
    assert File_creation in F_list('')


#Удаление файла по имени
@pytest.fixture()
def Delete_file():
    global file_name
    rm(file_name)
    return file_name

def test_Delete_file(Delete_file):
    assert Delete_file not in F_list('')


#Создание папки по имени
@pytest.fixture()
def Make_Directory():
    global test_name
    mkdir_py(test_name)
    return test_name

def test_Make_Directory(Make_Directory):
     assert Make_Directory in F_list('')


#Удаление папки по имени
@pytest.fixture()
def Del_Dir():
    global test_name
    dir_rem(test_name)
    return test_name

def test_del_dir(Del_Dir):
    assert Del_Dir not in F_list('')


#Перемещение по папкам
@pytest.fixture()
def dir_switch_f():
    global change_directory,file_name
    path1 = os.getcwd()
    mkdir_py(change_directory)
    chdir(change_directory)
    touch('Move.txt')
    return path1


def test_dir_switch_f(dir_switch_f):
    assert dir_switch_f != os.getcwd()


#Перемещение по папкам
@pytest.fixture()
def dir_switch_b():
    path2 = os.getcwd()
    chdir('back')
    return path2

def test_dir_switch_b(dir_switch_b):
    origin_path = os.getcwd()
    assert dir_switch_b != origin_path


#Копирование файлов
@pytest.fixture()
def copyTO():
    dir_name = 'File_Copies'
    name_of_file = 'file_to_copy.txt'
    mkdir_py(dir_name)
    touch(name_of_file)
    curDir = False
    nextDir = False
    still = False
    if name_of_file in F_list(''):
        curDir = True
    copy_folder(name_of_file, dir_name)
    chdir(dir_name)
    if name_of_file in F_list(''):
        nextDir = True
    chdir('back')
    if name_of_file in F_list(''):
        still = True
    if curDir == nextDir == still:
        return True
    else:
        return False

def test_copy_to_dir(copyTO):
    assert copyTO == True


#Перемещение файла из папки в другую папку
@pytest.fixture()
def move_to_dir():
    global file_name, test_name2
    touch(file_name)
    mkdir_py(test_name2)
    cDir = False
    nDir = False
    still = False
    if file_name in F_list(''):
        cDir = True
    moveto(file_name,test_name2)
    chdir(test_name2)
    if file_name in F_list(''):
        nDir = True
    chdir('back')
    if file_name in F_list(''):
        still = True
    if cDir == nDir and cDir != still:
        return True

def test_move_to_dir(move_to_dir):
    assert move_to_dir == True


#Переименование файлов
@pytest.fixture()
def rename_file():
    global original_name, Second_name
    touch(original_name)
    rename(original_name, Second_name)

def test_rename_file(rename_file):
    global original_name, Second_name
    assert original_name not in F_list('') and Second_name in F_list('')
    rm(Second_name)