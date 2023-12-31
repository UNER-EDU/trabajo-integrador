import json
import presentacion

def Obtener_Lista_Comidas():
    try:
        #lee y obtengo la lista de comidas rapidas 
        with open("comidas_rapidas.json", "r", encoding="utf-8") as dataComidas:
            lista_comidas = json.load(dataComidas)

        return lista_comidas
    except Exception as e:
        print("Error al obtener lista de comidas" , str(e))

def mostrar_lista_comidas(lista):
    presentacion.limpiar_consola()
    for comida in lista:
        print("ID:", comida['id'])
        print("Descripción:", comida['descripcion'])
        print("Ingredientes:", "-".join(comida['ingredientes']))
        print("Tiempo:", comida['tiempo'])
        print("Precio:", comida['precio'])
        print("Calorías:", comida['calorias'])
        print("Vegana:", comida['vegana'])
        print("--------------------")

def Mostrar_Comidas_Abreviadas(lista):
    print("BREVES DESCRIPCION DE LAS COMIDAS DISPONIBLES A ELIGIR:")

    for comida in lista:
        print("*------------------------*")
        print("ID:", comida['id'], "- Descripción:", comida['descripcion'].upper(), "- Precio:", comida['precio'])
        
        #print("Descripción:", comida['descripcion']) 
       

def Buscar_Comida(lista):
    print("Opciones de búsqueda:")
    print("1. Buscar por ingrediente.")
    print("2. Buscar por precio.")
    print("3. Buscar por calorías.")
    print("4. Mostrar comidas veganas disponibles.")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        ingrediente = input("Ingrese el ingrediente a buscar: ")
        presentacion.limpiar_consola()
        Buscar_por_Ingredientes(lista, ingrediente)        
    elif opcion == "2":
        precio_max = float(input("Ingrese un rango de precio (Max): "))
        precio_min= float(input("Ingrese un rango de precio (Min): "))
        presentacion.limpiar_consola()
        buscar_por_precio(lista, precio_max,precio_min)
    elif opcion == "3":
        calorias_max = int(input("Ingrese las calorías máximas: "))
        calorias_min = int(input("Ingrese las calorías min: "))
        presentacion.limpiar_consola()
        buscar_por_calorias(lista,calorias_max,calorias_min)
    elif opcion=="4":
        presentacion.limpiar_consola()
        buscar_veganas(lista)

def Buscar_por_Ingredientes(lista, ingrediente):
    lista_comida_filtrada = []
   
    for comida in lista:
        ingredientes = comida['ingredientes']
        if ingrediente in ingredientes:
            lista_comida_filtrada.append(comida)
    
    presentacion.limpiar_consola()
    cant=len(lista_comida_filtrada)
    print("*------LISTA DE COMIDAS ENCONTRADAS CANT: " ,cant,"--------*")
    if lista_comida_filtrada:
        for comida in lista_comida_filtrada:
            print("ID:", comida['id'])
            print("Descripción:", comida['descripcion'])
            print("Ingredientes:", "-".join(comida['ingredientes']))
            print("Tiempo:", comida['tiempo'])
            print("Precio:", comida['precio'])
            print("Calorías:", comida['calorias'])
            print("Vegana:", comida['vegana'])
            print("--------------------")
    else:
        print("No se encontraron comidas que contengan ese ingrediente.")

def buscar_por_precio(lista, precio_max,precio_min):
    lista_comida_filtrada=[]
    for comida in lista:
        if precio_min <= comida['precio'] <= precio_max:
            lista_comida_filtrada.append(comida)

    if not lista_comida_filtrada:
        print("No se encontraron comidas en ese rango de precios.")
    else:
        print(f"*------LISTA DE COMIDAS POR RANGO DE PRECIOS {precio_min} Y {precio_max} -------*")
        for comida_filtrada in lista_comida_filtrada:
            print("ID:", comida_filtrada['id'])
            print("Descripción:", comida_filtrada['descripcion'])
            print("Ingredientes:", "-".join(comida['ingredientes']))
            print("")
            print("Tiempo:", comida_filtrada['tiempo'])
            print("Precio:", comida_filtrada['precio'])
            print("Calorías:", comida_filtrada['calorias'])
            print("Vegana:", comida_filtrada['vegana'])
            print("--------------------")
       
