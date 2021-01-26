import abc


class Pessoa(abc.ABC):
    def __init__(self, nome):
        self.__nome = nome

    def __del__(self):
        pass

    def get_nome(self):
        return self.__nome

    @abc.abstractmethod
    def definir_id(self, identificacao):
        pass
