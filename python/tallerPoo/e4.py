class metodoP:
    def __init__(self,opc, montos):
        self.__opcion=opc
        self.__montoS=montos
    
    def cuota(self):
        if self.__opcion==1:
            cuota=int(input("De cuanto es la cuota fija que desea depositar en su cuenta SAR cada mes?"))
            des=self.__montoS-cuota
            print("Cada mes, usted estara depositando $",int(cuota),"en su cuenta SAR.Por lo tanto, su pago mensual sera de $",int(des),".")
        else:
            cuota=int(input("De cuanto es el porcentaje de salario que desea depositar en su cuenta SAR cada mes?"))
            des=self.__montoS-((self.__montoS*cuota)/100)
            print("Cada mes, usted estara depositando $",int((self.__montoS*cuota)/100),"en su cuenta SAR.Por lo tanto, su pago mensual sera de $",int(des),".")    

