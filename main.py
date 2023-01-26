###~~~~~~~~~~~~~~~~~~El siguiente porgrama deja agregar a cuantos alumnos sea a una base de datos, siempre y cuando este ya no este asociado en la misma y del mismo modo permite buscar a un alumno ya registrado.~~~~~~~~~~~~~~~~~~~~~~~~

import sqlite3
import sys

def agregar_alumno(id,nombre,apellido):
    
    num_id = int(id)
    id_fila = num_id + 1
        
    conn = sqlite3.connect('Alumnos.db', isolation_level = None)
    c = conn.cursor()
    
    query_buscar = f'SELECT * FROM info WHERE (Nombre = "{nombre}" AND Apellido = "{apellido}")'
    buscar = c.execute(query_buscar)
    coincidencia = buscar.fetchone()
    
    if coincidencia == None:
        query_agregar = f'INSERT INTO info VALUES({id_fila},"{nombre}","{apellido}")'
        c.execute(query_agregar)
        print('\nEl estudiante se agrego correctamente!\n')
    else:
        print('\nEl estudiante ya esta registrado\n')
    
    c.close()
    conn.close()

def buscar_alumno(estudiante):
    conn = sqlite3.connect('Alumnos.db', isolation_level = None)
    c = conn.cursor()
    
    query_buscar = f'SELECT * FROM info WHERE Nombre = "{estudiante}"'
    buscar = c.execute(query_buscar)
    coincidencia = buscar.fetchone()
    
    if coincidencia == None:
        print(f'\nNo hay ningún estudiante con el nombre {estudiante}\n')
    else:
        print(f'\nLos siguientes son los datos del estudiante: {coincidencia}\n')
    
    c.close()
    conn.close()

def main():

    conn = sqlite3.connect('Alumnos.db', isolation_level = None)
    c = conn.cursor()

    ####~~~~~~~~~~~~~~~~~~~~~~~~~~Creacion de la tabla~~~~~~~~~~~~~~~~~~~~~~~
    c.execute("""CREATE TABLE IF NOT EXISTS info(
            Id INTEGER PRIMARY KEY,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL
        )""" )

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Menú~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while True:
        
        print(
            "Base de datos de alumnos\n Opciones\n 1. Agregar estudiantes\n 2. Buscar estudiante\n 3. Salir"
        )
        
        opcion = int(input('Digite una opción: '))
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~Deja añadir cuantos estudiantes sea, a menos de que ya este registrado en la bd~~~~~~~~~~~~
        if opcion == 1:
            query_id = f'SELECT * FROM info WHERE Id = (SELECT MAX(Id) FROM info)'
            posicion = c.execute(query_id)
            id = posicion.fetchone()
            
            if id == None:
                nombre = input('Nombre del alumno: ')
                apellido = input('Apellido del alumno: ')
                agregar_alumno(0, nombre, apellido)
            else:
                nombre = input('Nombre del alumno: ')
                apellido = input('Apellido del alumno: ')
                agregar_alumno(id[0], nombre, apellido)
        elif opcion == 2:
            estudiante = input('Escriba el nombre del estudiante a buscar: ')
            buscar_alumno(estudiante)
        elif opcion == 3:
            sys.exit()
        else:
            print("\nSeleccione una opcion válida.\n")
            


if __name__ == '__main__':
    main()

