import sqlite3
#import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#application_window = tk.Tk()

def Conectar():
   global Bloquear
   try:
      global miConexion
      miConexion=sqlite3.connect("Usuarios")
      global miCursor
      miCursor=miConexion.cursor()
   except:
      Bloquear = True
Conectar()

#GIT
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
controlID=False
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
   textoPsword=Entry(root,font =("Arial",10),show="*", textvariable = datosPsword)
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
   global textoComentario
   textoComentario=Text(root,font=("Arial",10), height=7, width=20)
   textoComentario.setvar(datosComentario)
   textoComentario.grid(row=6,column=2,padx=10,pady=10)
   textoComentario.insert(INSERT,datosComentario)
   scrollvert=Scrollbar(root,command=textoComentario.yview)
   scrollvert.grid(row=6,column=3,sticky="nsew")
   textoComentario.config(yscrollcommand=scrollvert.set)

###############################

def afterBBDD():
   try:
      miConexion.commit()
   except:
      print("")
   print("")
   

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
      Conectar()
      messagebox.showinfo("CRUD","La base de datos se creo correctamente")
   except:
      messagebox.showinfo("CRUD","La base de datos ya está creada")
   afterBBDD()

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

def AccionAgregar():
   #try:   
      dataUsuario=[
         (datosNombre.get(),datosPsword.get(),datosApellido.get(),datosDireccion.get(),textoComentario.get(1.0,END))
      ]
      lnombre=datosNombre.get()
      A=datosNombre.get()
      miCursor.executemany("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)",dataUsuario)
      afterBBDD()
      Ultima_ID()
      #ids = miCursor.lastrowid
      messagebox.showinfo("CRUD","Se creo el usuario correctamente\nEsta es su ID:"+ str(lastID))
   #except:
   #      messagebox.showerror("CRUD","Un error ha ocurrido")

def AccionLeer():
   global controlID 
   global textoID
   global valorID
   #valorID.set("1")
   x = "'"+ valorID.get() + "'" 
   try:
      """
      if controlID == False:
         
         textoID.destroy()
         textoID = Entry(root,font =("Arial",10), state="normal", textvariable = valorID)
         textoID.grid(row=1,column=2,padx=10,pady=10)
         controlID = True
         messagebox.showinfo("CRUD","Introduce una ID")
      elif valorID.get()=="":
         messagebox.showerror("CRUD","Introduce una ID")
      else:
      """
      borra_campos()
      miCursor.execute("SELECT * FROM USUARIOS WHERE ID ="+ x)
      datalectura=miCursor.fetchall()
      DevuelveLectura=(datalectura[0])
      datosNombre.set(DevuelveLectura[1])
      datosPsword.set(DevuelveLectura[2])
      datosApellido.set(DevuelveLectura[3])
      datosDireccion.set(DevuelveLectura[4])
      textoComentario.insert(END, DevuelveLectura[5])
      textoID=Entry(root,font =("Arial",10), state="disabled", textvariable = valorID)
   except:
      borra_campos()
      datosNombre.set("No existo :O")
      #messagebox.showerror("CRUD","Introdusca una ID válida")

def AccionActualizar(deGuardar):
   global controlID
   global textoID
   global valorID
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


#ValueError
###############################
originales = True
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

def Boton_Crear():
   global botonCrear
   botonCrear=Button(root, text="Crear", width=6, command=lambda:AccionAgregar())
   botonCrear.place(x=10,y=370)

def Boton_Leer():
   global botonLeer
   botonLeer=Button(root, text="Leer", width=6, command=lambda:ocultar("Leer"))
   botonLeer.place(x=75,y=370)

def Boton_Actualizar():
   global botonActualizar
   botonActualizar=Button(root, text="Actualizar", width=7, command=lambda:ocultar("Actualizar"))
   botonActualizar.place(x=140,y=370)

def Boton_Borrar():
   global botonBorrar
   botonBorrar=Button(root, text="Borrar", width=6, command=lambda:AccionBorrar())
   botonBorrar.place(x=210,y=370)

