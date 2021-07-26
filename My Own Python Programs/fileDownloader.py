import requests, os, pyperclip, easygui

urlToDownload = pyperclip.paste()
res = requests.get(urlToDownload)
res.raise_for_status()
extension = os.path.splitext(urlToDownload)
location = easygui.diropenbox()
print('Enter new name for file being downloaded')
filename = input()
ext = extension[1]
newDownloadedFileName = os.path.join(location, str(filename)+'.'+str(ext))
downloadedFile = open(newDownloadedFileName, 'wb')
for chunk in res.iter_content(100000):
    downloadedFile.write(chunk)
downloadedFile.close()
print('Done')
