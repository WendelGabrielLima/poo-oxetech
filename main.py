from livro import Livro
from membro import Membro
from emprestimo import Emprestimo

class LivrosDisponiveis:
    def __init__(self):
        self.livrosDisponiveis = []

    def adicionarLivroDisponivel(self, livro):
        self.livrosDisponiveis.append(livro)

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
    print("7 -> DEVOLVER LIVRO")
    print("8 -> SAIR")
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

        
        

