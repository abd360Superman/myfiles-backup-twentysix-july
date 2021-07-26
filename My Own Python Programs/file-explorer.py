from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb
from send2trash import send2trash
from pathlib import Path
import zipfile

def new_file():
    mb.showinfo('confirmation', 'Select location for new file')
    path = filedialog.askdirectory()
    print('Enter new name for file')
    name = input()
    print('Enter the file type')
    ftype = input()
    final_path = os.path.join(path, name+'.'+ftype)
    with open(final_path, 'w') as fp:
        pass
    mb.showinfo('confirmation', 'File created!')

def open_window():
    read = easygui.fileopenbox()
    return read

def open_file():
    mb.showinfo('confirmation', 'Select file to open')
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', 'File not found!')

def copy_file():
    mb.showinfo('confirmation', 'Choose file to copy')
    source = open_window()
    mb.showinfo('confirmation', 'Choose folder for copied file')
    destination = filedialog.askdirectory()
    shutil.copy(source, destination)
    mb.showinfo('confirmation', 'File copied!')

def delete_file():
    mb.showinfo('confirmation', 'Choose file to permanently delete')
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
        mb.showinfo('confirmation', 'File deleted! ')
    else:
        mb.showinfo('confirmation', 'File not found!')

def send_file_to_trash():
    mb.showinfo('Choose file to send to trash')
    send = open_window()
    if os.path.exists(send):
        send2trash(send)
        mb.showinfo('confirmation', 'File sent to trash!')
    else:
        mb.showinfo('confirmation', 'File not found!')

def rename_file():
    mb.showinfo('confirmation', 'Choose file to rename')
    chosen_file = open_window()
    old_path = os.path.dirname(chosen_file)
    extension = os.path.splitext(chosen_file)[1]
    print('Enter new file name')
    newname = input()
    path = os.path.join(old_path, newname+extension)
    os.rename(chosen_file, path)
    mb.showinfo('confirmation', 'File renamed!')

def move_file():
    mb.showinfo('confirmation', 'Choose file to move')
    source = open_window()
    mb.showinfo('confirmation', 'Choose new destination')
    destination = filedialog.askdirectory()
    if source == destination:
        mb.showinfo('confirmation', 'Source and destination are the same')
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', 'File moved!')

def file_size():
    mb.showinfo('confirmation', 'Select file to get size')
    file = open_window()
    print(os.path.getsize(file))

def file_path():
    mb.showinfo('confirmation', 'Slect File to get path')
    file = open_window()
    print(str(file))

def list_file_with_specific_path():
    mb.showinfo('confirmation', 'Select Folder')
    p = filedialog.askdirectory()
    print('Enter file type')
    ftype = input()
    for folderName, subfolders, filenames in os.walk(p):
        print('Current folder: ' + folderName)

        for subfolder in subfolders:
            print('Subfolder of ' + folderName + ': ' + subfolder)

        for filename in filenames:
            if filename.endswith(ftype):
                print('File inside ' + folderName + ': ' + filename)

        print('')

def new_folder():
    mb.showinfo('confirmation', 'Choose destination for new folder')
    location = filedialog.askdirectory()
    print('Enter name for the folder')
    name = input()
    path = os.path.join(location, name)
    os.mkdir(path)
    mb.showinfo('confirmation', 'New folder made!')

def delete_folder():
    mb.showinfo('confirmation', 'Choose folder to permanently delete')
    delFolder = filedialog.askdirectory()
    shutil.rmtree(delFolder)
    mb.showinfo('confirmation', 'Folder Deleted!')

def send_folder_to_trash():
    mb.showinfo('confirmation', 'Choose folder to send to trash')
    trashFolder = filedialog.askdirectory()
    for folderName, subfolders, filenames in os.walk(trashFolder):
        send2trash(folderName)

        for subfolder in subfolders:
            pass
        
        for filename in filenames:
            pass

def rename_folder():
    mb.showinfo('confirmation', 'Choose folder to rename')
    refolder = filedialog.askdirectory()
    location = os.path.dirname(refolder)
    print('Enter new name for folder')
    nname = input()
    path = os.path.join(location, nname)
    os.rename(refolder, path)
    mb.showinfo('confirmation', 'Folder Renamed!')

