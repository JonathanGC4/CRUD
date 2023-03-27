from crud import *
from basic_functions import *

while True:
    print("Menu de opciones")
    print("1. Ver todos los registros")
    print("2. Buscar un registro")
    print("3. Agregar Registro")
    print("4. Modificar Registro")
    print("5. Eliminar Registro")
    print("6. Salir de sistema")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        read_biblioteca()
    elif opcion == "2":
        id = int(input("Ingrese el id del registro a buscar: "))
        read_biblioteca(id)
    elif opcion == "3":
        biblioteca= create_json_biblioteca()
        create_biblioteca(biblioteca)
    elif opcion == "4":
        id = int(input("Ingrese el id del registro a modificar: "))
        biblioteca= create_json_update_biblioteca()
        update_biblioteca(id,biblioteca)
    elif opcion == "5":
        id = int(input("Ingrese el id de registro a eliminar: "))

        if biblioteca.deleted_count == 1:
            print("El registro ha sido eliminado.")
        else:
            print("No se ha encontrado ningún registro con el ID especificado.")


    elif opcion == "6":
        print("Saliendo del sistema")
        break
