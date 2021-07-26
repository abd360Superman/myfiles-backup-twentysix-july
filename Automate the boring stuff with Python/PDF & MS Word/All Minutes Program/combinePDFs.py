#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF. Randomly rotate pages and encrypt it

import PyPDF2, os, random

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pageObj.rotateClockwise(random.choice([90, 180, 270]))
        pdfWriter.addPage(pageObj)

pdfWriter.encrypt('minutes')
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
