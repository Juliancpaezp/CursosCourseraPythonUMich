# 6.5 Write code using find() and string slicing
# (see section 6.10) to extract the number at
# the end of the line below. Convert the extracted
# value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

# 1. Se busca la posicion de los ":"
PosicionDeDosPuntos = text.find(":")

# 2. Se guarda todo lo que este despues
# (Como es "despues de" y no "a partir de" entonces
# se agraga +1 al index)
slice = text[PosicionDeDosPuntos+1:]

# 3. se le quitan los espacios que le sobren
#slice = slice.split()

# 4. Se convierte en variable tipo float
slice = float(slice)

# 5. Se imprime y fin
print(slice)
