import sqlite3
from tkinter import *
from tkinter import messagebox

miConexion=sqlite3.Connection



root=Tk()
root.title("CRUD")
barraMenu=Menu(root)
root.config(menu=barraMenu)
root.geometry("270x400")


###############################
def Salir():
   valor=messagebox.askyesno("Salir", "¿Deseas salir de la aplicación?")
   if valor==True:
      root.destroy()


###############################
def Label_ID():

    labelID=Label(root,font =("Arial",10), text = "ID")
    labelID.grid(row=1,column=1,padx=10,pady=10)
    #labelID.config(background="black",fg="light blue", justify="right")

valorID=StringVar()
textoID=Entry(root,font =("Arial",10), state="disabled", textvariable = valorID)
textoID.grid(row=1,column=2,padx=10,pady=10)
#textoID.config(background="black",fg="light blue", justify="right")
###############################
def Label_Nombre():

   labelNombre=Label(root,font =("Arial",10), text = "Nombre")
   labelNombre.grid(row=2,column=1,padx=10,pady=10)

datosNombre=StringVar()
def Texto_Nombre():
   textoNombre=Entry(root,font =("Arial",10), textvariable = datosNombre)
   textoNombre.grid(row=2,column=2,padx=10,pady=10)
###############################
def Label_Psword():

    labelPsword=Label(root,font =("Arial",10), text = "Contraseña")
    labelPsword.grid(row=3,column=1,padx=10,pady=10)

datosPsword=StringVar()
def Texto_Psword():
   textoPsword=Entry(root,font =("Arial",10), textvariable = datosPsword)
   textoPsword.grid(row=3,column=2,padx=10,pady=10)
###############################
def Label_Apellido():

    labelApellido=Label(root,font =("Arial",10), text = "Apellido")
    labelApellido.grid(row=4,column=1,padx=10,pady=10)

datosApellido=StringVar()
def Texto_Apellido():
   textoApellido=Entry(root,font =("Arial",10), textvariable = datosApellido)
   textoApellido.grid(row=4,column=2,padx=10,pady=10)
###############################
def Label_Direccion():

    labelDireccion=Label(root,font =("Arial",10), text = "Direccion")
    labelDireccion.grid(row=5,column=1,padx=10,pady=10)

datosDireccion=StringVar()
def Texto_Direccion():
   textoDireccion=Entry(root,font =("Arial",10), textvariable = datosDireccion)
   textoDireccion.grid(row=5,column=2,padx=10,pady=10)
###############################
def Label_Comentario():

    labelComentario=Label(root,font =("Arial",10), text = "Comentario")
    labelComentario.grid(row=6,column=1,padx=10,pady=10)

datosComentario=StringVar()
datosComentario=""
def Texto_Comentario():
   textoComentario=Text(root,font=("Arial",10), height=7, width=20)
   textoComentario.grid(row=6,column=2,padx=10,pady=10)
   textoComentario.insert(INSERT,datosComentario)
###############################

def afterBBDD():
   miConexion.commit()
   miConexion.close()

def AccionCrear():
   miConexion=sqlite3.connect("Usuarios")
   miCursor=miConexion.cursor()
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
      messagebox.showinfo("CRUD","La base de datos ya está creada")
   afterBBDD()

def AccionAgregar():
   dataUsuario[
      (datosNombre.get(),datosPsword.get(),datosApellido.get(),datosDireccion.get(),datosComentario.gett())
   ]
   miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?,?,?)",dataUsuario)

def AccionLeer():
   if textoID == Entry(root,font =("Arial",10), state="disabled", textvariable = valorID):
      textoID = Entry(root,font =("Arial",10), state="enabled", textvariable = valorID)
   elif valorID.get()=="":
      messagebox.showerror("CRUD","Introduce una ID")
   else:
      try:
         miCursor.execute("SELECT * FROM PRODUCTOS WHERE ID =",valorID)
         dataUsuario=miCursor.fetchall()
         textoID=Entry(root,font =("Arial",10), state="disabled", textvariable = valorID)
      except:
         messagebox.showerror("CRUD","Introdusca una ID válida")

#ValueError
###############################
def Boton_Crear():
   botonCrear=Button(root, text="Crear", width=6, command=lambda:numeroPulsado("7"))
   botonCrear.place(x=10,y=370)

def Boton_Leer():
   botonLeer=Button(root, text="Leer", width=6, command=lambda:numeroPulsado("7"))
   botonLeer.place(x=75,y=370)

def Boton_Actualizar():
   botonActualizar=Button(root, text="Actualizar", width=7, command=lambda:numeroPulsado("7"))
   botonActualizar.place(x=140,y=370)

def Boton_Borrar():
   botonBorrar=Button(root, text="Borrar", width=6, command=lambda:numeroPulsado("7"))
   botonBorrar.place(x=210,y=370)
###############################

def El_menu():
   bbddmenu=Menu(barraMenu,tearoff=0)
   barraMenu.add_cascade(label="BBDD", menu = bbddmenu)
   bbddmenu.add_command(label="Conectar",command=lambda:AccionCrear())
   bbddmenu.add_command(label="Salir",command=lambda:Salir())
   
   borramenu=Menu(barraMenu,tearoff=0)
   barraMenu.add_cascade(label="Borrar",menu=borramenu)
   borramenu.add_command(label="Borrar campos",command=lambda:borra_campos())

   Crudmenu=Menu(barraMenu,tearoff=0)
   barraMenu.add_cascade(label="CRUD",menu=Crudmenu)
   Crudmenu.add_command(label="Create")
   Crudmenu.add_command(label="Read")
   Crudmenu.add_command(label="Update")
   Crudmenu.add_command(label="Delete")

   Ayudamenu=Menu(barraMenu,tearoff=0)
   barraMenu.add_cascade(label="Ayuda",menu=Ayudamenu)
   Ayudamenu.add_command(label="Acerca de...")
   Ayudamenu.add_command(label="Licencia")

def borra_campos():
   valorID.set("")
   datosNombre.set("")
   datosPsword.set("")
   datosApellido.set("")
   datosDireccion.set("")
   datosComentario.set("")

def funciones():
   El_menu()
   Label_ID()
   #Texto_ID()
   Label_Nombre()
   Texto_Nombre()
   Label_Psword()
   Texto_Psword()
   Label_Apellido()
   Texto_Apellido()
   Label_Direccion()
   Texto_Direccion()
   Label_Comentario()
   Texto_Comentario()
   Boton_Crear()
   Boton_Leer()
   Boton_Actualizar()
   Boton_Borrar()

funciones()




root.mainloop()