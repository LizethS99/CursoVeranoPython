#Sánchez Sandoval Yeraldi Lizeth
print("\n\t----- HOLA Y BIENVENIDO -----\n")
verduras = {"Brocoli": 8.55, "Pepino": 6.87, "Calabaza": 11.55, "Chayote": 14.33}
totalcompra = 0
while True:
    opc = input("Desea comprar? s/n: ")
    if opc == "s":
        print("\nContamos con las siguientes verduras:\nBrocoli $8.55\nPepino $6.87\nCalabaza $11.55\nChayote $14.33")
        OpcVerdura = input("\nQué verdura desea? (Escriba el nombre)_ ").lower().capitalize()
        if OpcVerdura in verduras:
            opcKilos = int(input("\nCuántos kilos desea?: "))
            compra = verduras[OpcVerdura] * opcKilos
            totalcompra = totalcompra + compra
            print(f"\nUsted ha escogido {OpcVerdura} con un precio de ${verduras[OpcVerdura]} por kilo, su compra es de ${compra:.2f}")
        else:
            print("\nLo sentimos no contamos con esa verdura")
    else:
        print(f"\n-----TOTAL DE SU COMPRA: ${totalcompra}")
        print("\nGracias por su visita c:")
        break