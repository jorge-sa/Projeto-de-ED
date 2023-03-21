from modulos.Registro import Registro
from modulos.LinkedList import *

def menu():
    print("".join("="*50))
    print("=   Aplicativo de Contatos com lista encadeada   =")
    print("".join("="*50))
    print("1 -> Ver lista de contataos\n2 -> Pesquisar contato\n3 -> Registrar contato\n4 -> Remover contato\n0 -> Sair\n")

lista = LinkedList()

while True:
    menu()
    e = input()

    if e == "1":
        if lista.size == 0:
            print("Você não possui contatos")
        else:
            lista.printList()
    elif e == "2":
        nome = input("\nNome do contato = ")
        p = lista.find(nome)
        if p >= 0:
            node = lista.get(p)
            node.show()
        else:
            print("\nContato não encontrado\n")
    elif e == "3":
        telefone = input("Telefone do Contato = ")
        email = input("E-Mail do contato = ")
        nome = input("Nome do contato = ")

        if nome != "" and (email != "" or telefone != ""):

            r = Registro(nome,telefone,email)
            n = Node(r)

            lista.add(n)

            print("\nContato adicionado\n")
        else:
            print("\nDeve possuir nome e um meio de contato\n")
    elif e == "4":
        nome = input("\nNome do contato = ")
        p = lista.find(nome)
        if p >= 0:
            node = lista.remover(p)
            print("Contato removido")
        else:
            print("\nContato não encontrado\n")
    elif e == "0":
        break
    else:
        print(">> ERR: Comando Inválido")