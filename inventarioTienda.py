import os
inventario = []

#funcion de limpiar pantalla para mejorar la visualizacion del menu
def limpiar_pantalla():
    if os.name == "nt": #opcion para windows
        os.system("cls") #opcion para MacOs
    else:
        os.system("clear")
        #funcion para solicitar numero
def  solicitar_numero(mensaje, tipo_dato): #Solicitar numero al usuario
    while True:
        try:
            valor = tipo_dato(input(mensaje))
            if valor < 0:
                print("Error: El numero no puede ser negativo")
            else:
                return valor
        except ValueError:
            print("Error: Por favor ingrese numero valido")
def agregar_producto(): #permite agregar productos al inventario con nombre cantidad y precio
    print("\n-Agregar Producto-")

    nombre = input("Nombre del producto:").strip()
    if nombre == "":
        print("No puede estar vacio")
        return
    cantidad = solicitar_numero("cantidad:",int) #solicita numeros enteros 
    precio = solicitar_numero("precio:",float)
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}   #crea el diccionario para los productos del inventario

    inventario.append(producto) #Se añade el producto 
    print(f"{nombre} agregado exitosamente")
def ver_inventario():
     print("\n-Inventario-")
     if not inventario:
        print("El inventario esta vacio")
     else:
        print(f"{'Producto':<20} | {'Cantidad':<10} | {'Precio':<10}") #muestra los encabezado de la tabla y alinear los datos en las columnas
        print("-" * 46)
        for prod in inventario:
            print(f"{prod['nombre']:<20} | {prod['cantidad']:<10} | ${prod['precio']:.2f}")
def buscar_producto(): #busca los productos que estan en el inventario por nombre (sin destinguir mayusculas y minusculas)
        print("\n-Buscar Producto-")
        nombre_buscar = input("Ingrese el nombre del producto").strip()
        encontrado = False
        for prod in inventario:
            if prod["nombre"].lower() == nombre_buscar.lower(): #compara los nombres en minusculas para evitar errores
                print(f"Producto: {prod['nombre']}, Cantidad: {prod['cantidad']}, Precio: ${prod['precio']:.2f}")
                encontrado = True
                break #termina de buscar una vez que encuentra el producto
            if not encontrado:
                print("Producto no encontrado")
def eliminar_producto(): #elimina el producto del inventatio segun el nombre ingresado por el usuario
        print("\n-Eliminar Producto-")
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar:").strip()
        for i, prod in enumerate(inventario): #compara los nombre en minusculas para evitar errores
            if prod["nombre"].lower() == nombre_eliminar.lower(): #elimina el producto de la lista
                del inventario[i]
                print(f"{nombre_eliminar} eliminado exitosamente")
                return 
        print("Producto no encontrado")            
def menu_principal():
        while True:
            print("\n-- Menu Inventario --")
            print("1. Agregar Producto")
            print("2. Ver inventario")
            print("3. Buscar producto")
            print("4. Salir")
            opcion = input("Seleccione una opcion (1-4):").strip()
            if opcion == "1":
                agregar_producto()
            elif opcion == "2":
                ver_inventario()
            elif opcion == "3":
                buscar_producto()
            elif opcion == "4":
                print("Salir")
                break
            else:
                print("Por favor intente de nuevo")
            if opcion in ["1","2","3"]:
                input("Presione Enter para volver")
if __name__ == "__main__":
        menu_principal()
