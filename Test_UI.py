
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("920x450")
        self.title('Generador de Números Aleatorios')

        # initialize data
        self.menu = ("Método de los Centros Cuadrados",
      "Método Congruencial",
      "Método Congruencial Mixto",
      "Generador Multiplicativo",
      "Método Congruencial Lineal Combinado")

        # set up variable
        self.option = tk.StringVar(self)
        
        self.option.set(self.menu[0])
        
        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='SIMULADOR DE NUMEROS RANDOM',font = ("Castellar",15))
        label.grid(column=0, row=0, sticky=tk.W, **paddings)
        

        self.frame = tk.LabelFrame(self,text="Método de los Centros Cuadrados", borderwidth=8, padx=100, pady=50, labelanchor = "nw", font = ("Castellar",12))
        self.frame.place(x=10, y=70)

        
        
        # option menu
        option_menu = tk.OptionMenu(
            self,
            self.option,
            *self.menu,
            command=self.option_changed)
        
        helv36 = tkFont.Font(family='Castellar', size=8)
        option_menu.config(font=helv36)
        
        option_menu.place(x=585, y=10)


        
    def cuadrados_frame(self, *args):
        self.frame['text']="Método de los Centros Cuadrados"
        for widget in self.frame.winfo_children():
            widget.destroy()

        
        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20).grid(column=1,row=0)

        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20).grid(column=1,row=1)
        
        sumbit_btn= tk.Button(self.frame, text="Generar",font = ("Castellar",8)).place(relx=0.4, rely=1.1)
        
    def congruencial_frame(self, *args):

        self.frame['text']="Método Congruencial"
        for widget in self.frame.winfo_children():
            widget.destroy()

        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20).grid(column=1,row=0)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20).grid(column=1,row=1)
        
        incremento_label= ttk.Label(self.frame,  text='Incremento:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        incremento_input = ttk.Entry(self.frame, width=20).grid(column=1,row=2)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20).grid(column=1,row=3)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=4,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20).grid(column=1,row=4)        
        
        sumbit_btn= tk.Button(self.frame, text="Generar",font = ("Castellar",8)).place(relx=0.4, rely=1.1)
        
    
    def congruencial_mixto_frame(self, *args):

        self.frame['text']="Método Congruencial Mixto"
        
        for widget in self.frame.winfo_children():
            widget.destroy()

        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20).grid(column=1,row=0)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20).grid(column=1,row=1)
        
        incremento_label= ttk.Label(self.frame,  text='Incremento:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        incremento_input = ttk.Entry(self.frame, width=20).grid(column=1,row=2)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20).grid(column=1,row=3)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=4,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20).grid(column=1,row=4)  
        
        sumbit_btn= tk.Button(self.frame, text="Generar",font = ("Castellar",8)).place(relx=0.4, rely=1.1)
        
    
        
    def multiplicativo_frame(self, *args):

        self.frame['text']="Generador Multiplicativo"
        for widget in self.frame.winfo_children():
            widget.destroy()
            
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20).grid(column=1,row=0)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20).grid(column=1,row=1)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20).grid(column=1,row=2)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20).grid(column=1,row=3)    
        
        sumbit_btn= tk.Button(self.frame, text="Generar",font = ("Castellar",8)).place(relx=0.4, rely=1.1)
        
    def congruencial_lineal_frame(self, *args):

        self.frame['text']="Método Congruencial Lineal"
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        
        disclaimer = ttk.Label(self.frame,  text='Introduce tus valores con el siguiente formato: 456, 7891, 7831, ...',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        
        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20).grid(column=1,row=1)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20).grid(column=1,row=2)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20).grid(column=1,row=3)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=4,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20).grid(column=1,row=4)          
        
        sumbit_btn= tk.Button(self.frame, text="Generar",font = ("Castellar",8)).place(relx=0.5, rely=1.1)
        
    
    def option_changed(self, *args):
        if self.option.get() == self.menu[0]:
            self.cuadrados_frame()
        elif self.option.get() == self.menu[1]:
            self.congruencial_frame()
        elif self.option.get() == self.menu[2]:
            self.congruencial_mixto_frame()
        elif self.option.get() == self.menu[3]:
            self.multiplicativo_frame()
        elif self.option.get() == self.menu[4]:
            self.congruencial_lineal_frame()        

if __name__ == "__main__":
    app = App()
    app.mainloop()