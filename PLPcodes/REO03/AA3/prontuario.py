from medicamento import Medicamento
from medico import Medico
from datetime import datetime



class Prontuario: 
    #__listaProcedimentos

    def __init__(self):
        self.__listaProcedimentos = []
    
    def insere_procedimento(self, medicamento, posologia, medico, data, hora):
        nomeMedico = medico.nome_medico
        nomeMedicamento = medicamento.get_medicamento
        dataFormatada = datetime.strptime(data, '%d-%m-%Y').date()
        horaFormatada = datetime.strptime(hora + ':00', '%H:%M:%S').time() 
        __procedimento = {'medicamento': nomeMedicamento, 'posologia': posologia, 
        'medico': nomeMedico, 'data': dataFormatada, 'hora': horaFormatada} 
        self.__listaProcedimentos.append(__procedimento)
    
    def exibe_prontuario(self):
        self.saida = ''

        for x in self.__listaProcedimentos:
            self.saida = self.saida + f'{x["medicamento"]} - {x["posologia"]} - {x["medico"]} - {x["data"]} - {x["hora"]}' + '\n'
        return print(self.saida)
