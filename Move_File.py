import os
import shutil
from_dir = 'C:\\Users\\shyam\\Downloads'
to_dir = 'C:\\Users\\shyam\\Downloads\\Document_files'
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == '':
        continue    
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir +  '/' + file_name
        path2 = to_dir + '/' + 'document_files'
        path3 = to_dir + '/' + 'document_files' + '/' + file_name
       # print(path1)
        #print(path3)
#check if folder or directory path exists before moving
    if os.path.exists(path2):
        print("Moving" + file_name)
        shutil.move(path1, path3)
#else make a new folder or directory then move
    else: 
        os.makedirs(path2)
        print("moving" + file_name)
        shutil.move(path1, path3)