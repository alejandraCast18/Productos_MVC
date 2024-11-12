import tkinter as tk
import tkinter.messagebox as MessageBox
from tkinter import ttk

class Vista(tk.Frame):
    def __init__(self, root):
        super().__init__(root) 
        self.root = root
        root.title('')
        root.minsize(height= 475, width=795)
        root.geometry('1000x500+180+80')
        root.call('wm', 'iconphoto', root._w, tk.PhotoImage('imagenes/synergy.png'))

        self.controlador = None
        self.menu = True
        self.tooltip_message = ""
       
        self.codigo = tk.StringVar()
        self.codigo.trace_add('write', lambda *args: self.codigo.set(self.codigo.get().upper()))
        self.nombre = tk.StringVar()
        self.nombre.trace_add('write', lambda *args: self.nombre.set(self.nombre.get().upper()))
        self.modelo = tk.StringVar()
        self.modelo.trace_add('write', lambda *args: self.modelo.set(self.modelo.get().upper()))
        self.precio = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.buscar = tk.StringVar()
        self.buscar_actualiza =  tk.StringVar()
        self.id = tk.StringVar()
        ###
        self.logo = tk.PhotoImage(file ='imagenes/synergy_logo.png')
        self.frame_inicio = tk.Frame(self.root, bg='black', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
        self.frame_menu = tk.Frame(self.root, bg='black', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        self.frame_top = tk.Frame(self.root, bg='black', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        self.frame_principal = tk.Frame(self.root, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.titulo = tk.Label(self.frame_top,text= 'MVC EN PYTHON CON TKINTER Y MYSQL', bg='black', fg= 'orange', font= ('Arial', 15, 'bold'))
        self.titulo.pack(expand=1)


        self.set_paginas()
        self.set_imagenes()
        self.set_botones()
        self.set_etiquetas()
        self.mostrar_treeview()
        self.mostrar_formulario_incluir()
        self.mostrar_formulario_modificar()
        self.mostrar_formulario_eliminar()



    def set_paginas(self):
        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='black', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected", 'black')])
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);

        self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook')
        self.paginas.grid(column=0,row=0, sticky='nsew')
        self.frame_uno = tk.Frame(self.paginas, bg='white')
        self.frame_dos = tk.Frame(self.paginas, bg='white')
        self.frame_tres = tk.Frame(self.paginas, bg='white')
        self.frame_cuatro = tk.Frame(self.paginas, bg='white')
        self.frame_cinco = tk.Frame(self.paginas, bg='white')
        self.frame_seis = tk.Frame(self.paginas, bg='white')
        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)
        self.paginas.add(self.frame_tres)
        self.paginas.add(self.frame_cuatro)
        self.paginas.add(self.frame_cinco)
        self.paginas.add(self.frame_seis)


    def set_menu_lateral(self):
        if self.menu is True:
            for i in range(50,170,10):
                self.frame_menu.config(width= i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_cerrar.grid_forget()
                if clik_inicio is None:
                    self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
                    self.bt_inicio.grid_propagate(0)
                    self.bt_inicio.config(width=i)
                    self.set_pantalla_inicial()
                    self.menu = False
        else:
            for i in range(170,50,-10):
                self.frame_menu.config(width=  i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_inicio.grid_forget()
                if clik_inicio is None:
                    self.frame_menu.grid_propagate(0)
                    self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
                    self.bt_cerrar.grid_propagate(0)
                    self.bt_cerrar.config(width=i)
                    self.set_pantalla_inicial()
                    self.menu = True


    def set_pantalla_inicial(self):
        self.paginas.select([self.frame_uno])


    def set_imagenes(self):
        tk.Label(self.frame_uno ,image= self.logo, bg='white').pack(expand=1)
        self.imagen_inicio = tk.PhotoImage(file ='imagenes/inicio.png')
        self.imagen_menu = tk.PhotoImage(file ='imagenes/menu.png')
        self.imagen_datos = tk.PhotoImage(file ='imagenes/datos.png')
        self.imagen_registrar = tk.PhotoImage(file ='imagenes/escribir.png')
        self.imagen_actualizar = tk.PhotoImage(file ='imagenes/actualizar.png')
        self.imagen_buscar = tk.PhotoImage(file ='imagenes/buscar.png')
        self.imagen_eliminar = tk.PhotoImage(file ='imagenes/eliminar.png')
        self.imagen_uno = tk.PhotoImage(file ='imagenes/imagen_uno.png')
        self.imagen_dos= tk.PhotoImage(file ='imagenes/imagen_dos.png')
        self.bt_inicio = tk.Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.set_menu_lateral)
        self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)

        self.bt_cerrar = tk.Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black', bd=0, command = self.set_menu_lateral)
        self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)
        self.tooltip_message = 'Expandir el menú'
        self.bt_cerrar.bind("<Enter>", self.show_tooltip)
        self.bt_cerrar.bind("<Leave>", self.hide_tooltip)


    def set_botones(self):
        tk.Button(self.frame_menu, image= self.imagen_datos, bg='black', activebackground='black', bd=0, command = self.clic_consultar).grid(column=0, row=1, pady=20,padx=10)
        tk.Button(self.frame_menu, image= self.imagen_registrar, bg='black',activebackground='black', bd=0, command = self.clic_agregar).grid(column=0, row=2, pady=20,padx=10)
        tk.Button(self.frame_menu, image= self.imagen_actualizar, bg= 'black',activebackground='black', bd=0, command = self.clic_modificar).grid(column=0, row=3, pady=20,padx=10)
        tk.Button(self.frame_menu, image= self.imagen_buscar, bg= 'black',activebackground='black', bd=0, command = self.clic_borrar).grid(column=0, row=4, pady=20,padx=10)


    def set_etiquetas(self):
        tk.Label(self.frame_menu, text= 'Consultar', bg= 'black', fg= 'orange', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
        tk.Label(self.frame_menu, text= 'Registrar', bg= 'black', fg= 'orange', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
        tk.Label(self.frame_menu, text= 'Actualizar', bg= 'black', fg= 'orange', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
        tk.Label(self.frame_menu, text= 'Eliminar', bg= 'black', fg= 'orange', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)


    def set_controlador(self, controlador):
        self.controlador = controlador


    def clic_consultar(self):
        info = self.controlador.consultar_todo()
        self.set_pantalla_datos()
        self.mostrar_datos_totales(info)

    def set_pantalla_datos(self):
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.columnconfigure(1, weight=1)
        self.frame_dos.rowconfigure(2, weight=1)
        self.frame_tabla_uno.columnconfigure(0, weight=1)
        self.frame_tabla_uno.rowconfigure(0, weight=1)

    def mostrar_treeview(self):
        tk.Label(self.frame_dos, text= 'Datos de los Productos', bg='white', fg= 'black', font= ('Arial', 12, 'bold')).grid(column =0, row=0)
        #Definir los estilos de la tabla
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo_tabla.map('Treeview',background=[('selected', 'blue')], foreground=[('selected','white')] )
        estilo_tabla.configure('Heading',background = 'white', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
        estilo_tabla.configure('Item',foreground = 'white', focuscolor ='blue')
        estilo_tabla.configure('TScrollbar', arrowcolor = 'blue',bordercolor  ='black', troughcolor= 'blue',background ='white')
		#Tabla uno
        self.frame_tabla_uno = tk.Frame(self.frame_dos, bg= 'gray90')
        self.frame_tabla_uno.grid(columnspan=3, row=2, sticky='nsew')
        self.tabla_uno = ttk.Treeview(self.frame_tabla_uno)
        self.tabla_uno.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_uno, orient = 'horizontal', command= self.tabla_uno.xview)
        ladox.grid(column=0, row = 1, sticky='ew')
        ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient ='vertical', command = self.tabla_uno.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_uno.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_uno['columns'] = ('Nombre', 'Modelo', 'Precio', 'Cantidad')
        self.tabla_uno.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla_uno.column('Nombre', minwidth=100, width=130 , anchor='center')
        self.tabla_uno.column('Modelo', minwidth=100, width=120, anchor='center' )
        self.tabla_uno.column('Precio', minwidth=100, width=120 , anchor='center')
        self.tabla_uno.column('Cantidad', minwidth=100, width=105, anchor='center')

        self.tabla_uno.heading('#0', text='Código', anchor ='center')
        self.tabla_uno.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_uno.heading('Modelo', text='Modelo', anchor ='center')
        self.tabla_uno.heading('Precio', text='Precio', anchor ='center')
        self.tabla_uno.heading('Cantidad', text='Cantidad', anchor ='center')
        self.tabla_uno.bind("<<TreeviewSelect>>", self.obtener_fila)

    def mostrar_datos_totales(self, info):
        self.tabla_uno.delete(*self.tabla_uno.get_children())
        i = -1
        for producto in info:
            i= i+1
            self.tabla_uno.insert('',i, text = producto[1:2], values=producto[2:6])

    def obtener_fila(self, event):
        current_item = self.tabla_uno.focus()
        if not current_item:
            return
        data = self.tabla_uno.item(current_item)
        self.nombre_borrar = data['values'][0]



    def clic_agregar(self):
        self.paginas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.columnconfigure(1, weight=1)
        self.limpiar_variables()
        self.after(500, self.cod_pro.focus())

    def mostrar_formulario_incluir(self):
        tk.Label(self.frame_tres, text = 'Agregar Nuevo Producto',fg='black', bg ='white', font=('Arial',20,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        tk.Label(self.frame_tres, text = 'Código',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=1, pady=15, padx=15)
        tk.Label(self.frame_tres, text = 'Nombre',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=2, pady=15)
        tk.Label(self.frame_tres, text = 'Modelo',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=3, pady=15)
        tk.Label(self.frame_tres, text = 'Precio', fg='black',bg ='white', font=('Arial',14,'bold')).grid(column=0,row=4, pady=15)
        tk.Label(self.frame_tres, text = 'Cantidad',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=5, pady=15)

        vcmd_cod = (self.register(self.on_validate), '%P', '10')
        self.cod_pro = tk.Entry(self.frame_tres, textvariable=self.codigo, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_cod)
        self.cod_pro.grid(column=1,row=1)
        #self.cod_pro.focus()

        vcmd_nom = (self.register(self.on_validate), '%P', '20')
        self.nom_pro = tk.Entry(self.frame_tres, textvariable=self.nombre, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_nom)
        self.nom_pro.grid(column=1,row=2)

        self.mod_pro = tk.Entry(self.frame_tres, textvariable=self.modelo, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_nom)
        self.mod_pro.grid(column=1,row=3)

        vcmd_pre = (self.register(self.on_validate), '%P', '12')
        self.pre_pro = tk.Entry(self.frame_tres, textvariable=self.precio, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_pre)
        self.pre_pro.bind('<KeyRelease>', self.verificar_num_dec)
        self.pre_pro.grid(column=1,row=4)

        vcmd_can = (self.register(self.on_validate), '%P', '5')
        self.can_pro = tk.Entry(self.frame_tres, textvariable=self.cantidad, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_can)
        self.can_pro.bind('<KeyRelease>', lambda e: self.verificar_num())
        self.can_pro.grid(column=1,row=5)

        tk.Button(self.frame_tres,command= self.clic_registrar, text='Registrar', font=('Arial',14,'bold'), bg='green').grid(column=3,row=6, pady=10, padx=4)

        tk.Label(self.frame_tres, image= self.imagen_uno, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)

        self.limpiar_variables()

    def clic_registrar(self):
        cod_pro = self.codigo.get()
        nom_pro = self.nombre.get()
        mod_pro = self.modelo.get()
        pre_pro = self.precio.get()
        can_pro = self.cantidad.get()
        if cod_pro == "" or nom_pro == "" or mod_pro == "" or pre_pro == "" or can_pro == "":
            MessageBox.showerror("ERROR", "Debe ingresar todos los campos")
        else:
            result = self.controlador.insertar(cod_pro, nom_pro, mod_pro, pre_pro, can_pro)
            if not(isinstance(result, int)):
                MessageBox.showerror("Error", result)
            else:
                if result > 0:
                    MessageBox.showinfo("Status", "Insertado exitosamente")
                    self.limpiar_variables()
                    self.after(500, self.cod_pro.focus())

    def limpiar_variables(self):
        self.codigo.set('')
        self.nombre.set('')
        self.modelo.set('')
        self.precio.set('')
        self.cantidad.set('')


    def clic_modificar(self):
        self.paginas.select([self.frame_cuatro])
        self.frame_cuatro.columnconfigure(0, weight=1)
        self.frame_cuatro.columnconfigure(1, weight=1)
        self.cod_prom.config(state='normal')
        self.boton_actualizar.config(state='disabled')
        self.limpiar_cajasm()
        self.after(500, self.cod_prom.focus())

    def mostrar_formulario_modificar(self):
        tk.Label(self.frame_cuatro, text = 'Modificar Producto',fg='black', bg ='white', font=('Arial',20,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        tk.Label(self.frame_cuatro, text = 'Código',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=1, pady=15, padx=15)
        tk.Label(self.frame_cuatro, text = 'Nombre',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=2, pady=15)
        tk.Label(self.frame_cuatro, text = 'Modelo',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=3, pady=15)
        tk.Label(self.frame_cuatro, text = 'Precio', fg='black',bg ='white', font=('Arial',14,'bold')).grid(column=0,row=4, pady=15)
        tk.Label(self.frame_cuatro, text = 'Cantidad',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=5, pady=15)

        vcmd_cod = (self.register(self.on_validate), '%P', '10')
        self.cod_prom = tk.Entry(self.frame_cuatro, textvariable=self.codigo, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_cod)
        self.cod_prom.grid(column=1,row=1)

        vcmd_nom = (self.register(self.on_validate), '%P', '20')
        self.nom_prom = tk.Entry(self.frame_cuatro, textvariable=self.nombre, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_nom)
        self.nom_prom.grid(column=1,row=2)

        self.mod_prom = tk.Entry(self.frame_cuatro, textvariable=self.modelo, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_nom)
        self.mod_prom.grid(column=1,row=3)

        vcmd_pre = (self.register(self.on_validate), '%P', '12')
        self.pre_prom = tk.Entry(self.frame_cuatro, textvariable=self.precio, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_pre)
        self.pre_prom.bind('<KeyRelease>', self.verificar_num_dec)
        self.pre_prom.grid(column=1,row=4)

        vcmd_can = (self.register(self.on_validate), '%P', '5')
        self.can_prom = tk.Entry(self.frame_cuatro, textvariable=self.cantidad, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_can)
        self.can_prom.bind('<KeyRelease>', lambda e: self.verificar_num())
        self.can_prom.grid(column=1,row=5)

        self.boton_buscar = tk.Button(self.frame_cuatro,command= self.clic_buscar, text='Buscar', font=('Arial',14,'bold'), bg='sky blue').grid(column=2,row=1, pady=10, padx=4)

        self.boton_actualizar = tk.Button(self.frame_cuatro,command= self.clic_actualizar, text='Actualizar', font=('Arial',14,'bold'), bg='green', state="disabled")
        self.boton_actualizar.grid(column=2,row=6, pady=10, padx=4)

        tk.Label(self.frame_cuatro, image= self.imagen_dos, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)

        self.aviso_encontrado = tk.Label(self.frame_cuatro, bg= 'white', font=('Arial', 12), fg='black')
        self.aviso_encontrado.grid(columnspan= 2 , column =0, row = 6, padx= 5)

    def limpiar_cajasm(self):
        self.aviso_encontrado.config(text = "")
        self.aviso_encontrado.update()
        self.limpiar_variables()

    def clic_buscar(self):
        self.aviso_encontrado.config(text = "")
        self.aviso_encontrado.update()
        cod_pro = self.codigo.get()
        if cod_pro == "":
            MessageBox.showerror("ERROR","Se requiere el código para ubicar el producto")
        else:
            info = self.controlador.consultar(cod_pro)
            if info:
                self.limpiar_cajasm()
                self.cod_prom.insert(0, info[1])
                self.nom_prom.insert(0, info[2])
                self.mod_prom.insert(0, info[3])
                self.pre_prom.insert(0, info[4])
                self.can_prom.insert(0, info[5])
                self.cod_prom.config(state="readonly")
                self.boton_actualizar.config(state='normal')
            else:
                self.aviso_encontrado.config(text = "No encontrado")
                self.aviso_encontrado.update()

    def clic_actualizar(self):
        cod_pro = self.codigo.get()
        nom_pro = self.nombre.get()
        mod_pro = self.modelo.get()
        pre_pro = self.precio.get()
        can_pro = self.cantidad.get()
        if nom_pro == "" or mod_pro == "" or pre_pro == "" or can_pro == "":
            MessageBox.showerror("ERROR", "Se requieren los campos a actualizar")
        else:
            result = self.controlador.actualizar(cod_pro, nom_pro, mod_pro, pre_pro, can_pro)
            if not(isinstance(result, int)):
                MessageBox.showerror("Error", result)
            else:
                if result > 0:
                    MessageBox.showinfo("Status", "Modificado exitosamente")
                else:
                    MessageBox.showinfo("Status", "Nada que modificar")



    def clic_borrar(self):
        self.paginas.select([self.frame_cinco])
        self.frame_cinco.columnconfigure(0, weight=1)
        self.frame_cinco.columnconfigure(1, weight=1)
        self.cod_proe.config(state='normal')
        self.boton_eliminar.config(state='disabled')
        self.limpiar_cajase()
        self.after(500, self.cod_proe.focus())

    def mostrar_formulario_eliminar(self):
        tk.Label(self.frame_cinco, text = 'Eliminar Producto',fg='black', bg ='white', font=('Arial',20,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        tk.Label(self.frame_cinco, text = 'Código',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=1, pady=15, padx=15)
        tk.Label(self.frame_cinco, text = 'Nombre',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=2, pady=15)
        tk.Label(self.frame_cinco, text = 'Modelo',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=3, pady=15)
        tk.Label(self.frame_cinco, text = 'Precio', fg='black',bg ='white', font=('Arial',14,'bold')).grid(column=0,row=4, pady=15)
        tk.Label(self.frame_cinco, text = 'Cantidad',fg='black', bg ='white', font=('Arial',14,'bold')).grid(column=0,row=5, pady=15)

        vcmd_cod = (self.register(self.on_validate), '%P', '10')
        self.cod_proe = tk.Entry(self.frame_cinco, textvariable=self.codigo, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, validate='key',validatecommand=vcmd_cod)
        self.cod_proe.grid(column=1,row=1)

        self.nom_proe = tk.Entry(self.frame_cinco, textvariable=self.nombre, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, state='readonly')
        self.nom_proe.grid(column=1,row=2)

        self.mod_proe = tk.Entry(self.frame_cinco, textvariable=self.modelo, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, state='readonly')
        self.mod_proe.grid(column=1,row=3)

        self.pre_proe = tk.Entry(self.frame_cinco, textvariable=self.precio, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, state='readonly')
        self.pre_proe.grid(column=1,row=4)

        vcmd_can = (self.register(self.on_validate), '%P', '5')
        self.can_proe = tk.Entry(self.frame_cinco, textvariable=self.cantidad, font=('Arial', 14), highlightbackground = "black", highlightcolor= "green", highlightthickness=5, state='readonly')
        self.can_proe.grid(column=1,row=5)

        self.boton_buscare = tk.Button(self.frame_cinco,command= self.clic_buscare, text='Buscar', font=('Arial',14,'bold'), bg='sky blue').grid(column=2,row=1, pady=10, padx=4)

        self.boton_eliminar = tk.Button(self.frame_cinco,command= self.clic_eliminar, text='Eliminar', font=('Arial',14,'bold'), fg='white', bg='red', state="disabled")
        self.boton_eliminar.grid(column=2,row=6, pady=10, padx=4)

        tk.Label(self.frame_cinco, image= self.imagen_eliminar, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)

        self.aviso_encontradoe = tk.Label(self.frame_cinco, bg= 'white', font=('Arial', 12), fg='black')
        self.aviso_encontradoe.grid(columnspan= 2 , column =0, row = 6, padx= 5)

    def limpiar_cajase(self):
        self.aviso_encontradoe.config(text = "")
        self.aviso_encontradoe.update()
        self.limpiar_variables()

    def activar_desactivar_cajas(self, estado):
        self.nom_proe.config(state=estado)
        self.mod_proe.config(state=estado)
        self.pre_proe.config(state=estado)
        self.can_proe.config(state=estado)

    def clic_buscare(self):
        self.aviso_encontradoe.config(text = "")
        self.aviso_encontradoe.update()
        cod_pro = self.codigo.get()
        if cod_pro == "":
            MessageBox.showerror("ERROR","Se requiere el código para ubicar el producto")
        else:
            info = self.controlador.consultar(cod_pro)
            if info:
                self.limpiar_cajase()
                self.activar_desactivar_cajas('normal')
                self.cod_proe.insert(0, info[1])
                self.nom_proe.insert(0, info[2])
                self.mod_proe.insert(0, info[3])
                self.pre_proe.insert(0, info[4])
                self.can_proe.insert(0, info[5])
                self.activar_desactivar_cajas('readonly')
                self.boton_eliminar.config(state='normal')
            else:
                self.nombre.set('')
                self.modelo.set('')
                self.precio.set('')
                self.cantidad.set('')
                self.aviso_encontradoe.config(text = "No encontrado")
                self.aviso_encontradoe.update()

    def clic_eliminar(self):
        cod_pro = self.codigo.get()
        if cod_pro == "":
            MessageBox.showerror("ERROR", "Ingrese el código para eliminar el producto")
        else:
            if MessageBox.askokcancel("Consulta", "¿Está seguro de eliminar el producto?"):
                result = self.controlador.eliminar(cod_pro)
                if result > 0:
                    MessageBox.showinfo("Status", "Eliminado exitosamente")
                    self.limpiar_cajase()
                    self.cod_proe.focus()

    def on_validate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True

    def verificar_num(self):
        cantidad = self.can_pro.get()
        for i in cantidad:
            if i not in '0123456789':
                self.can_pro.delete(cantidad.index(i), cantidad.index(i)+1)

    def verificar_num_dec(self, event):
        key = event.char #Captura la tecla pulsada
        cantidad = self.pre_pro.get()
        #Verifica que el punto no se haya incluido ya, y si es así,
        # lo elimina del entry
        if key == '.' and cantidad.count('.') > 1:
            self.pre_pro.delete(len(cantidad)-1, len(cantidad))
        else:
            for i in cantidad:
                if i not in '0123456789.':
                    self.pre_pro.delete(cantidad.index(i), cantidad.index(i)+1)



    def show_tooltip(self, event):
        self.tooltip_window = tk.Toplevel(self.root)
        tooltip_label = tk.Label(self.tooltip_window, text=self.tooltip_message, fg='black', bg='yellow')
        tooltip_label.pack()

        self.tooltip_window.overrideredirect(True)

        x = self.root.winfo_pointerx() + 50
        y = self.root.winfo_pointery() + 20
        self.tooltip_window.geometry("+{}+{}".format(x, y))

    def hide_tooltip(self, event):
        # Destroy the tooltip window
        self.tooltip_window.destroy()
        self.tooltip_window = None