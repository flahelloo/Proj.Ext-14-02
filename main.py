#1
listaFeira = [12, "Banana", 7.8]

#2
listaFeira.insert(3, False)

#3
listaFeira[1]= "laranja"
#print(*listaFeira)

#4
listaFeira.remove(12)
#print(*listaFeira)
listaFeira.append(12)
#print(*listaFeira)

#5
#print(listaFeira[2], listaFeira [0], listaFeira[3], listaFeira[1])

#6
listaFeira.append("maça")
listaFeira.append(5.30)
listaFeira.append(9)
listaFeira.append("morango")
#print(*listaFeira, "\n")

#7
listaFeira2 = listaFeira
#print(*listaFeira)
#print(*listaFeira2, "\n")
listaFeira.remove("morango")
print(*listaFeira2, "\n")

#8 e 9
listaFeira3 = listaFeira.copy()
listaFeira3.remove(9)
listaFeira3.insert(2, "kiwi")
listaFeira3.insert(3, 2.50)
listaFeira3.insert(5, "jabuticaba")
#print(*listaFeira3)

#10
listaFeira4 = []
listaFeira4.append(listaFeira3[0:4])
#print(*listaFeira4)
listaFeira5 = []
listaFeira5.append(listaFeira3[4:8])
print(*listaFeira5)

#11
listaFeira6 = []
listaFeira6.insert(0, *listaFeira5)
listaFeira6.insert(1, *listaFeira4)
print(*listaFeira6 , "\n")

#12
print(*listaFeira2[4:8])

#13
print(*listaFeira2[::-1])

#14
for item in listaFeira2:
    if item == "banana":
        print("VERDADEIRO")
    else:
        print("FALSO")
        break

#15
listaFeira7 = []
for i in range(11):
    x = i * i
    listaFeira7.append(x)
print(listaFeira7, "\n")


#EXTRA
numeros = [5, 62, 8, 54, 100, 96, 200, 97, 36, 1]
numerosOrdenados = sorted(numeros)

print(numerosOrdenados)