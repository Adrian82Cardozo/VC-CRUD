


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

def Boton_Crear():
   global botonCrear
   botonCrear=Button(root, text="Crear", width=6, command=lambda:AccionAgregar())
   botonCrear.place(x=10,y=370)

def Boton_Leer():
   global botonLeer
   botonLeer=Button(root, text="Leer", width=6, command=lambda:AccionLeer())
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

def Boton_Cancelar():
   global botonCancelar
   botonCancelar=Button(root, text="Cancelar", width=7,command=lambda:ocultar("Actualizar")) 
   #botonCancelar.place_forget()
   #botonCancelar.place(x=140,y=370)

def Boton_Siguiente():
   global botonSiguiente
   imgSiguiente=PhotoImage(file= r"Siguiente.png")
   imgSiguiente=imgSiguiente.subsample(1,1)
   botonSiguiente=Button(root,text=">" )#image=imgSiguiente,compound = TOP)
   #botonSiguiente.place(x=140,y=370)

