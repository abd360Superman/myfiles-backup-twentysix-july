#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory

import os, csv

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