def list_files():
    mb.showinfo('confirmation', 'Choose Folder')
    folder_list = filedialog.askdirectory()
    for folderName, subfolders, filenames in os.walk(folder_list):
        print('Current folder: ' + folderName)

        for subfolder in subfolders:
            print('Subfolder of ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('File inside ' + folderName + ': ' + filename)

        print('')

def move_folder():
    mb.showinfo('confirmation', 'Choose folder to move')
    folder = filedialog.askdirectory()
    mb.showinfo('confirmation', 'Choose new location for folder')
    nlocation = filedialog.askdirectory()
    if folder == nlocation:
        mb.showinfo('confirmation', 'The Folder and Location are same!')
    else:
        shutil.move(folder, nlocation)
        mb.showinfo('confirmation', 'Folder Moved!')

def copy_folder():
    mb.showinfo('confirmation', 'Choose folder to copy')
    source = filedialog.askdirectory()
    mb.showinfo('confirmation', 'Choose destination for copied folder')
    destination = filedialog.askdirectory()
    print('Enter name for copied folder')
    nname = input()
    fdestinataion = os.path.join(destination, nname)
    shutil.copytree(source, fdestinataion)
    mb.showinfo('confirmation', 'Folder Copied!')

def folder_size():
    mb.showinfo('conrimation', 'Choose Folder')
    folder = filedialog.askdirectory()
    totalsize = 0
    for filename in os.listdir(folder):
        totalsize = totalsize + os.path.getsize(os.path.join(folder, filename))
    print(totalsize)

def files_in_zip():
    mb.showinfo('confirmation', 'Choose zip file')
    my_zipfile = easygui.fileopenbox(filetypes='*.zip')
    zip_atr = zipfile.ZipFile(my_zipfile)
    print(zip_atr.namelist())
    zip_atr.close()

def extract_zip():
    mb.showinfo('confirmation', 'Choose zip file')
    my_zipfile = easygui.fileopenbox(filetypes='*.zip')
    mb.showinfo('confirmation', 'Choose location to extract zip')
    destination = filedialog.askdirectory()
    zip_atr = zipfile.ZipFile(my_zipfile)
    zip_atr.extractall(path=destination)
    zip_atr.close()
    mb.showinfo('confirmation', 'ZipFile extracted!')

def create_zip():
    mb.showinfo('confirmation', 'Select location of new zip')
    destination = filedialog.askdirectory()
    print('Enter name for zip file')
    zname = input()
    my_zipfile = os.path.join(destination, zname+'.zip')
    zip_atr = zipfile.ZipFile(my_zipfile, 'a')
    zip_atr.close()
    mb.showinfo('confirmation', 'ZipFile Made!')

def add_file_zip():
    mb.showinfo('confirmation', 'Choose file to add')
    nfile = easygui.fileopenbox()
    mb.showinfo('confirmation', 'Choose Zip')
    zfile = easygui.fileopenbox(filetypes='*.zip')
    zip_atr = zipfile.ZipFile(zfile, 'a')
    zip_atr.write(nfile, compress_type=zipfile.ZIP_DEFLATED)
    zip_atr.close()
    mb.showinfo('confirmation', 'File added to Zip')

def add_folder_zip():
    mb.showinfo('confirmation', 'Choose folder to add')
    fold = filedialog.askdirectory()
    mb.showinfo('confirmation', 'Choose zip')
    zfile = easygui.fileopenbox(filetypes='*.zip')
    zip_atr = zipfile.ZipFile(zfile, 'a')
    zip_atr.write(fold, compress_type=zipfile.ZIP_DEFLATED)
    zip_atr.close()
    mb.showinfo('confirmation', 'Folder added to zip')

tk = Tk()
tk.geometry('470x295')
tk.title(' ')
tk.resizable(0, 0)
tk.update()
Label(tk, text='Filesh Exploresh', font=('Helvetica', 16), fg='blue').grid(row=5, column=2)

Button(tk, text='New File', command=new_file).grid(row=15, column=2)
Button(tk, text='Open File', command=open_file).grid(row=25, column=2)
Button(tk, text='Get File Path', command=file_path).grid(row=35, column=2)
Button(tk, text='Rename File', command=rename_file).grid(row=45, column=2)
Button(tk, text='Delete File', command=delete_file).grid(row=55, column=2)
Button(tk, text='Send File To Trash', command=send_file_to_trash).grid(row=65, column=2)
Button(tk, text='Move File', command=move_file).grid(row=75, column=2)
Button(tk, text='Copy File', command=copy_file).grid(row=85, column=2)
Button(tk, text='Get File Size', command=file_size).grid(row=95, column=2)

Button(tk, text='List All Files With Particular Format In Directory', command=list_file_with_specific_path).place(x = 20, y=265, anchor=NW)

Button(tk, text='New Folder', command=new_folder).grid(row=15, column=4)
Button(tk, text='List All Files And Paths in  ', command=list_files).grid(row=25, column=4)
Button(tk, text='directory tree(same as above)', command=list_files).grid(row=35, column=4)
Button(tk, text='Rename Folder', command=rename_folder).grid(row=45, column=4)
Button(tk, text='Delete Folder', command=delete_folder).grid(row=55, column=4)
Button(tk, text='Move Folder', command=move_folder).grid(row=65, column=4)
Button(tk, text='Copy Folder', command=copy_folder).grid(row=75, column=4)
Button(tk, text='Get Folder Size', command=folder_size).grid(row=85, column=4)

Button(tk, text='List files in Zip', command=files_in_zip).grid(row=15, column=6)
Button(tk, text='Extract zip file', command=extract_zip).grid(row=25, column=6)
Button(tk, text='Create new Zip', command=create_zip).grid(row=35, column=6)
Button(tk, text='Add file to zip', command=add_file_zip).grid(row=45, column=6)
Button(tk, text='Add folder to zip', command=add_folder_zip).grid(row=55, column=6)

tk.mainloop()
