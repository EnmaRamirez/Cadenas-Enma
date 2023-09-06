#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla 
#el número de euros y el número de céntimos del precio introducido.
Precio=input("Cual es el precio de su producto: ")

print("EUROS: ", Precio[:Precio.find(".")], "céntimos: ", Precio[Precio.find(".")+1:])
