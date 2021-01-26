class Book:
    __slots__ = ('_Book__name', '_Book__author', '_Book__pages')
    def __init__(self):
        self.__name = ''
        self.__author = ''
        self.__pages = ''
    def __del__(self):
        print("Book delete from data bank")

    @property
    def name(self):
        return f'NOME: {(self.__name)}'
    @name.setter
    def name(self, newName):
        self.__name = newName
    @property
    def author(self):
        return f'AUTOR: {self.__author}'    
    @author.setter
    def author(self, newAuthor):
        self.__author = newAuthor
    @property
    def pages(self):
        return f'N DE PAGINAS: {self.__pages}'
    @pages.setter
    def pages(self, newPages):
        self.__pages = newPages
    

b1 = Book()
b1.name = 'Neves'   
b1.author = 'Gamer'
b1.pages = int('122')

print(f'{b1.name}\n{b1.author}\n{b1.pages}')

