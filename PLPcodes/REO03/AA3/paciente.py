from pessoa import Pessoa
from prontuario import Prontuario

class Paciente:
    __numeroPacientes = 0
    
    def __init__(self, nome):
        Pessoa.__init__(self, nome)
        Paciente.__numeroPacientes += 1

    def __del__(self):
        Paciente.__numeroPacientes -= 1
    
    def definir_id(self, identificacao):
        if(len(identificacao) > 5):
            print('Erro: O ID possui mais de 5 caracteres. Revise e tente novamente')
        else:
            self.__id = identificacao
    
    def definir_prontuario(self, prontuario):
        self.prontuario = prontuario
    
    @classmethod
    def pacientes_ativos(cls):
        return cls.__numeroPacientes