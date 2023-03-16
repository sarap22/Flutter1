class cliente:
    def __init__(self, nom, ed, cor):#un solo constructor
        #self(python) = this(java)
        self.__nombre=nom
        self.__edad=ed
        self.__correo=cor
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getCorreo(self):
        return self.__correo
    
    
        