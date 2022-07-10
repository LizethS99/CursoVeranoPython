#Sánchez Sandoval Yeraldi Lizeth 
print("\t----- HOLA Y BIENVENIDO -----\n")
listaAsig = []
while True:
    opc = input("Desea agregar una asignatura a su lista? s/n: ")
    if opc == "n":
        print("\nGracias por tu visita c:")
        break
    else:
        asignaturas = input("Ingrese la asignatura que quiera agregar a su lista: ")
        listaAsig.append(asignaturas)
        print(listaAsig)