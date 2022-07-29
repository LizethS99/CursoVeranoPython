#Sánchez Sandoval Yeraldi Lizeth 
print("\t----- HOLA Y BIENVENIDO -----\n")
totalcompra = 0
def iva(total,porcentaje):
    global totalcompra
    if porcentaje=="":
       total_iva = total*(.16)+total 
    else:
        total_iva = total*(int(porcentaje)/100)+total
    totalcompra = totalcompra+total_iva
    return total_iva

        

while True:
    opc = input("\nPara agregar IVA presione S de lo contrario presione N: ").lower()
    if opc=="s":
        entrada1=float(input("\nPor favor, ingrese el total: "))
        entrada2=input("\nPor favor, ingrese el porcentaje: ")
        print(f"\nEl total de su compra es ${iva(entrada1,entrada2)}, se le ha agregado IVA a su compra")
    else:
        print(f"\n-----TOTAL DE SU COMPRA: ${totalcompra}")
        print("\nGracias por visita! :D\n")
        break