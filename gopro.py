import requests
import re
import wget
import time

goproHTTPRoot = "http://10.5.5.9/videos/DCIM/"

def takeshot():
    r = requests.get("http://10.5.5.9/gp/gpControl/command/shutter?p=1")
    return r.status_code
    
def getFoldersList():
    r = requests.get(goproHTTPRoot)
    folderList = re.findall(r'href=".*/"', r.text)
    
    folderListResult = []
    
    for i in range(len(folderList)):
        folderName = folderList[i].replace("href=\"", "").replace("\"", "")
        folderListResult.append(folderName)
    
    return folderListResult
        
    
def getPhotosNameList(folder):
    r = requests.get(goproHTTPRoot + folder)
    photoNameList = re.findall(r'href=".*.JPG"', r.text)
    
    photoNameListResult = []
    
    for i in range(len(photoNameList)):
        photoName = photoNameList[i].replace("href=\"", "").replace("\"", "")
        photoNameListResult.append(folder + photoName)
        
    return photoNameListResult
    
def getAllPhotoPaths():
    folders = getFoldersList()
    
    result = []
    
    for i in range(len(folders)):
        photosNames = getPhotosNameList(folders[i])
        for j in range(len(photosNames)):
            result.append(photosNames[j])
    
    return result
    
def getLastPhotoPath():
    allPhotosPathsList = sorted(getAllPhotoPaths())
    print allPhotosPathsList
    return allPhotosPathsList[-1]
    
def downloadPhoto(url):
    filename = wget.download(url)
    return filename
    
def takePhotoAndDownload():
    status = takeshot()
    time.sleep(5)
    lastPhoto =  getLastPhotoPath()
    return downloadPhoto(goproHTTPRoot + lastPhoto)
    


if __name__ == '__main__':
    takenPhotoName = takePhotoAndDownload()
    print takenPhotoName
