import os.path
import shutil
import time

HOME_PATH = '/home/matheus/'

FILE_ORIGIN = HOME_PATH + 'proxy_files/origin/'
FILE_DEST = HOME_PATH + 'proxy_files/dest/'

FILE_NAME = 'file_4'

print('======= bom dia =======')

while not os.path.exists(FILE_ORIGIN + FILE_NAME):
    print('Ainda não existe,')
    time.sleep(1)
if os.path.isfile(FILE_ORIGIN + FILE_NAME):
    print('Arquivo encontrado.')
    print('movendo para: ' + FILE_DEST)
    shutil.move(FILE_ORIGIN + FILE_NAME, FILE_DEST)

else:
    raise ValueError(("%s isn't a file!" % FILE_ORIGIN))

