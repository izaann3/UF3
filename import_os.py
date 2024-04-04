import os

#file director = fd
#r permite leer
fd = open("/home/alumne/Escriptori/app.py","r")

#w permite escribir pero al abrirlo no hay contenido dentro
fd = open("/home/alumne/Escriptori/app.py","w")

#a permite hacer append y te mantiene las cosas que hay dentro
fd = open("/home/alumne/Escriptori/app.py","a")

#r+ permite leer + escribir
fd = open("/home/alumne/Escriptori/app.py","r+")

os.listdir()

print(fd)
