from tkinter import *
from tkinter import ttk as ttk

#ventana principal  
root = Tk()
root.title("Login Usuario")

#mainFrame, contenido  
mainFrame = Frame(root)
mainFrame.pack()
mainFrame.config(width=480, height=320)# bg="lightblue")

#etiqueta
titulo = Label (mainFrame, text="Login de Usuario con Python", font=("Arial",24))
titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

#Elementos de interfaz, textos y titulos
nombreLabel = Label(mainFrame, text="Nombre: ")
nombreLabel.grid(column=0, row=1)

passLabel = Label(mainFrame, text="Contraseña: ")
passLabel.grid(column=0, row=2)

#Entradas de textos
nombreUsuario = StringVar()
nombreUsuario.set("Carlos")
nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
nombreEntry.grid(column=1, row=1)

contraUsuario = StringVar()
contraUsuario.set("1234")
contraEntry = Entry(mainFrame, textvariable=contraUsuario, show="*")
contraEntry.grid(column=1, row=2)

#botones 
iniciarSesionButton = ttk.Button(mainFrame, text="Iniciar sesion")
iniciarSesionButton.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)

registrarButton = ttk.Button(mainFrame, text="Registrar")
registrarButton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

root.mainloop()
