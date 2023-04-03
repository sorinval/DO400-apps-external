# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import stat


def renameFile(oldNm, newNm):
    try:
        os.rename(oldNm, newNm)
        print("changed ", oldNm, "==>", newNm)
    except IOError as er:
        print("renameFile IO error: ", er)
        return 1
    print("exit renameFile")
    return 0

def chmodFile(fileNm, priv):
    try:
        os.chmod(fileNm, priv)
        print("chmod ", fileNm, "==>", priv)
    except IOError as er:
        print("chmodFile IO error: ", er)
        return 1
    print("exit chmodFile")
    return 0

import shutil


def copyFl(oldNm, newNm):
    try:
        shutil.copyfile(oldNm, newNm)
        print("copied ", oldNm, "==>", newNm)
    except IOError as er:
        print("copyFl IO error: ", er)
        return 1
    print("exit copyFl")
    return 0

def moveFl(oldNm, newNm):
    try:
        shutil.move(oldNm, newNm)
        print("moved ", oldNm, "==>", newNm)
    except IOError as er:
        print("moveFl IO error: ", er)
        return 1
    print("exit moveFl ")
    return 0


def copyDr(oldNm, newNm):
    try:
        shutil.copytree(oldNm, newNm, symlinks=True)
        print("copied diectory", oldNm, "==>", newNm)
    except IOError as er:
        print("copyDr IO error: ", er)
        return 1
    print("exit copyDr")
    return 0

def replaceStringInFile(fileIn, oldString, newString, fileOut):
    try:
        if len(fileIn) == 0 or len(oldString) == 0 or len(fileOut) == 0 :
            print("replaceStringInFile - ERROR invalid arguments ", fileIn, oldString, fileOut, sep="|")
            return 1
        fin = open(fileIn, "rt")
        fout = open(fileOut, "wt")
        for line in fin:
            fout.write(line.replace(oldString, newString))
        fin.close()
        fout.close()
        print("replaceStringInFile done ", fileIn, "==>", fileOut, oldString, "-->", newString)
    except IOError as er:
        print("replaceStringInFile IO error: ", er)
        return 1
    print("exit replaceStringInFile")
    return 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #renameFile("C:\\tmp\\test1.txt", "C:\\tmp\\test2.txt")
    #copyFl("C:\\tmp\\test2.txt", "C:\\tmp\\test3.txt")
    copyDr("C:\\tmp\\AA", "C:\\tmp\\BB")
    #moveFl("C:\\tmp\\AA\\test2.txt", "C:\\tmp\\BB\\test23.txt")
    replaceStringInFile("C:\\tmp\\BB\\test23.txt","g","gelu", "C:\\tmp\\BB\\test23a.txt")
    # renameFile("C:\\tmp1", "C:\\tmp")
    print(stat.S_IREAD, stat.S_IWRITE, stat.S_IEXEC)
    chmodFile("C:\\tmp\\test3.txt", 0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
