#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
#el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan 
#con un solo carácter.

#Fecha=input("Cual es tu fecha de nacimiento en formato dd/mm/aaaa:\n")

#Dia=Fecha[:2]
#Mes=Fecha[3:5]
#Año=Fecha[6:10]

#print(Dia)
#print(Mes)
#print(Año)
Fecha=input("Cual es tu fecha de nacimiento en formato:\n")

Dia=Fecha[:Fecha.find("/")]

print(Dia)









