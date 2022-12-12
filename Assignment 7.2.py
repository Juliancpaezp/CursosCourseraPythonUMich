# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point
# values from each of the lines and compute the average
# of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum
# in your solution.
# You can download the sample data at
# http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt
# as the file name.

# Use the file name mbox-short.txt as the file name
#FileName = input("Enter file name: ")
FileName =  "mbox-short.txt"
FileHandle = open(FileName)

cantidadDeLineas = 0
totalDenumerillo = 0

for line in FileHandle:

    # Si no empieza con "X-DSPAM-Confidence:" continua a la siguiente iteracion de for
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # 1. Se busca la posicion de los ":"
    PosicionDeDosPuntos = line.find(":")

    # 2. Se guarda todo lo que este despues de ":" como numerillo
    # (Como es "despues de" y no "a partir de" entonces
    # se agraga +1 al index)
    numerillo = line[PosicionDeDosPuntos+1:]

    # 3. se le quitan los espacios que le sobren
    numerillo = numerillo.strip()

    # 4. Se convierte en variable tipo float
    numerillo = float(numerillo)

    # 5. Añadir 1 al contador de lineas
    cantidadDeLineas = cantidadDeLineas + 1

    # 6. Añadir valor de numerillo al total
    totalDenumerillo = totalDenumerillo + numerillo

    # 7. Calcular promedio
    pomedioDenumerillo = totalDenumerillo/cantidadDeLineas

print("Average spam confidence:", pomedioDenumerillo)
