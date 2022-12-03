from heap import *

print("Teste das funções de Heap \n\n")

heap = [20, 35, 18, 64, 70, 7, 12, 43, 25, 50]
print("Vetor V inicial: ", heap)
constroi_heap(heap)
print("Heap formado pelo vetor V: ", heap, "\n")

inserir(heap, 10)
print("Chave 10 inserida: ", heap)
inserir(heap, 99)
print("Chave 99 inserida: ", heap)
inserir(heap, 5)
print("Chave 5 inserida: ", heap, "\n")

heapsort(heap)
print("Vetor após o Heapsort: ", heap)

constroi_heap(heap)
print("Heap formado pelo vetor", heap, "\n")

print("         ", heap)
remover(heap)
print("Remoção: ", heap)
remover(heap)
print("Remoção: ", heap)
remover(heap)
print("Remoção: ", heap, "\n")

inserir(heap, 13)
print("Chave 13 inserida: ", heap, "\n")

heapsort(heap)
print("Vetor após o Heapsort: ", heap)

input()