def buscar_por_calorias(lista,calorias_max,calorias_min):
    lista_comida_filtrada=[]
    for comida in lista:
        if calorias_min <= comida['calorias'] <= calorias_max:
            lista_comida_filtrada.append(comida)

    if not lista_comida_filtrada:
        print("No se encontraron comidas dentro de ese rango de calorias.")
    else:
        print(f"*------LISTA DE COMIDAS POR CALORIAS ENTRE {calorias_min} y {calorias_max}-------*")
        for comida_filtrada in lista_comida_filtrada:
            print("ID:", comida_filtrada['id'])
            print("Descripción:", comida_filtrada['descripcion'])
            print("Ingredientes:", "-".join(comida['ingredientes']))
            print("")
            print("Tiempo:", comida_filtrada['tiempo'])
            print("Precio:", comida_filtrada['precio'])
            print("Calorías:", comida_filtrada['calorias'])
            print("Vegana:", comida_filtrada['vegana'])
            print("--------------------")
def buscar_veganas(lista):
    lista_comida_filtrada=[]
    for comida in lista:
        if comida['vegana'] == "True":
            lista_comida_filtrada.append(comida)

    if not lista_comida_filtrada:
        print("No hay comidas veganas.")
    else:
        print("*------LISTA DE COMIDAS VEGANAS-------*")
        for comida_filtrada in lista_comida_filtrada:
            print("ID:", comida_filtrada['id'])
            print("Descripción:", comida_filtrada['descripcion'])
            print("Ingredientes:", "-".join(comida['ingredientes']))
            print("")
            print("Tiempo:", comida_filtrada['tiempo'])
            print("Precio:", comida_filtrada['precio'])
            print("Calorías:", comida_filtrada['calorias'])
            print("Vegana:", comida_filtrada['vegana'])
            print("--------------------")

def modificar_comida(lista):
    #Muestro toda las comidas
    mostrar_lista_comidas(lista)
    #pregunto que comida desea modificar
    id = int(input("Ingrese el ID de la comida a modificar: "))
    #La muestro
    for comida in lista:
        if comida['id'] == id:
            print("ID:", comida['id'])
            print("Descripción:", comida['descripcion'])
            print("Ingredientes:", "-".join(comida['ingredientes']))
            print("")
            print("Tiempo:", comida['tiempo'])
            print("Precio:", comida['precio'])
            print("Calorías:", comida['calorias'])
            print("Vegana:", comida['vegana'])
            print("--------------------")
            print("Ingrese los nuevos datos de la comida")
            descripcion = input("Ingrese la descripción: ")           
            tiempo = int(input("Ingrese el tiempo de preparación: "))
            comida['ingredientes'] = ingresar_ingredientes()
            precio = float(input("Ingrese el precio: "))
            calorias = int(input("Ingrese las calorías: "))
            vegana = input("Ingrese si es vegana (S/N): ")
            comida['descripcion'] = descripcion
            #los nuevos ingredientes se los paso desde una funcion por fuera
            comida['tiempo'] = tiempo
            comida['precio'] = precio
            comida['calorias'] = calorias
            #Control que si es Vengana guarde True y si no False
            if vegana=="S" or vegana=="s":
                comida['vegana'] = vegana == "True"
            else:
                comida['vegana'] = vegana == "False"
            break
    else:
        print("No se encontró la comida con el ID:", id)

    #actualizo el archivo user.json guarda do los cambios de la comida seleccionada
    with open("comidas_rapidas.json", "w", encoding="utf-8") as dataComidas:
        json.dump(lista, dataComidas)
    print("Comida modificada con éxito")
    if (presentacion.continuar_presentacion()!=True):
        exit()
    else:
        presentacion.limpiar_consola()

