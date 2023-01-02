import tkinter as tk

class Calculator:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()
        
    def create_widgets(self):
        # Creamos una pantalla de entrada para mostrar el resultado de las operaciones
        self.display = tk.Entry(self.parent, font=("Advanced Pixel LCD 7", 24))
        self.display.grid(row=0, column=0, columnspan=5)
        self.display.config(width=30)

        # Creamos los botones numéricos
        self.button9 = tk.Button(self.parent, text="9", font=("Helvetica", 24), command=self.add_char("9"), width=5, height=2)
        self.button9.grid(row=1, column=2)
        self.button8 = tk.Button(self.parent, text="8", font=("Helvetica", 24), command=self.add_char("8"), width=5, height=2)
        self.button8.grid(row=1, column=1)
        self.button7 = tk.Button(self.parent, text="7", font=("Helvetica", 24), command=self.add_char("7"), width=5, height=2)
        self.button7.grid(row=1, column=0)
        self.button6 = tk.Button(self.parent, text="6", font=("Helvetica", 24), command=self.add_char("6"), width=5, height=2)
        self.button6.grid(row=2, column=0)
        self.button5 = tk.Button(self.parent, text="5", font=("Helvetica", 24), command=self.add_char("5"), width=5, height=2)
        self.button5.grid(row=2, column=1)
        self.button4 = tk.Button(self.parent, text="4", font=("Helvetica", 24), command=self.add_char("4"), width=5, height=2)
        self.button4.grid(row=2, column=2)
        self.button3 = tk.Button(self.parent, text="3", font=("Helvetica", 24), command=self.add_char("3"), width=5, height=2)
        self.button3.grid(row=3, column=0)
        self.button2 = tk.Button(self.parent, text="2", font=("Helvetica", 24), command=self.add_char("2"), width=5, height=2)
        self.button2.grid(row=3, column=1)
        self.button1 = tk.Button(self.parent, text="1", font=("Helvetica", 24), command=self.add_char("1"), width=5, height=2)
        self.button1.grid(row=3, column=2)

       # Creamos los botones de operación
        self.button_add = tk.Button(self.parent, text="+", font=("Helvetica", 24), command=self.add_char("+"), width=5, height=2)
        self.button_add.grid(row=1, column=3)
        self.button_subtract = tk.Button(self.parent, text="-", font=("Helvetica", 24), command=self.add_char("-"), width=5, height=2)
        self.button_subtract.grid(row=1, column=4)
        self.button_subtract = tk.Button(self.parent, text="*", font=("Helvetica", 24), command=self.add_char("*"), width=5, height=2)
        self.button_subtract.grid(row=2, column=3)
        self.button_subtract = tk.Button(self.parent, text="/", font=("Helvetica", 24), command=self.add_char("/"), width=5, height=2)
        self.button_subtract.grid(row=2, column=4)
        
        # Creamos el botón para limpiar la pantalla
        self.button_clear = tk.Button(self.parent, text="C", font=("Helvetica", 24), command=self.clear, width=5, height=2)
        self.button_clear.grid(row=3, column=3)

        # Creamos el botón de igual
        self.button_equal = tk.Button(self.parent, text="=", font=("Helvetica", 24), command=self.calculate, width=5, height=2)
        self.button_equal.grid(row=3, column=4)

    def add_char(self, char):
        # Esta función se encarga de añadir un carácter a la pantalla de entrada
        def inner():
            self.display.insert("end", char)
        return inner

    def clear(self):
    # Esta función se encarga de limpiar la pantalla de entrada
        self.display.delete(0, "end")
        
    def calculate(self):
        # Esta función se encarga de calcular el resultado de la expresión en la pantalla de entrada
        result = eval(self.display.get())
        self.display.delete(0, "end")
        self.display.insert("end", result)
    
# Creamos la ventana principal
root = tk.Tk()
root.title("Calculadora")
# Obtenemos el ancho y alto de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Calculamos las coordenadas de la ventana de manera que aparezca en el centro de la pantalla
window_x = (screen_width - 605) // 2
window_y = (screen_height - 300) // 2
# Establecemos las coordenadas de la ventana
root.geometry(f"605x300+{window_x}+{window_y}")

root.resizable(False, False)

# Creamos la instancia de la calculadora y la mostramos en la ventana
calculator = Calculator(root)

# Iniciamos el bucle de eventos de tkinter
root.mainloop()
