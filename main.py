import os
import platform

from laboratorio_poo import (
    ProductoElectronico,
    ProductoAlimenticio,
    GestionProductos
)

def limpiar_pantalla():
    '''Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("------------------------------Sistema de Gestión de Productos------------------------------")
    print("1. Agregar Producto")
    print("2. Mostrar todos los Productos")
    print("3. Actualizar precio del Producto")
    print("4. Eliminar Producto")
    print("5. Buscar Producto")
    print("6. Salir")
    print("-------------------------------------------------------------------------------------------")

def agregar_producto(gestion):
    limpiar_pantalla()
    print("1. Agregar Producto Electronico")
    print("2. Agregar Producto Alimenticio")
    tipo_producto = input("Seleccione una opción: ")
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: $"))
        stock = int(input("Ingrese la cantidad de stock del producto: "))
        if tipo_producto == '1':
            garantia = int(input("Ingrese la cantidad de meses de garantía del producto: "))
            producto = ProductoElectronico(id_producto, nombre, descripcion, precio, stock, garantia)
        elif tipo_producto == '2':
            vencimiento = input ("Ingrese la fecha de vencimiento en formato dd-mm-aaaa: ")
            producto = ProductoAlimenticio(id_producto, nombre, descripcion, precio, stock, vencimiento)
        else:
            print ("Opción no válida.")
            return
        gestion.nuevo_producto(producto)
        input('Presione enter para continuar... ')
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado : {e}")

def buscar_producto(gestion):
    limpiar_pantalla()
    id_producto = input ("Ingrese el ID del producto que desea buscar: ")
    gestion.buscar_producto(id_producto)
    input("Presione enter para continuar... ")

def actualizar_precio(gestion):
    id_producto = input("Ingrese el ID del producto que desea actualizar su precio: ")
    precio = float(input("Ingrese el nuevo precio del producto: "))
    gestion.actualizar_precio(id_producto, precio)
    input("Presione enter para continuar... ")

def eliminar_producto(gestion):
    id_producto = input("Ingrese el ID del producto que desea eliminar: ")
    gestion.eliminar_producto(id_producto)
    input("Presione enter para continuar... ")

def mostrar_productos(gestion):
    limpiar_pantalla()
    try: 
        productos = gestion.mostrar_todos_los_productos()
        print("------------------------------Lista de todos los Productos------------------------------")
        for producto in productos:
            if isinstance(productos, ProductoAlimenticio):
                print(f"Producto Alimenticio: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock}, Vencimiento: {producto.vencimiento}. ")
            else:
                print(f"Producto Electronico: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock}, Garantía: {producto.garantia} meses.")
        print("----------------------------------------------------------------------------------------")
    except Exception as e:
        print(f"Error al mostrar todos los productos {e}")
    input("Presione enter para continuar... ")

if __name__ == "__main__":
    gestion_productos = GestionProductos()
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_producto(gestion_productos)
        elif opcion == '2':
            mostrar_productos(gestion_productos)
        elif opcion == '3':
            actualizar_precio(gestion_productos)
        elif opcion == '4':
            eliminar_producto(gestion_productos)
        elif opcion == '5':
            buscar_producto(gestion_productos)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print ("Opción no válida. Por favor, seleccione otra opción.")