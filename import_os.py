import os

#file director = fd
#r permite leer
fd = open("/home/alumne/Escriptori/app.py","r")

#w permite escribir
fd = open("/home/alumne/Escriptori/app.py","w")

#a permite hacer append
fd = open("/home/alumne/Escriptori/app.py","a")

#r+w permite leer + escribir
fd = open("/home/alumne/Escriptori/app.py","r+w")

os.listdir()

print(fd)
