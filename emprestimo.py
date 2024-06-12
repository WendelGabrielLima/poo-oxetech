class Emprestimo:
    def __init__(self, livro, membro, data_emprestimo, data_devolucao, estado):
        self.__livro = livro
        self.__membro = membro
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
        self.__estado = estado

    def livro(self):
        return self.__livro
    
    def membro(self):
        return self.__membro

    def data_emprestimo(self):
        return self.__data_emprestimo
    
    def data_evolucao(self):
        return self.__data_devolucao

# acho que será preciso inserir um set para data de emprestimo e devolução...
# mas não tenho certeza porém não tenho cabeça para pensar mais kkkk
# qualquer coisa fale comigo no wpp, se precisar de ajuda