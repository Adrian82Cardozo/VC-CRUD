import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

form_font = ("Arial",10)
global miConexion
global miCursor
originales = True

class Form1:
    global controlID
    global textoID
    global valorID

    def __init__(self, master):
        self.master = master
        master.title("CRUD by JC")
        master.geometry("640x320")

        master.grid_columnconfigure(3)
        master.grid_rowconfigure(7)

        #<=========== Menú ==========>#
        menuBar=Menu(master)
        master.config(menu=menuBar)
        menuItem1=Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Archivo", menu = menuItem1)
        menuItem1.add_command(label = "Conectar", command = lambda:AccionCrear())
        menuItem1.add_command(label = "Salir", command = lambda:self.close_window())
        menuItem2=Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Ayuda", menu = menuItem2)
        menuItem2.add_command(label = "Acerca de...", command = lambda:borra_campos())

        #<=========== Controles ==========>#
        # button1 = Button(master,text='New Window', width=10,command=self.new_window).grid(row=0,column=0,padx=2,pady=2)
        # button2 = Button(master,text='Exit', width=10,command=self.close_window).grid(row=0,column=1,padx=2,pady=2)

        lbl_id = Label(master,font=form_font,text="ID").grid(row=1,column=0,padx=10,pady=10)
        var_id = StringVar()
        txt_id=Entry(master,font=form_font,state="disabled",textvariable=var_id,width=50).grid(row=1,column=1,padx=10,pady=10)

        lbl_nombre = Label(master,font = form_font, text = "Nombre").grid(row=2,column=0,padx=10,pady=10)
        var_nombre = StringVar()
        txt_nombre=Entry(master,font=form_font,textvariable=var_nombre,width=50).grid(row=2,column=1,padx=10,pady=10)

        lbl_apellido = Label(master,font = form_font, text = "Apellido").grid(row=3,column=0,padx=10,pady=10)
        var_apellido = StringVar()
        txt_apellido=Entry(master,font=form_font,textvariable=var_apellido,width=50).grid(row=3,column=1,padx=10,pady=10)

        lbl_password = Label(master,font = form_font, text = "Password").grid(row=4,column=0,padx=10,pady=10)
        var_password = StringVar()
        txt_password=Entry(master,font=form_font,textvariable=var_password,width=50).grid(row=4,column=1,padx=10,pady=10)

        lbl_direccion = Label(master,font = form_font, text = "Dirección").grid(row=5,column=0,padx=10,pady=10)
        var_direccion = StringVar()
        txt_direccion=Entry(master,font=form_font,textvariable=var_direccion,width=50).grid(row=5,column=1,padx=10,pady=10)

        lbl_comentario = Label(master,font = form_font, text = "Comentario").grid(row=6,column=0,padx=10,pady=10)
        var_comentario = ""
        global textoComentario
        #txt_comentario=Entry(master,font=form_font,textvariable=var_comentario,width=50).grid(row=6,column=1,padx=10,pady=10)
        txt_comentario=Text(master,font=form_font, height=7, width=20).grid(row=6,column=1,padx=10,pady=10)
        #txt_comentario.setvar(var_comentario)
        #txt_comentario.insert(INSERT,var_comentario)
        
        scrollvert=Scrollbar(master,command=txt_comentario.yview).grid(row=6,column=2,sticky="nsew")
        txt_comentario.config(yscrollcommand=scrollvert.set)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Form2(self.newWindow)
    
    def close_window(self):
        valor=messagebox.askyesno("Salir", "¿Deseas salir de la aplicación?")
        if valor==True:
            self.master.destroy()

    def borra_campos():
        txt_id.set("")
        txt_nombre.set("")
        txt_password.set("")
        txt_apellido.set("")
        txt_direccion.set("")
        txt_comentario.delete(1.0,END)
    
    def AccionAgregar():
        dataUsuario=[var_nombre.get(),var_password.get(),var_apellido.get(),var_direccion.get(),var_comentario.get(1.0,END)]
        miCursor.executemany("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)",dataUsuario)
        
        ids = miCursor.lastrowid
        messagebox.showinfo("CRUD","Se creo el usuario correctamente\nEsta es su ID:"+ str(ids))
        #except:
        #      messagebox.showerror("CRUD","Un error ha ocurrido")

    def AccionLeer():
        global controlID 
        global textoID
        global valorID
        x = "'"+ valorID.get() + "'" 
        miCursor.execute("SELECT * FROM USUARIOS WHERE ID = MAX(ID)")
        datalectura=miCursor.fetchall()
        DevuelveLectura=(datalectura[0])
        messagebox.showinfo("",len(DevuelveLectura[0]))
        return
        try:
            if controlID == False:
                textoID.destroy()
                textoID = Entry(root,font =("Arial",10), state="normal", textvariable = valorID)
                textoID.grid(row=1,column=2,padx=10,pady=10)
                controlID = True
                messagebox.showinfo("CRUD","Introduce una ID")
            elif valorID.get()=="":
                messagebox.showerror("CRUD","Introduce una ID")
            else:
                miCursor.execute("SELECT * FROM USUARIOS WHERE ID = max(ID)")
                datalectura=miCursor.fetchall()
                DevuelveLectura=(datalectura[0])
                datosNombre.set(DevuelveLectura[1])
                datosPsword.set(DevuelveLectura[2])
                datosApellido.set(DevuelveLectura[3])
                datosDireccion.set(DevuelveLectura[4])
                textoComentario.insert(END, DevuelveLectura[5])
                textoID=Entry(root,font =("Arial",10), state="disabled", textvariable = valorID)
                messagebox.showinfo("",len(datalectura))
        except:
            messagebox.showerror("CRUD","Introdusca una ID válida")

    def AccionActualizar(deGuardar):
        x = "'"+ valorID.get() + "'" 
        if controlID == False:
            textoID.destroy()
            textoID = Entry(root,font =("Arial",10), state="normal", textvariable = valorID)
            textoID.grid(row=1,column=2,padx=10,pady=10)
            controlID = True
            messagebox.showinfo("CRUD","Introduce una ID y datos a actualizar")
        elif valorID.get()=="":
            messagebox.showerror("CRUD","Introduce una ID")
        elif deGuardar==True:
            if  datosNombre.get() == "" and datosPsword.get() == "" and datosApellido.get() == "" and datosDireccion.get() == "" and textoComentario.get(1.0,END) == "\n":
                messagebox.showwarning("CRUD","Introdusca un valor.\nSi se arrepiente, puede darle al boton de suscribirse, de cancelar.")
            else:
                try:
                    #print("'"+ textoComentario.get(1.0,END)+"'")
                    if datosNombre.get() != "":
                        miCursor.execute("UPDATE USUARIOS SET NOMBRE_USUARIO='"+datosNombre.get()+ "' WHERE ID=" + x)
                    if datosPsword.get() != "":
                        miCursor.execute("UPDATE USUARIOS SET CONTRASEÑA='"+datosPsword.get()+ "' WHERE ID=" + x)
                    if datosApellido.get() != "":
                        miCursor.execute("UPDATE USUARIOS SET APELLIDO='"+datosApellido.get()+ "' WHERE ID=" + x)
                    if datosDireccion.get() != "":
                        miCursor.execute("UPDATE USUARIOS SET DIRECCION='"+datosDireccion.get()+ "' WHERE ID=" + x)
                    if textoComentario.get(1.0,END) != "\n":
                        miCursor.execute("UPDATE USUARIOS SET COMENTARIO='"+textoComentario.get(1.0,END)+ "' WHERE ID=" + x)
                        messagebox.showinfo("CRUD","Se actualizaron los datos con éxito")
                        borra_campos()
                        afterBBDD()
                except:
                    messagebox.showerror("CRUD","Un error ha ocurrido")
        #miCursor.execute("UPDATE USUARIOS SET PRECIO=35 WHERE ID=1")
        #//                                 Tambien puede ser: NOMBRE_ARTICULO='pelota'

        def AccionBorrar():
            #simpledialog.TclError("CRUD",)
            answer = simpledialog.askinteger("CRUD", "Ingrese la ID a Borrar")
            if answer==None:
                messagebox.showerror("CRUD","No introdujo nada -_-")
            else:
                yesno = messagebox.askquestion("CRUD", "¿Estás seguro?")
                if yesno=="yes":
                    try:
                        miCursor.execute("DELETE FROM USUARIOS WHERE ID="+ "'"+ str(answer) +"'")
                        afterBBDD()
                        messagebox.showinfo("CRUD","Se borraron los datos con éxito")
                    except:
                        messagebox.showerror("CRUD","Un error ha ocurrido")

    def ocultar(tipo):
        global originales
        global controlID
        global textoID
        if tipo=="Actualizar" and originales==True:
            AccionActualizar(False)
            botonCrear.place_forget()
            botonLeer.place_forget()
            botonActualizar.place_forget()
            botonBorrar.place_forget()
            botonGuardar.place(x=75,y=370)
            botonCancelar.place(x=140,y=370)
            originales=False
        elif tipo=="Actualizar" and originales==False:
            textoID.destroy()
            textoID = Entry(root,font =("Arial",10), state="disabled", textvariable = valorID)
            textoID.grid(row=1,column=2,padx=10,pady=10)
            controlID=False
            botonCrear.place(x=10,y=370)
            botonLeer.place(x=75,y=370)
            botonActualizar.place(x=140,y=370)
            botonBorrar.place(x=210,y=370)
            botonGuardar.place_forget()
            botonCancelar.place_forget()
            originales=True
        elif tipo=="Leer" and originales==True:
            botonUltimo.place(x=190,y=370)
            botonSiguiente.place(x=160,y=370)
            botonAnterior.place(x=95,y=370)
            botonPrimero.place(x=65,y=370)
            botonX.place(x=128,y=370)
            AccionLeer()
            botonCrear.place_forget()
            botonLeer.place_forget()
            botonActualizar.place_forget()
            botonBorrar.place_forget()
            originales=False
        elif tipo=="Leer"and originales==False:
            botonCrear.place(x=10,y=370)
            botonLeer.place(x=75,y=370)
            botonActualizar.place(x=140,y=370)
            botonBorrar.place(x=210,y=370)
            global First
            global Indice
            First = False
            Indice=0
            botonUltimo.place_forget()
            botonSiguiente.place_forget()
            botonAnterior.place_forget()
            botonPrimero.place_forget()
            botonX.place_forget()
            originales=True
            borra_campos()
            valorID.set("")
    def Ultima_ID():
        global lastID
        global lenID
        global datalectura
        global DevuelveLectura
        miCursor.execute("SELECT * FROM USUARIOS")
        datalectura=miCursor.fetchall()
        lenID= len(datalectura) -1
        DevuelveLectura=(datalectura[lenID])
        lastID=DevuelveLectura[0]

    def The_ID():
        Ultima_ID()
        global TheIDs
        #O=0
        TheIDs=[]
        for O in range(lenID + 1):
            DevuelveLectura=(datalectura[O])
            TheIDs.append (DevuelveLectura[0])    

class Form2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def afterBBDD():
   try:
      miConexion.commit()
   except:
      print("")
   

def conectar():
   try:
      miConexion=sqlite3.connect("Usuarios.db")
      miCursor=miConexion.cursor()
   except:
        try:
            miCursor.execute("""CREATE TABLE USUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(20), 
                CONTRASEÑA VARCHAR(30),
                APELLIDO VARCHAR(20),
                DIRECCION VARCHAR(50),
                COMENTARIO VARCHAR(255)
                )""")
            messagebox.showinfo("CRUD","La base de datos se creo correctamente")
        except:
            pass




#<=========== M A I N ==========>#
root = tk.Tk()
app = Form1(root)
conectar()
root.mainloop()
#miConexion.close()