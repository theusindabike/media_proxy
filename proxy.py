import os.path
import time

FILE_PATH = '/home/matheus.lopes/media_files/file_2.img'

print('======= bom dia =======')

while not os.path.exists(FILE_PATH):
    print('Ainda não existe')
    time.sleep(0.5)
if os.path.isfile(FILE_PATH):
    print('existeee ****')
else:
    raise ValueError(("%s isn't a file!" % FILE_PATH))