#funcion para agregar los ingredientes a la lista 
def ingresar_ingredientes():
    ingredientes = []
    while True:
        entrada = input("Ingrese un ingrediente ( n para terminar): ")
        if entrada.lower() == "N" or entrada.lower() == "n":
            break
        ingredientes.append(entrada)
    return ingredientes

def agregar_comida(lista):
    ingredientes = []
    # Pedir todos los datos de comida
    print("Se solicitarán todos los datos de la comida")
    descripcion = input("Ingrese la descripción: ")
    tiempo = int(input("Ingrese el tiempo (en minutos) de preparación: "))
    ingredientes = ingresar_ingredientes()
    precio = float(input("Ingrese el precio: "))
    calorias = int(input("Ingrese las calorías: "))
    vegana = input("Ingrese si es vegana (S/N): ")

    if vegana.lower() == "s":
        vegana = True
    else:
        vegana = False

    # Obtengo el último id de la lista y le sumo 1 para asignarle el nuevo id
    id = lista[-1]['id'] + 1
    if guardar_nueva_comida(lista,id,descripcion,ingredientes,tiempo,precio,calorias,vegana):
        menu_admin()
    

def guardar_nueva_comida(lista,id,descripcion,ingredientes,tiempo,precio,calorias,vegana):
    # Crear el nuevo objeto comida
    nueva_comida = {
        "id": id,
        "descripcion": descripcion,
        "ingredientes": ingredientes,
        "tiempo": tiempo,
        "precio": precio,
        "calorias": calorias,
        "vegana": vegana
    }
    lista.append(nueva_comida)   
    try:    
        # Actualizo el archivo comidas_rapidas.json guardando los cambios de la comida seleccionada
        with open("comidas_rapidas.json", "w", encoding="utf-8") as dataComidas:
            json.dump(lista, dataComidas)
        print("Comida Insertada")
    except Exception as e:
        print("Error al actualizar la lista de comida" , str(e))
    return True
    
import json

def Borrar(lista):
    comida_borrada = False
    id = int(input("Ingrese por ID la comida para eliminar: "))
    
    for comida in lista:
        if comida['id'] == id:
            lista.remove(comida)
            comida_borrada = True
            break
        
    if not comida_borrada:
        print("No existe comida con el ID ingresado")
    try:
        with open("comidas_rapidas.json", "w", encoding="utf-8") as dataComidas:
            json.dump(lista, dataComidas)
        print("Se eliminó la comida con éxito")
    except Exception as e:
        print("Error al borrar la comida seleccionada:", str(e))
    
    return True


def menu_admin():
    presentacion.limpiar_consola()
    opcion = -1  # Inicializamos la opción con un valor diferente de cero
    while opcion != 0:
        print("**************")
        print("MENU ADMIN")
        print("**************")
        print("1. Mostrar comidas rápidas")
        print("2. Buscar comida rápida")
        print("3. Modificar comida")
        print("4. Agregar comidas rápidas")
        print("5. Borrar comidas rápidas")
        print("0. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            lista=Obtener_Lista_Comidas()
            mostrar_lista_comidas(lista)
        elif opcion == 2:
            presentacion.limpiar_consola()
            lista=Obtener_Lista_Comidas()            
            mostrar_lista_comidas(lista)
            Buscar_Comida(lista)
        elif opcion == 3:
            lista=Obtener_Lista_Comidas()
            modificar_comida(lista)
        elif opcion == 4:
            lista=Obtener_Lista_Comidas()
            agregar_comida(lista)
        elif opcion == 5:
            lista=Obtener_Lista_Comidas()
            Borrar(lista)
        
    presentacion.limpiar_consola()
    presentacion.Presentacion()
    print("                 Gracias por usar la app")

   