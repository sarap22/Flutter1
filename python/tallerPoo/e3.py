class costo:
    def __init__(self,ingreso, costo):
        self.__ingresos=ingreso
        self.__costoC=costo

    def pago(self):
        if self.__ingresos<=8000:
            enganche=self.__costoC*0.15
            pagosM=(self.__costoC-enganche)/120
            print("Ya que sus ingresos son de $",int(self.__ingresos),",la cuota inicial a pagar de la casa (enganche) es de $",int(enganche),";y los restantes $",int(self.__costoC-enganche),",los tendra que pagar en cuotas mensuales de $",int(pagosM),",durante 10 años.")
        else:
            enganche=self.__costoC*0.30
            pagosM=(self.__costoC-enganche)/83.944228834268
            print("Ya que sus ingresos son de $",int(self.__ingresos),",la cuota inicial a pagar de la casa (enganche) es de $",int(enganche),";y los restantes $",int(self.__costoC-enganche),",los tendra que pagar en cuotas mensuales de $",int(pagosM),",durante 7 años.")
        
