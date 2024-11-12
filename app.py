import tkinter as tk
from modelo import Modelo
from vista import Vista
from controlador import Controlador

ventana = tk.Tk()
bd = Modelo() 
vista = Vista(ventana) 
controlador = Controlador(bd) 
vista.set_controlador(controlador) 


if __name__ == '__main__':
    app = vista
    app.mainloop()