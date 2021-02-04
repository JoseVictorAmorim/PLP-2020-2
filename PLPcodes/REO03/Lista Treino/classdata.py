from datetime import date


class Date:
    __slots__ = ('_Date__Day', '_Date__Month', '_Date__Year')

    def __init__(self, day = date.today().day, month = date.today().month, year = date.today().year):
        if int(day) <= 30 and int(day) > 0:
            self.__Day = day
        else:
            print('Dia não aceito')
        if int(month) > 0 and int(month) <= 12:
            self.__Month = month
        else:
            print('Mes não aceito')
        self.__Year = int(year)

    @property
    def Day(self):
        return f'DIA: {self.__Day}'

    @Day.setter
    def Day(self, newDay):
        self.__Day = newDay

    @property
    def Month(self):
        return f'MES: {self.__Month}'

    @Month.setter
    def Month(self, newMonth):
        self.__Month = newMonth

    @property
    def Year(self):
        return f'ANO: {self.__Year}'

    @Year.setter
    def Year(self, newYear):
        self.__Year = newYear

    def __str__(self):
        print(f'{self.__Day}/{self.__Month}/{self.__Year}')
    
    def printDate(self):
        self.__str__()


d = int(input("Digite o dia: "))
m = int(input("Digite o mês: "))
y = int(input("Digite o dia: "))

d2 = Date(d, m, y)
print(f'{d2.Day}\n{d2.Month}\n{d2.Year}')

d1 = Date()
print(f'{d1.Day}\n{d1.Month}\n{d1.Year}')
d1.Day = 15
d1.Month = 12
d1.Year = 2020
d1.printDate()
print(f'{d1.Day}\n{d1.Month}\n{d1.Year}')
