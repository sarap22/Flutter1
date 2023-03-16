class precio:
    def __init__(self,pro, cant, pre):
        self.__promedio=pro
        self.__cantidad=cant
        self.__precio=pre
    
    def precio(self):
        if  self.__promedio>=9:
            multi=self.__cantidad*self.__precio
            des=multi-(multi*0.3)
            print("El precio total de su colegiatura es de $",int(multi),".Pero, ya que su promedio fue mayor de 9, se le hará un descuento del 30% sobre el valor de la colegiatura y no se le cobrará IVA.\nAsí que el precio de su colegiatura es de $",int(des))
        else:
            multi=self.__cantidad*self.__precio
            des=multi+(multi*0.1)   
            print("El precio total de su colegiatura es de $",int(multi),".Pero, ya que su promedio no fue mayor de 9, no se le hará ningún descuento sobre el valor de la colegiatura, se le cobrara la colegiatura completa y se le cobrará el 10% de IVA.\nAsí que el precio de su colegiatura es de $",int(des))

    