import traceback
try:
    raise Exception('This is the error message')
except:
    errorFile = open('error.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback information was written to error.txt')
