class inversion:
    def __init__(self,hipo,inver):
        self.__hipotecaT=hipo
        self.__inversionT=inver
    
    def monto(self):
        if self.__hipotecaT<100000000:
            print("Usted debe invertir el 50% de la inversion total y su socio tambien, es decir, cada uno tiene que invertir $",int(self.__inversionT/2))
        else:
            if self.__inversionT>self.__hipotecaT:
                print("Usted invertirá el monto total de la hipoteca y los restantes $",int(self.__inversionT-self.__hipotecaT)," los pagara en partes iguales de $",int((self.__inversionT-self.__hipotecaT)/2),"junto con su socio")           
            else:
                print("Usted invertirá el monto total de la hipoteca y el resto del dinero que se necesite para cubrir la inversión total se repartirá en partes iguales su socio y usted.")
