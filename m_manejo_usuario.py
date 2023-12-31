import json
import presentacion


def pedir_datos_login():
    print("               **************")
    print("                   LOGIN")
    print("               **************")
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    return usuario, password

#Verifico si el usuario existe en arcihvo user.json
def usuario_existe(nombre_usuario):
    usuarioValido = False
    with open('user.json','r') as dataUser:
        usuarios = json.load(dataUser)

    for usuario in usuarios:
        if usuario["user"] == nombre_usuario:
            usuarioValido = True
            break

    return usuarioValido

def crear_usuario(usuario,contraseña):
    usuarioValido = usuario_existe(usuario)
    if usuarioValido:
        print("INTENTE USAR OTRO USUARIO, ESTE NO ESTA DISPONIBLE")
        return False
    else:
            nuevoUsuario = {
                            "user": usuario,
                            "password": contraseña
                            }
            try:
                #lee y obtengo la lista de usuarios
                with open("user.json", "r", encoding="utf-8") as dataUser:
                    lista_usuarios = json.load(dataUser)
                
            
                #addiciono el nuevo usuario a la lista de usuarios
                lista_usuarios.append(nuevoUsuario)
                #actualizo el archivo user.json
                with open("user.json", "w", encoding="utf-8") as dataUser:
                    json.dump(lista_usuarios, dataUser)
                print("**************")
                print("USUARIO CREADO CON EXITO")
                print("**************")
                if (presentacion.continuar_presentacion()!=True):
                    exit()
                else:
                    presentacion.limpiar_consola()
                    return True
            except Exception as e:
                print("Error al registrar usuario" , str(e))

#Verifica si el usuario y contraseña ingresados son correctos
def control_usuario(usuario, contraseña):
    usuario_valido = False
    with open('user.json') as lista_usuario:
        lst_usuarios = json.load(lista_usuario)
    for usr in lst_usuarios:
        if usr["user"] == usuario and usr["password"] == contraseña:
            usuario_valido = True
            break
    return usuario_valido

def bienvenida(usuario):
    
    print("**************")
    print("BIENVENIDO ", usuario.upper())
    print("**************")

def tipo_usuario(usuario,contraseña):
    if usuario == "admin" and contraseña == "admin":
        return True
    else:
        return False