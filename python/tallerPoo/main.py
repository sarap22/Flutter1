menu=1
while menu>0 and menu<7:
    menu=int(input("Menu de opciones:\n1.Numero objetivo.\n2.Colegiatura\n3.Casa interes social\n4.SAR\n5.Hipoteca.\n6.Anemia.\n7.Salir."))
    if menu==1:
        import e1
        cantidad=int(input("Cuántas números va a sumar?"))
        matriz=[]
        salida=[]
        for i in range(cantidad):
            if i==0:
                num=int(input("Ingrese un número"))
            else:
                num=int(input("Ingrese otro número"))
            matriz.append(num)
        objetivo=int(input("Ingrese el numero objetivo"))
        i=0
        j=1
        while j<len(matriz):
    #print(matriz[i],matriz[j],objetivo)
            objeto=e1.objetivo(matriz[i],matriz[j],objetivo)
            if objeto.Suma()==True:
                salida.append(i)
                salida.append(j)
            i+=1
            j+=1
        print(salida)    
    
    elif menu==2:
        import e2
        promedio=int(input("Digite la Nota de su Promedio Académico en el ultimo periodo"))
        cantidad=int(input("Cuántas materias va a cursar?"))
        costo=int(input("Ingrese el costo de las materias"))
        datos2=e2.precio(promedio,cantidad,costo)
        datos2.precio()

    elif menu==3:
        import e3
        ing=int(input("De cuanto son sus ingresos?"))
        costoC=int(input("De cuanto es el costo de la casa?"))
        objeto=e3.costo(ing,costoC)
        objeto.pago()

    elif menu==4:   
        import e4
        metodo=int(input("De que manera desea que la empresa deposite parte de su salario en la cuenta SAR:\n1.Cuota fija.\n2.Porcentaje de salario"))
        if metodo>0 and metodo<3:
            salario=int(input("Cual es el monto de su salario?")) 
            objeto=e4.metodoP(metodo,salario)
            objeto.cuota()
        else:
            print("Opcion no valida")    

    elif menu==5:
        import e5
        hipoteca=int(input("Cuanta plata es de hipoteca?"))        
        inverT=int(input("De cuanta plata es la inversion total?"))
        objeto=e5.inversion(hipoteca,inverT)
        objeto.monto()
    
    elif menu==6:
        import e6
        edad=int(input("Ingrese su edad"))
        nivelH=float(input("Ingrese el nivel de hemoglobina en su sangre"))
        objeto=e6.anemia(edad,nivelH)
        if edad==0:
            objeto.anemiaB()
        elif edad<13:
            moA=int(input(str(edad)+"\n1.meses?\n2.años?"))
            if moA==1:
                objeto.anemiaB()
            else:
                objeto.anemiaN()
        else:
            sexo=int(input("Seleccione su genero\n1.Femenino.\n2.Masculino"))
            objeto=e6.anemia1(edad,nivelH,sexo)
            objeto.anemiaA()
              