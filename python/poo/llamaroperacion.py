class operacion:
    def __init__(self, num1, num2):#un solo constructor
        #self(python) = this(java)
        self.__n1=num1
        self.__n2=num2
    
    def getSuma(self):
        return self.__n1+self.__n2
    
    def getResta(self):
        return self.__n1-self.__n2
    
    def getMulti(self):
        return self.__n1*self.__n2
        
    def getDiv(self):
        return self.__n1/self.__n2
