
#from desencriptar.py import desencriptar
from datetime import datetime

fichero = 'pruebas/ejemplo.txt'
contador = 0



def escribirLog(mensaje):
    logs = open(r'E:\Universidad\Tercero_1\Compresion_Seguridad\Compresion_Seguridad\logs.txt','a')
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    logs.writelines(date_time + ": " +mensaje+"\n")

