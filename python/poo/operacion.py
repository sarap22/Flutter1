import llamaroperacion
n1=int(input("Ingrese el primer numero"))
n2=int(input("Ingrese el segundo numero"))

op=llamaroperacion.operacion(n1,n2)

print("Suma:",op.getSuma())
print("Resta:",op.getResta())
print("Multiplicacion:",op.getMulti())
print("Division:",op.getDiv())
