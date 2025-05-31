class m_calc:
    __num1 = 0
    __num2 = 0
    __result = 0

    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def setnum(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def plus(self):
        self.__result = self.__num1 + self.__num2
        self.__plus_view()

    def minus(self):
        self.__result = self.__num1 - self.__num2
        self.__minus_view()
    
    def mul(self):
        self.__result = self.__num1 * self.__num2
        self.__mul_view()
    
    def div(self):
        self.__result = self.__num1 / self.__num2
        self.__div_view()

    def __plus_view(self):
        print(self.__num1, " + ", self.__num2, " = ", self.__result)

    def __minus_view(self):
        print(self.__num1, " - ", self.__num2, " = ", self.__result)
    
    def __mul_view(self):
        print(self.__num1, " * ", self.__num2, " = ", self.__result)
    
    def __div_view(self):
        print(self.__num1, " / ", self.__num2, " = ", self.__result)

