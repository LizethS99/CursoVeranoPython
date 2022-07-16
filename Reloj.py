#Reloj Sánchez Sandoval Yeraldi Lizeth
import os
import time

while True:
    entrada = input("\n\tIngrese la hora hora:minutos:segundos de esta manera: ")
    lista = entrada.split(":") ## 5:12:41 - ["5", "12", "41"]
    tam = len(lista)
    if ":" in entrada and tam == 3: 
#Con este if le pedimos que verifique que haya dos puntos para que este en el formato para que posteriormente se asegure 
#que solo estan ingresando 3 elementos, es decir hora:minutos:segundos
        print(f"\n\t{lista[0]}:{lista[1]}:{lista[2]}")
        e_hora = int(lista [0])
        e_minuto = int(lista[1])
        e_segundo = int(lista[2])
        if e_hora <=24 and e_minuto <= 60 and e_segundo <= 60:
            #Aquí verificamos que la hora ingresada sea dentro de un rango real 
            for hora in range(e_hora, 24):
                for minuto in range(e_minuto, 60):
                    for segundo in range(e_segundo, 60):
                        #os.system("cls") para windows
                        os.system("clear") #Linux o mac
                        print(f"{hora}:{minuto}:{segundo}")
                        time.sleep(1)
            
                        if segundo == 59:
                            segundo = 0
                            e_segundo = 0
        
                    if minuto == 59:
                        minuto = 0
                        e_minuto = 0 
        
                if hora == 23:
                    hora = 0
                    e_hora = 0
            break
        else:
            print("\nNo se encunetra en un rango real de hora")
    else :
        print("\nEl formato no es correcto, asegurese de ingresar hora:minutos:segundos, por favor vuelva a intentarlo ")