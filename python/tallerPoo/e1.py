class objetivo:
    def __init__(self,p1,p2,obje):
        self.___posicion1=p1
        self.__posicion2=p2
        self.__objetivo=obje
    
    def Suma(self):
        if self.___posicion1+self.__posicion2==self.__objetivo:
            return True
         