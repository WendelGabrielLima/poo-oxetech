class Membro:

    _index = 0

    def __init__(self, nome, endereco):
        Membro._index += 1
        self.__nome = nome
        self.__id = Membro._index
        self.__endereco = endereco

    def __str__(self):
        return f"{self.__id} | NOME: {self.__nome} | ENDEREÇO: {self.__endereco}"

    def get_nome(self):
        return self.__nome
    
    def get_id(self):
        return self.__id
    
    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, endereco):
        self.__endereco = endereco
