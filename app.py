from abc import abstractmethod
from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion ():
    __ventana = None
    __altura = None
    __peso = None
    __resultado = None
    def __init__(self):
        # Creación de la ventana
        self.__ventana = Tk()
        self.__ventana.geometry('')
        self.__ventana.configure(bg = '#fff')
        self.__ventana.title('Calculadora de IMC')

        # Creación de cuadricula
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        # Creación de elementos
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__resultado = StringVar()
        
        # En la fila 1 estará el titulo
        ttk.Label(mainframe, text='Calculadora de IMC', anchor=CENTER).grid(column=2, row=1, sticky=(W,E))

        # En la fila 2 estará lo correspondiente a Altura
        ttk.Label(mainframe, text='Altura:').grid(column=1, row=2, sticky=(N,W))
        self.alturaEntry = ttk.Entry(mainframe, width=7, textvariable=self.__altura).grid(column=2, row=2, sticky= (W,E))
        ttk.Label(mainframe, text='cm').grid(column=3,row=2)
        
        # En la fila 3 estará lo correspondiente a Peso
        ttk.Label(mainframe, text='Peso:').grid(column=1, row=3, sticky=(N, W))
        self.pesoEntry = ttk.Entry(mainframe, width=7, textvariable=self.__peso).grid(column=2, row=3, sticky= (W,E))
        ttk.Label(mainframe, text='kg').grid(column=3,row=3)

        # En la fila 4 estarán los dos botones "Calcular" y "Limpiar"
        ttk.Button(mainframe, text='Calcular', command= self.calcular).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='Limpiar', command= self.limpiar).grid(column=3, row=4, sticky=W)
        
        # En la fila 5 estará el resultado
        ttk.Label(mainframe, textvariable=self.__resultado, foreground='#3c7642', background="#dff0d8", font="").grid(column=2, row=5)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            
        self.__ventana.mainloop()

    def calcular(self):
        try:
            valor = float(self.__peso.get()) / ((float(self.__altura.get())/100)**2)
            if valor < 18.5:
                aux = 'Peso inferior al normal'
            elif valor >= 18.5 and valor <= 24.9:
                aux = 'Peso normal'
            elif valor >= 25 and valor <= 29.9:
                aux = 'Peso superior al normal'
            elif valor >= 30:
                aux = 'Obesidad'
            self.__resultado.set(f"Tu indice de Masa Corporal (IMC) es {valor:.2f} \n {aux}")
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        self.__altura.set('')
        self.__peso.set('')

    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')

if __name__ == '__main__':
    app = Aplicacion()