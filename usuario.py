from msilib import datasizemask

class usuario():
    
    numUsuario = 0

    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra

        self.conectado = False
        self.intentos = 3

        usuario.numUsuario+=1

    def conectar(self, contrasenia = None):
        if contrasenia==None:
            myContra = input ("Ingrese su contraseña: ")
        else:
            myContra=contrasenia
        if myContra==self.contra:
            print("Se ha conectado con exito!")
            self.conectado = True
            return True 
#password mala   
        else:
#se pierde 1 intento cada vez que se ingrese mal 
            self.intentos-=1
#si quedan intentos, mostrar mensajes y pedir dnvo credenciales
            if self.intentos > 0:
                print("Contraseña incorrecta, intentelo nuevamente...")
                if contrasenia!=None:
                    return False
                print("Intentos restantes:",self.intentos)
                self.conectar()
#si ya no tienes intentos, salir de app
            else:
                print("Error, no se pudo iniciar sesion...")
                print("Adios")

    def desconectar(self):
        if self.conectado:
            print("Se cerro sesion con exito!")
            self.conectado = False
        else:
            print("Error, no se ha iniciado sesion")
    
    def __str__(self):
        if self.conectado:
            conect = "Conectado"
        else:
            conect = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"

#despues de crear usuario, se muestra el estado
#user1 = usuario(input("Ingrese un nombre: "), input("Ingrese una contraseña: "))
#print(user1)

#estado conectado
#user1.conectar()
#print(user1)

#estado desconectado
#user1.desconectar()
#print(user1)
