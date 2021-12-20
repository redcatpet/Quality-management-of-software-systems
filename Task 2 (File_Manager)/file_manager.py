import sys
import os
import shutil
import send2trash

print('Welcome to the file-manager\n')

# Сохраняет каждый накопитель, подключенный к ПК, в список
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

# Перечисляет каждую папку и файл, присутствующий в текущем рабочем каталоге
def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)

while True:
    print("1.Open files/folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n")
    result = input("Choose one of the following: ")

    if result == '1':
        # Домашний экран
        print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')

        print('Drives: ')
        for x in range(len(drives)):
            print(str(5 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp == '1':
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '2':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '3':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '4':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break

            elif inp in drives:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct input / drive name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            res = input('\nChoose a file/folder: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    os.system('"' + res + '"')
                else:
                    os.chdir(res)

            elif res == 'exitManager':                    # Команда Exit для выхода из цикла
                sys.exit(0)

            elif res == 'backManager':                    # Команда назад для перехода на олин каталог вверх
                os.chdir('..')

            else:
                print('No file/folder exist of this name.')

    if result == '2':
        print("You chose to rename")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            print('Type "renameManager" to rename this directory')

            res = input('\nChoose a file to rename: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):

                    new_name = input("Enter a new name: ")
                    ogDir = res
                    newDir = os.getcwd() + '\\' + new_name
                    shutil.move(ogDir, newDir)
                else:
                    os.chdir(res)

            elif res == 'exitManager':    # Команда Exit для выхода из цикла
                sys.exit(0)

            elif res == 'backManager':    # Команда для перехода на один каталог вверх
                os.chdir('..')

            elif res == 'renameManager':  # Команда Rename для удаления одного каталога

                new_name = input("Enter a new name: ")
                ogDir = os.getcwd()
                os.chdir('..')
                newDir = os.getcwd() + '\\' + new_name
                shutil.move(ogDir, newDir)

            else:
                print('No file/folder exist of this name.')

    if result == '3':
        print("You chose to move")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            print('Type "cutManager" to move this directory')

            res = input('\nChoose a file to move: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("\nMove " + res + " to a desired location.")

                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])

                        inp2 = input("\nEnter your Choice: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a correct drive name.\n')

                    while True:
                        listDirectories()

                        print('Type "pasteManager" to paste this file in current directory')

                        res2 = input('\nChoose a file to move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")
                            else:
                                os.chdir(res2)

                        elif res2 == 'pasteManager':
                            shutil.move(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == 'exitManager':              # Команда Exit для выхода из цикла
                sys.exit(0)

            elif res == 'backManager':              # Команда назад для перехода на один каталог вверх
                os.chdir('..')

            elif res == 'cutManager':
                og_path = os.getcwd()

                print("Moving the current directory")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])

                    inp2 = input("\nEnter your Choice: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:
                    listDirectories()

                    print('\nType "pasteManager" to paste this folder in current directory')

                    res2 = input('\nChoose a folder to open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")
                        else:
                            os.chdir(res2)

                    elif res2 == 'pasteManager':
                        shutil.move(og_path, os.getcwd())
                        break

            else:
                print('No file/folder exist of this name.')

    if result == '4':
        print("You chose to copy")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            print('Type "copyManager" to copy this directory')

            res = input('\nChoose a file to copy: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("Move " + res + " to a desired location.")

                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])

                        inp2 = input("\nEnter your Choice: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a correct drive name.\n')

                    while True:
                        listDirectories()

                        print('Type "pasteManager" to copy this file in current directory')

                        res2 = input('\nChoose a file to move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")
                            else:
                                os.chdir(res2)

                        elif res2 == 'pasteManager':
                            shutil.copy(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == 'exitManager':  # Команда Exit для выхода из цикла
                sys.exit(0)

            elif res == 'backManager':  # Команда назад для перехода на один каталог вверх
                os.chdir('..')

            elif res == 'copyManager':
                og_path = os.getcwd()

                print("Copying the current directory")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])

                    inp2 = input("\nEnter your Choice: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:
                    listDirectories()

                    print('\nType "pasteManager" to copy this file in current directory')

                    res2 = input('\nChoose a folder to open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")
                        else:
                            os.chdir(res2)

                    elif res2 == 'pasteManager':
                        print(og_path)
                        folder_name = og_path.split('\\')[-1]
                        folder_directory = os.getcwd() + '\\' + folder_name
                        shutil.copytree(og_path, folder_directory)
                        break

            else:
                print('No file/folder exist of this name.')

    if result == '5':
        while True:

            # Опции для удаления файлов/папок навсегда или иным образом
            print('\n1. Permanently \n2. Recycle Bin')
            query = input('Would you like to permanently delete or send to Recycle Bin?: ')

            if query == '1':
                print('You chose to permanently delete files/folders.\n')
                print('Drives: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])

                while True:
                    inp = input("\nEnter your Choice: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirectories()

                    print('\n\nType "exitManager" to exit from file manager.')
                    print('Type "backManager" to go up one directory.')
                    print('Type "deleteManager" to permanently delete this directory')

                    res = input('\nChoose a file to delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            # Предупреждение, чтобы предотвратить ненужное удаление
                            print('Are you sure you want to permanently delete this file? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                os.unlink(res)
                        else:
                            os.chdir(res)

                    elif res == 'exitManager':                      # Команда Exit для выхода из цикла
                        sys.exit(0)

                    elif res == 'backManager':                      # Команда назад для перехода на один каталог вверх
                        os.chdir('..')

                    elif res == 'deleteManager':                    # Удалить команду для удаления одного каталога

                        # Предупреждение, чтобы предотвратить ненужное удаление
                        print('Are you sure you want to permanently delete this folder? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            shutil.rmtree(path)

                    else:
                        print('No file/folder exist of this name.')

            elif query == '2':
                print('You chose to temporarily delete files/folders.')
                print('Drives: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])

                while True:
                    inp = input("\nEnter your Choice: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirectories()

                    print('\n\nType "exitManager" to exit from file manager.')
                    print('Type "backManager" to go up one directory.')
                    print('Type "deleteManager" to send this directory to recycle bin')

                    res = input('\nChoose a file to delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            # Предупреждение, чтобы предотвратить ненужное удаление
                            print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                send2trash.send2trash(res)
                        else:
                            os.chdir(res)

                    elif res == 'exitManager':    # Команда Exit для выхода из цикла
                        sys.exit(0)

                    elif res == 'backManager':    # Команда назад для перехода на один каталог вверх
                        os.chdir('..')

                    elif res == 'deleteManager':  # Удалить команду для удаления одного каталога

                        # Предупреждение, чтобы предотвратить ненужное удаление
                        print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            send2trash.send2trash(path)

                    else:
                        print('No file/folder exist of this name.')

        else:
            print('You chose wrong number')