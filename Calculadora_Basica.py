#Sánchez Sandoval Yeraldi Lizeth
print("\n\t----- HOLA Y BIENVENIDO -----\n")
Opera = {1: "Suma", 2: "Resta", 3: "Multiplicación", 4: "División"}
simbolo = {1: "+", 2: "-", 3: "*", 4: "/"}
op = []
Historial = []
Numero1 = []
Numero2 = []
res = 0
while True:
    opc = input("\nDesea realizar alguna operación? s/n: ")
    if opc == "s":
        print("\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Historial")
        while True:
            operacion = int(input("\nID de la operacion a realizar: "))
            if operacion <=4:
                op.append(operacion)
                num1 = int(input("\nTeclee el primer número: "))
                Numero1.append(num1)
                num2 = int(input("\nTeclee el segundo número: "))
                Numero2.append(num2)
                if operacion == 1:
                    res = num1 + num2
                    Historial.append(res)
                elif operacion == 2:
                    res = num1 - num2
                    Historial.append(res)
                elif operacion == 3:
                    res = num1 * num2
                    Historial.append(res)
                elif operacion == 4:
                    res = num1 / num2
                    Historial.append(res)
                print(f"El resultado de la operación {Opera[operacion]} que se seleccionó es: {res:.2f}")
                break
            elif operacion == 5:
                tam = len(Historial)
                if tam == 0:
                    print("Se encuentra vacio, no ha realizado una operación")
                else:
                    for n in range(0,tam):
                        x = op[n]
                        print(f"{Opera[x]} {Numero1[n]} {simbolo[x]} {Numero2[n]} = {Historial[n]}")

                    res = input("\nDesea borrar el historial? s/n: ")
                    if res == "s":
                        Historial.clear()
                        print(f"El historial ha sido limpiado, tiene {len(Historial)} elementos")
                        break
                    else:
                        break
            else:
                print("Lo sentimos, la opción no es válida, vuelva a intentarlo")
    else:
        print("\nGracias por su atención c:")
        break