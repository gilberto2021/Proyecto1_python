from tkinter import *

ventana = Tk()
ventana.title("calculadora")
ventana.geometry("450x600")
ventana.resizable(False,False)
ventana.configure(background="gray")

#funciones
operacion = ""
resultado = StringVar()

def Borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0,END)

def Pulsar(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0, operacion)

def Calcular():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado="Error"
    finally:
        pantalla.delete(0,END)
        pantalla.insert(0, resultado)



#display de los resultados
pantalla = Entry(ventana, font=("arial",20,"bold"), borderwidth=2)
pantalla.grid(row=0, column=0, columnspan=3, pady=10, padx=5)

#boton de reiniciar
boton_reset = Button(ventana, text="AC", width=8, height=2, command=lambda:Borrar())
boton_reset.grid(row=0, column=3, pady=10)

#botones

ancho = 8
alto = 3

boton1 = Button(ventana, text="1", width=ancho, height=alto, command=lambda:Pulsar("1"))
boton1.grid(row=1, column=0, padx=5, pady=5)

boton2 = Button(ventana, text="2", width=ancho, height=alto, command=lambda:Pulsar("2"))
boton2.grid(row=1, column=1, padx=5, pady=5)

boton3 = Button(ventana, text="3", width=ancho, height=alto, command=lambda:Pulsar("3"))
boton3.grid(row=1, column=2, padx=5, pady=5)

boton4 = Button(ventana, text="4", width=ancho, height=alto, command=lambda:Pulsar("4"))
boton4.grid(row=1, column=3, padx=5, pady=5)

boton5 = Button(ventana, text="5", width=ancho, height=alto, command=lambda:Pulsar("5"))
boton5.grid(row=2, column=0, padx=5, pady=5)

boton6 = Button(ventana, text="6", width=ancho, height=alto, command=lambda:Pulsar("6"))
boton6.grid(row=2, column=1, padx=5, pady=5)

boton7 = Button(ventana, text="7", width=ancho, height=alto, command=lambda:Pulsar("7"))
boton7.grid(row=2, column=2, padx=5, pady=5)

boton8 = Button(ventana, text="8", width=ancho, height=alto, command=lambda:Pulsar("8"))
boton8.grid(row=2, column=3, padx=5, pady=5)

boton9 = Button(ventana, text="9", width=ancho, height=alto, command=lambda:Pulsar("9"))
boton9.grid(row=3, column=0, padx=5, pady=5)

boton0 = Button(ventana, text="0", width=ancho, height=alto, command=lambda:Pulsar("0"))
boton0.grid(row=3, column=1, padx=5, pady=5)

boton_punto = Button(ventana, text=".", width=ancho, height=alto, command=lambda:Pulsar("."))
boton_punto.grid(row=3, column=2, padx=5, pady=5)

boton_suma = Button(ventana, text="+", width=ancho, height=alto, command=lambda:Pulsar("+"))
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton_resta = Button(ventana, text="-", width=ancho, height=alto, command=lambda:Pulsar("-"))
boton_resta.grid(row=4, column=0, padx=5, pady=5)

boton_multiplicar = Button(ventana, text="*", width=ancho, height=alto, command=lambda:Pulsar("*"))
boton_multiplicar.grid(row=4, column=1, padx=5, pady=5)

boton_dividir = Button(ventana, text="/", width=ancho, height=alto, command=lambda:Pulsar("/"))
boton_dividir.grid(row=4, column=2, padx=5, pady=5)

boton_calcular = Button(ventana, text="=", width=ancho, height=alto, command=lambda:Calcular())
boton_calcular.grid(row=4, column=3, padx=5, pady=5)


ventana.mainloop()

