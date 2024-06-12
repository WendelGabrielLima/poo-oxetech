from livro import Livro
from membro import Membro
from emprestimo import Emprestimo
from datetime import datetime, timedelta

class LivrosDisponiveis:
    def __init__(self):
        self.livrosDisponiveis = []

    def adicionarLivroDisponivel(self, livro):
        self.livrosDisponiveis.append(livro)
    
    def emprestarLivro(self, livro, membro):
        if livro in self.livrosDisponiveis:
            data_emprestimo = datetime.now()
            data_devolucao = data_emprestimo + timedelta(days=7)

            emprestimo = Emprestimo(livro, membro, data_emprestimo, data_devolucao, estado="Emprestado")

            self.livrosDisponiveis.remove(livro)  
            emprestados.adicionarLivroEmprestado(emprestimo)  

            print("Livro emprestado com sucesso!")
        else:
            print("Livro não disponível para empréstimo.")

    def __str__(self):
        return f"Livros disponíveis: {self.livrosDisponiveis}"
    
class LivrosEmprestados:
    def __init__(self):
        self.livrosEmprestados = []

    def adicionarLivroEmprestado(self, emprestimoLivro):
        self.livrosEmprestados.append(emprestimoLivro)
    
    def __str__(self):
        return f"Livros Emprestados: {self.livrosEmprestados}"
    
class MembrosListados:
    def __init__(self):
        self.membrosLista = []

    def adicionarMembro(self, novoMembro):
        self.membrosLista.append(novoMembro)

    def __str__(self):
        return f"MEMBROS: {self.membrosLista}"
    
emprestados = LivrosEmprestados()
disponiveis = LivrosDisponiveis()
membrosListados = MembrosListados()

membro1 = Membro("Antonio Nunes", "Rua da Quixaba, 86")
membro2 = Membro("Maria Jose", "Centro, 79")
membro3 = Membro("Jose Maria", "Rua da Goiaba, 106")
membro4 = Membro("Joao Mateus", "Rua C, 10")
membro5 = Membro("Eulina Duarte", "Rua D, 35")

membrosListados.membrosLista.append(membro1)
membrosListados.membrosLista.append(membro2)
membrosListados.membrosLista.append(membro3)
membrosListados.membrosLista.append(membro4)
membrosListados.membrosLista.append(membro5)


livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes")
livro3 = Livro("Crime e Castigo", "Fiódor Dostoiévski")
livro4 = Livro("A Metamorfose", "Franz Kafka")
livro5 = Livro("Orgulho e Preconceito", "Jane Austen")

disponiveis.adicionarLivroDisponivel(livro1)
disponiveis.adicionarLivroDisponivel(livro2)
disponiveis.adicionarLivroDisponivel(livro3)
disponiveis.adicionarLivroDisponivel(livro4)
disponiveis.adicionarLivroDisponivel(livro5)

while True:
    print()
    print("----------------- BIBLIOTECA -----------------")
    print()
    print("1 -> LISTAR LIVROS DISPONÍVEIS")
    print("2 -> LISTAR LIVROS EMPRESTADOS")
    print("3 -> ADICIONAR NOVO LIVRO")
    print("4 -> REMOVER LIVRO")
    print("5 -> REGISTRAR MEMBRO")
    print("6 -> LISTAR MEMBROS")
    print("7 -> EMPRESTAR LIVRO")
    print("8 -> DEVOLVER LIVRO")
    print("9 -> SAIR")
    print()
    print("+ + + + + + + + + + + + + + + + + + + + + + + + ")
    print()
    opcao = int(input("OPÇÃO DESEJADA -> "))
    print()

    if opcao == 1:
        for i, livro in enumerate(disponiveis.livrosDisponiveis):
            print(livro)
    elif opcao == 2:
        if len(emprestados.livrosEmprestados) < 1:
            print("NÃO HÁ LIVROS EMPRESTADOS!")
        else:
            for livro in emprestados.livrosEmprestados:
                print(livro)
    elif opcao == 3:
        titulo = input("DIGITE O TÍTULO DO LIVRO QUE DESEJA ADICIONAR: ")
        autor = input("DIGITE O AUTOR DO LIVRO: ")
        novoLivro = Livro(titulo, autor)
        disponiveis.livrosDisponiveis.append(novoLivro)
        print("LIVRO ADICIONADO COM SUCESSO!")
    elif opcao == 4:
        for i, livro in enumerate(disponiveis.livrosDisponiveis):
            print(livro)
        print()
        excluirLivro = int(input("DIGITE O ÍNDICE DO LIVRO QUE DESEJA REMOVER: "))
        if excluirLivro <= len(disponiveis.livrosDisponiveis):
            excluirLivro = excluirLivro - 1
            del disponiveis.livrosDisponiveis[excluirLivro]
            print("LIVRO REMOVIDO COM SUCESSO!")
        else:
            print("NÃO HÁ LIVRO COM O ÍNDICE INFORMADO, TENTE NOVAMENTE")
    elif opcao == 5:
        name = input("DIGITE O NOME DO NOVO MEMBRO: ")
        endereço = input("DIGITE O ENDEREÇO DO MEMBRO: ")
        newMembro = Membro(name, endereço)
        membrosListados.membrosLista.append(newMembro)
        print("MEMBRO ADICIONADO COM SUCESSO!")
    elif opcao == 6:
        for membro in membrosListados.membrosLista:
            print(membro)
    elif opcao == 7:
        for i, livro in enumerate(disponiveis.livrosDisponiveis):
            print(livro)
        indice = int(input("DIGITE O ÍNDICE DO LIVRO QUE DESEJA EMPRESTAR: "))
        if 0 < indice <= len(disponiveis.livrosDisponiveis):
            livro = disponiveis.livrosDisponiveis[indice - 1]
            for membro in membrosListados.membrosLista:
                print(membro)
            indice_membro = int(input("DIGITE O ÍNDICE DO MEMBRO PARA EMPRESTAR O LIVRO: "))
            if 0 < indice_membro <= len(membrosListados.membrosLista):
                membro = membrosListados.membrosLista[indice_membro - 1]
                disponiveis.emprestarLivro(livro, membro)
            else:
                print("ÍNDICE DE MEMBRO INVÁLIDO!")
        else:
            print("ÍNDICE DE LIVRO INVÁLIDO!")
    elif opcao == 8:
        if len(emprestados.livrosEmprestados) < 1:
            print("NÃO HÁ LIVROS EMPRESTADOS!")
        else:
            for i, emprestimo in enumerate(emprestados.livrosEmprestados):
                livro = emprestimo.livro()
                membro = emprestimo.membro()
                print(f"{i+1} -> {livro} | EMPRESTADO PARA: {membro}")

            indice = int(input("DIGITE O ÍNDICE DO LIVRO QUE DESEJA DEVOLVER: "))
            if 0 < indice <= len(emprestados.livrosEmprestados):
                emprestimo = emprestados.livrosEmprestados[indice - 1]
                livro = emprestimo.livro()

                livro.set_status('disponível')
                emprestados.livrosEmprestados.remove(emprestimo)
                disponiveis.adicionarLivroDisponivel(livro)

                print("LIVRO DEVOLVIDO COM SUCESSO!")
            else:
                print("ÍNDICE INVÁLIDO!")
    elif opcao == 9:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

        
        

