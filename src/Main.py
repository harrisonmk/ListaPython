from Lista import Lista



lista = Lista()

lista.insereNoComeco(5)
lista.insereNoComeco(3)
lista.insereNoComeco(6)
lista.insereNoComeco(2)
lista.insereNoComeco(4)
lista.insereNoComeco(1)

lista.sort1(lista)

print()
print(lista)
lista.removeComeco()
print(lista)
print()

lista.listar()

print()
print("*********Busca********")
if lista.busca(2)== None:
    print("Elemento não encontrado na Lista")
else:
 print("Valor: ",lista.busca(2).getElemento())

#**********************************************************


lista1 = Lista()

lista1.insereNoFinal(5)
lista1.insereNoFinal(3)
lista1.insereNoFinal(6)
lista1.insereNoFinal(2)
lista1.insereNoFinal(4)
lista1.insereNoFinal(1)



print()

print(lista1)
lista1.removeFinal()
print()



lista1.listar()

print("\nTamanho da lista: ",lista1.tamanho())

print()


print("*********Busca********")
if lista.busca(10)== None:
    print("Elemento não encontrado na Lista")
else:
 print("Valor: ",lista.busca(10).getElemento())


 listaordenada = Lista()

 print(listaordenada)

 listaordenada.insereNoFinal(16)
 listaordenada.insereNoFinal(14)
 listaordenada.insereNoFinal(25)
 listaordenada.insereNoFinal(30)
 listaordenada.insereNoFinal(20)
 listaordenada.insereNoFinal(10)

