from re import I
from tkinter import *
from math import *
import math 

ventana = Tk()
#Personalizar ventana
ventana.title("C A L C U L A D O R A")
ventana.iconbitmap("icono.ico")
ventana.configure(background="#694F71")
ventana.resizable(width=False, height=False)

#Entrada desde teclado
display = Entry(ventana, font=("Helvetica", 24, "bold"), bg="#CAB1D2", fg="#694F71", width=10, bd=10, justify=RIGHT)
display.grid(row=1, columnspan=5, sticky=W+E)
display.insert(0, "0")
display.delete(0, 1)

#Funciones
#Funciones para devolver los números que se van tecleando

#variables globales
i = 0
def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "0")

def calculate():
    global i
    ecuation = display.get()
    print(ecuation)
    if "sin" in str(ecuation) or "cos" in str(ecuation) or "tan" in str(ecuation) or "atan" in str(ecuation):
        ec=(eval(ecuation)*(180/math.pi))
        print(eval(ecuation))
        resultado=str(ec)
    else:
        resultado=str(eval(ecuation))
    #resultado = str(eval(ecuation))
    display.delete(0, END)
    display.insert(0, resultado)
    longitud = len(resultado)
    i = longitud
    


#Botones
Button(ventana, text="7", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(7)).grid(row=4, column=1, sticky=W+E)
Button(ventana, text="8", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(8)).grid(row=4, column=2, sticky=W+E)
Button(ventana, text="9", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(9)).grid(row=4, column=3, sticky=W+E)

Button(ventana, text="4", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(4)).grid(row=5, column=1, sticky=W+E)
Button(ventana, text="5", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(5)).grid(row=5, column=2, sticky=W+E)
Button(ventana, text="6", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(6)).grid(row=5, column=3, sticky=W+E)

Button(ventana, text="1", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(1)).grid(row=6, column=1, sticky=W+E)
Button(ventana, text="2", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(2)).grid(row=6, column=2, sticky=W+E)
Button(ventana, text="3", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(3)).grid(row=6, column=3, sticky=W+E)
#botones para signos  
Button(ventana, text="AC", width=2, height=2, bg="#818bca", fg="white",font=("Helvetica", 10, "bold"), command=lambda:clear_display()).grid(row=3, column=0, sticky=W+E)
Button(ventana, text="0", width=2, height=2, bg="#9734B4", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_numbers(0)).grid(row=7, column=1, sticky=W+E)
Button(ventana, text="(", width=2, height=2, bg="#818bca", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("(")).grid(row=7, column=2, sticky=W+E)
Button(ventana, text=")", width=2, height=2, bg="#818bca", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation(")")).grid(row=7, column=3, sticky=W+E)

Button(ventana, text="+", width=2, height=2, bg="#b25fc1", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("+")).grid(row=4, column=4, sticky=W+E)
Button(ventana, text="-", width=2, height=2, bg="#b25fc1", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("-")).grid(row=5, column=4, sticky=W+E)
Button(ventana, text="x", width=2, height=2, bg="#b25fc1", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("*")).grid(row=6, column=4, sticky=W+E)
Button(ventana, text="÷", width=2, height=2, bg="#b25fc1", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("/")).grid(row=7, column=4, sticky=W+E)

Button(ventana, text="⌫", width=2, height=2, bg="#818bca", fg="white",font=("Helvetica", 10, "bold"), command=lambda:undo()).grid(row=3, column=4, sticky=W+E)
Button(ventana, text="x²", width=2, height=2, bg="#4b569b", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("**2")).grid(row=5, column=0, sticky=W+E)
Button(ventana, text="exp", width=2, height=2, bg="#4b569b", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("**")).grid(row=6, column=0, sticky=W+E)
Button(ventana, text="ln", width=2, height=2, bg="#4b569b", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("log(")).grid(row=7, column=0, sticky=W+E)
Button(ventana, text="√", width=2, height=2, bg="#4b569b", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("sqrt(")).grid(row=8, column=0, sticky=W+E)
Button(ventana, text="mod", width=2, height=2, bg="#4b569b", fg="white",font=("Helvetica", 10, "bold"), command=lambda:get_operation("%")).grid(row=8, column=1, sticky=W+E)
Button(ventana, text="=", width=2, height=2, bg="#b25fc1", fg="white",font=("Helvetica", 10, "bold"), command=lambda:calculate()).grid(row=8, column=3, columnspan=2, sticky=W+E)

Button(ventana, text="sen", width=2, height=2, bg="#4b569b",font=("Helvetica", 10, "bold"), fg="white",
 command=lambda:get_operation("sin(")).grid(row=3, column=1, sticky=W+E)
Button(ventana, text="cos", width=2, height=2, bg="#4b569b",font=("Helvetica", 10, "bold"), fg="white",
 command=lambda:get_operation("cos(")).grid(row=3, column=2, sticky=W+E)
Button(ventana, text="tan", width=2, height=2, bg="#4b569b",font=("Helvetica", 10, "bold"), fg="white",
 command=lambda:get_operation("tan(")).grid(row=3, column=3, sticky=W+E)
Button(ventana, text="atan", width=2, height=2, bg="#4b569b",font=("Helvetica", 10, "bold"), fg="white",
 command=lambda:get_operation("atan(")).grid(row=4, column=0, sticky=W+E)
Button(ventana, text=".", width=2, height=2, bg="#818bca",font=("Helvetica", 10, "bold"), fg="white", command=lambda:get_operation(".")).grid(row=8, column=2, sticky=W+E)


ventana.mainloop()