def Boton_Guardar():
   global botonGuardar
   botonGuardar=Button(root, text="Guardar", width=6, command=lambda:AccionActualizar(True)) 
   #botonGuardar.place_forget()
   #botonGuardar.place(x=75,y=370)
Boton_Guardar()

def Boton_Cancelar():
   global botonCancelar
   botonCancelar=Button(root, text="Cancelar", width=7,command=lambda:ocultar("Actualizar")) 
   #botonCancelar.place_forget()
   #botonCancelar.place(x=140,y=370)

First=False
Ya=False
Y4=False
Poraqui=False

def AccionSiguiente(Siguiente,Ultimo="No"):
   The_ID()
   global First
   global Cambio
   global Indice
   global Ya
   global Y4
   global Poraqui
   if Siguiente==True:
      Cambio=1
   else:
      Cambio=-1
   if First==False:
      Indice =0
      #Ultima_ID()
      #Indice= lastID
      First=True
   else:
      if Ultimo =="No":
         Indice= Indice + Cambio
      elif Ultimo =="True" or Ya ==True:
         if Ya ==True:
            Ya=False
            if Siguiente ==True:
               valorID.set(TheIDs[0])
            else:
               valorID.set(TheIDs[-2])
            Poraqui=True
         else:
            Ya=True
      elif Ultimo =="False" or Y4==True:
         if Y4 ==True:
            Y4=False
            if Siguiente ==True:
               valorID.set(TheIDs[1])
            else:
               valorID.set(TheIDs[-1])
            Poraqui=True
         else:
            Y4=True
   
   try:
      if Poraqui==False:
         valorID.set(TheIDs[Indice])
      else:
         Poraqui=False
   except IndexError:
      First=False
      AccionSiguiente(Siguiente)
      
   AccionLeer()

def AccionUltimo():
   The_ID()
   valorID.set(TheIDs[-1])
   AccionSiguiente="True"
   #First=False
   AccionLeer()

def AccionPrimero():
   The_ID()
   valorID.set(TheIDs[0])
   AccionSiguiente="False"
   #First=False
   AccionLeer()


Cambio= 0

def Boton_x():
   global botonX
   botonX=Button(root, text="X",command=lambda:ocultar("Leer")) 
   
def Boton_Siguiente():
   global botonSiguiente
   """imgSiguiente=PhotoImage(file= r"Siguiente.png")
   imgSiguiente=imgSiguiente.subsample(1,1)"""
   botonSiguiente=Button(root,text=">",command=lambda:AccionSiguiente(True))#image=imgSiguiente,compound = TOP)
   #botonSiguiente.place(x=140,y=370)

def Boton_Anterior():
   global botonAnterior
   botonAnterior=Button(root,text="<",command=lambda:AccionSiguiente(False))#image=imgSiguiente,compound = TOP)

def Boton_Ultimo():
   global botonUltimo
   botonUltimo=Button(root,text=">>",command=lambda:AccionUltimo())#image=imgSiguiente,compound = TOP)

def Boton_Primero():
   global botonPrimero
   botonPrimero=Button(root,text="<<",command=lambda:AccionPrimero())#image=imgSiguiente,compound = TOP)

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
   Crudmenu.add_command(label="Create",command=lambda:AccionAgregar())
   Crudmenu.add_command(label="Read",command=lambda:AccionLeer())
   Crudmenu.add_command(label="Update",command=lambda:ocultar("Actualizar"))
   Crudmenu.add_command(label="Delete",command=lambda:AccionBorrar())

   Ayudamenu=Menu(barraMenu,tearoff=0)
   barraMenu.add_cascade(label="Ayuda",menu=Ayudamenu)
   Ayudamenu.add_command(label="Acerca de...")
   Ayudamenu.add_command(label="Licencia")

def borra_campos():
   #valorID.set("")
   datosNombre.set("")
   datosPsword.set("")
   datosApellido.set("")
   datosDireccion.set("")
   textoComentario.delete(1.0,END)
   
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
   Boton_Guardar()
   Boton_Cancelar()
   Boton_Ultimo()
   Boton_Siguiente()
   Boton_Primero()
   Boton_Anterior()
   Boton_x()

funciones()

root.mainloop()
miConexion.close()