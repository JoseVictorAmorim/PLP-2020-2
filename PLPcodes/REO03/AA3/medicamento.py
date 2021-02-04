class Medicamento:
    def __init__(self, nome):
        self.__nomeMedicamento = nome
    
    @property
    def get_medicamento(self):
        return self.__nomeMedicamento