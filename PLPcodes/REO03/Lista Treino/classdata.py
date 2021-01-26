from datetime import date


class Date:
    __slots__ = ('_Date__Day', '_Date__Month', '_Date__Year')

    def __init__(self, day, month, year):
        if day <= 30 and day > 0:
            self.__Day = day
        if month > 0 and day <= 12:
            self.__Month = month
        self.__Year = year

    def __init__(self):
        self.__Day = date.today().day
        self.__Month = date.today().month
        self.__Year = date.today().year

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


d1 = Date()
d2 = Date('12', '11', '2021')

print(f'{d1.Day}\n{d1.Month}\n{d1.Year}')
print(f'{d2.Day}\n{d2.Month}\n{d2.Year}')
