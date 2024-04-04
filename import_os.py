import os

#file descriptor = fd
#r permite leer
fd = open("/home/alumne/Escriptori/app.py","r")

#w permite escribir pero al abrirlo no hay contenido dentro
fd = open("/home/alumne/Escriptori/app.py","w")

#a permite hacer append y te mantiene las cosas que hay dentro
fd = open("/home/alumne/Escriptori/app.py","a")

#r+ permite leer + escribir
fd = open("/home/alumne/Escriptori/app.py","r+")

os.listdir()

#read te leera el archivo
fd.read()

#tell te dice donde esta el cursor
fd.tell()

#seek 0,0 te esta diciendo que va a mover de 1 en 1 desde el inicio
fd.seek(0,0)

#seek 0,1 te esta diciendo que va a mover de 1 en 1 desde donde esta
fd.seek(0,1)

#seek 0,2 te esta diciendo que va a mover de 1 en 1 desde el final
fd.seek(0,2)

print(fd)
