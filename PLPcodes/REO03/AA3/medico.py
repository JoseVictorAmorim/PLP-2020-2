from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)

    def definir_id(self, identificacao):
        if(len(identificacao) > 3):
            print('Erro: O ID possui mais de 3 caracteres. Revise e tente novamente')
        else:
            self.__idMedico = identificacao

    @property
    def nome_medico(self):
        return self.nome
    

