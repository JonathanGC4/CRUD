import collections


def create_json_biblioteca():
    titulo= input("Titulo: ")
    fecha_publicacion = input("Fecha de publicación: ")
    autor = ("Autor: ")
    nombre = input("Nombre: ")
    nacionalidad = input("Nacionalidad: ")
    categoria = input("Categoria: ")

    bibliotecas = {
        "titulo": titulo,
        "fecha_publicacion": fecha_publicacion,
        None: autor,
        "nombre": nombre,
        "nacionalidad": nacionalidad,
        "categoria": categoria
    }
    return bibliotecas


def create_json_update_biblioteca():
    print("Menu de opciones ")
    print("1. Modificar todo el documento")
    print("2. Modificar solo un elemento del documento")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        titulo = input("Titulo: ")
        fecha_publicacion = input("Fecha de publicación: ")
        autor = ("Autor: ")
        nombre = input("Nombre: ")
        nacionalidad = input("Nacionalidad: ")
        categoria = input("Categoria: ")

        bibliotecas = {
            "titulo": titulo,
            "fecha_publicacion": fecha_publicacion,
            None:autor,
            "nombre": nombre,
            "nacionalidad": nacionalidad,
            "categoria": categoria
        }
        return bibliotecas
    elif opcion == "2":
        indice = input("Ingrese el valor de indice a modificar: ")
        valor = input("Ingrese el valor a modificar")
        bibliotecas = {indice:valor}
        return bibliotecas

def eliminar_registro():
    id_registro = input("Ingrese el ID del registro que desea eliminar: ")
    query = {"_id": id_registro}
    resultado = collections.delete_one(query)
    if resultado.deleted_count == 1:
        print("El registro ha sido eliminado.")
    else:
        print("No se ha encontrado ningún registro con el ID especificado.")