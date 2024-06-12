class Livro:

    _index = 0

    def __init__(self, titulo, autor, status = 'disponível'):
        Livro._index += 1
        self.__titulo = titulo
        self.__autor = autor
        self.__status = status
        self.__id = Livro._index

    def __str__(self):
        return f"{self.__id} | Título: {self.__titulo} | Autor: {self.__autor} | Status: {self.__status} |"

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        if status == 'disponível':
            self.__status = 'disponível'
            return status
        else:
            self.__status = 'indisponível'
            return status     




    






    
