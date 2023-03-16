class anemia:
    def __init__(self,ed,hemo):
        self.__edad=ed
        self.__hemoglobina=hemo
    """ def __init__(self,ed1,hemo1,genero):
        self.__edad=ed1
        self.__hemoglobina=hemo1
        self.__sexo=genero
 """
    def anemiaB(self):
        if self.__edad==0 or self.__edad==1 and self.__hemoglobina>=13 and self.__hemoglobina<=26:
            print("Negativo para anemia")         
        elif self.__edad>1 and self.__edad<=6 and self.__hemoglobina>=10 and self.__hemoglobina<=18:
            print("Negativo para anemia")
        elif self.__edad>6 and self.__edad<=12 and self.__hemoglobina>=11 and self.__hemoglobina<=15:
            print("Negativo para anemia")
        else:
            print("Positivo para anemia")
        """ else:
            if self.__edad>=1 and self.__edad<=5 and self.__hemoglobina>=11 and self.__hemoglobina<=15:
                print("Negativo para anemia")         
            elif self.__edad>5 and self.__edad<=10 and self.__hemoglobina>=11.5 and self.__hemoglobina<=15:
                print("Negativo para anemia")
            elif self.__edad>10 and self.__edad<=15 and self.__hemoglobina>=13 and self.__hemoglobina<=15.5:
                print("Negativo para anemia")
            elif self.__edad>15 and self.__sexo==1 and self.__hemoglobina>=12 and self.__hemoglobina<=16:
                print("Negativo para anemia")
            elif self.__edad>15 and self.__sexo==2 and self.__hemoglobina>=14 and self.__hemoglobina<=18:
                print("Negativo para anemia")
            else:
                print("Positivo para anemia")
 """    
    def anemiaN(self):
        if self.__edad>=1 and self.__edad<=5 and self.__hemoglobina>=11 and self.__hemoglobina<=15:
            print("Negativo para anemia")         
        elif self.__edad>5 and self.__edad<=10 and self.__hemoglobina>=11.5 and self.__hemoglobina<=15:
            print("Negativo para anemia")
        elif self.__edad>10 and self.__edad<=15 and self.__hemoglobina>=13 and self.__hemoglobina<=15.5:
            print("Negativo para anemia")
        else:
            print("Positivo para anemia")        

class anemia1:
    def __init__(self,ed1,hemo1,genero):
        self.__edad1=ed1
        self.__hemoglobina1=hemo1
        self.__sexo=genero

    def anemiaA(self):
        if self.__edad1>=1 and self.__edad1<=5 and self.__hemoglobina1>=11 and self.__hemoglobina1<=15:
            print("Negativo para anemia")         
        elif self.__edad1>5 and self.__edad1<=10 and self.__hemoglobina1>=11.5 and self.__hemoglobina1<=15:
            print("Negativo para anemia")
        elif self.__edad1>10 and self.__edad1<=15 and self.__hemoglobina1>=13 and self.__hemoglobina1<=15.5:
            print("Negativo para anemia")
        elif self.__edad1>15 and self.__sexo==1 and self.__hemoglobina1>=12 and self.__hemoglobina1<=16:
            print("Negativo para anemia")
        elif self.__edad1>15 and self.__sexo==2 and self.__hemoglobina1>=14 and self.__hemoglobina1<=18:
            print("Negativo para anemia")
        else:
            print("Positivo para anemia")
