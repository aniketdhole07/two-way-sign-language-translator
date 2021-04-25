import os
import shutil
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if(fullPath.endswith('.webp')):
                allFiles.append(fullPath)
                
    return allFiles

dirname = '/home/aniket/Downloads/giphy.com' #Your Full Path of Projects Folder
dest="/home/aniket/Desktop/Projects/gif_extract/gif_data/"

data=getListOfFiles(dirname)
for i in range(len(data)):
    fname=dest+str(i)+".webp"
    shutil.copyfile(data[i], fname)
