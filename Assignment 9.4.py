# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes
# the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that
# maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

nombreDelArchivo = input("Enter file:")
if len(nombreDelArchivo) < 1:
    nombreDelArchivo = "mbox-short.txt"
FileHandle = open(nombreDelArchivo)

mayorPalabra = None
mayorCantidad = None
histograma = dict()

for linea in FileHandle:
    if linea.startswith("From:"):
        lineaSeparada = linea.split()
        histograma[lineaSeparada[1]] = histograma.get(lineaSeparada[1],0)+1

for palabra,cantidad in histograma.items():
    if mayorCantidad is None or cantidad > mayorCantidad:
        mayorPalabra = palabra
        mayorCantidad = cantidad

print(mayorPalabra,mayorCantidad)
