import os, zipfile
from pathlib import Path
p = Path('C:/Darsh Files/Automate the boring stuff with Python/ZipFile Module')
exampleZip = zipfile.ZipFile(p / 'test-zip-file.zip')
print(exampleZip.namelist())
pdfFile = exampleZip.getinfo('www.case-study-project.com/Images.pdf')
print(pdfFile.file_size)
print(pdfFile.compress_size)
print(f'Compressed File is {round(pdfFile.file_size / pdfFile.compress_size, 2)}x smaller!')
exampleZip.close()
