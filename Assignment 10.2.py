# 10.2 Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From '
# line by finding the time and then splitting the string a
# second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print
# out the counts, sorted by hour as shown below.

import os
os.system('cls')

# nombreDelArchivo = input("Enter file:")
# if len(nombreDelArchivo) < 1:
#     nombreDelArchivo = "mbox-short.txt"
# FileHandle = open(nombreDelArchivo)
FileHandle = open("mbox-short.txt")

histogramaReloj = dict()
histogramaHora = dict()

for linea in FileHandle:
    if linea.startswith("From "):
        lineaSeparada = linea.split()
        histogramaReloj[lineaSeparada[5]] = histogramaReloj.get(lineaSeparada[5],0)+1

for Reloj in histogramaReloj:
    RelojSeparado = Reloj.split(":")
    histogramaHora[RelojSeparado[0]] = histogramaHora.get(RelojSeparado[0],0)+1

for hora,cantidad in sorted(histogramaHora.items()):
    print(hora,cantidad)

#Distribucion gaussiana de emails
