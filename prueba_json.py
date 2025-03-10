import json

contactos = open("contactos.json","r")
datos = json.load(contactos)
contactos.close()

print(datos)



