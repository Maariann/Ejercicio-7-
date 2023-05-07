class ViajeroFrecuente:
    
    
    def __init__(self, num, dni, nom, apell, illas):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apell
        self.__millas = millas

  
    def __gt__(self, otro):
        return self.__millas > otro._millas

    def __add__(self millas):
        return ViajeroFrecuente(self.__numero, self.__dni, self.__nombre, self.__apellido, self.__millas + millas)

    def __sub__(self,millas):
        return ViajeroFrecuente(self.__numero, self.__dni, self.__nombre, self.__apellido, self.__millas - millas)

    def __eq__(self, otro):
        return self.__millas == otro

    def __radd__(self, millas):
        return self.__add__(millas)

    def __rsub__(self, millas):
    return self._sub__(millas)
