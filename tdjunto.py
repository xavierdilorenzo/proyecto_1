import pymysql

def id_existe(cursor, id, tabla):
    cursor.execute(f"SELECT COUNT(id) FROM {tabla} WHERE id = %s", (id,))
    count = cursor.fetchone()[0]
    return count > 0

def crear_estudiante(cursor):

    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        listar_cursos(cursor)
        id_curso = int(input("Ingrese el ID del curso: "))
    
        cursor.execute("INSERT INTO estudiante (nombre, apellido, id_curso) VALUES (%s, %s, %s)",
                    (nombre, apellido, id_curso))
        print("Estudiante creado con éxito!")
    except pymysql.IntegrityError as e:
        print("Seleccione una opcion valida")
        crear_estudiante(cursor)



def listar_estudiantes(cursor):
    cursor.execute("""
        SELECT e.id, e.nombre, e.apellido, c.nombre
        FROM estudiante e
        JOIN curso c ON e.id_curso = c.id
    """)
    estudiantes = cursor.fetchall()
    
    for estudiante in estudiantes:
        print(estudiante)

def actualizar_estudiante(cursor):
    try:
        id_estudiante = int(input("Ingrese el ID del estudiante a actualizar: "))
        if not id_existe(cursor, id_estudiante, "estudiante"):
            print("ID de estudiante no existe")
            actualizar_estudiante(cursor)
            return
        nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del estudiante: ")
        nuevo_id_curso = int(input("Ingrese el nuevo ID del curso (1-6): "))
    
        cursor.execute("UPDATE estudiante SET nombre = %s, apellido = %s, id_curso = %s WHERE id = %s",
                       (nuevo_nombre, nuevo_apellido, nuevo_id_curso, id_estudiante))
        print("Estudiante actualizado con éxito!")
    except ValueError:
        print("Ingrese un ID válido")
        actualizar_estudiante(cursor)
    except pymysql.IntegrityError as e:
        print("Datos invalidos")
        actualizar_estudiante(cursor)

def borrar_estudiante(cursor):
    try:
        id_estudiante = int(input("Ingrese el ID del estudiante a borrar: "))
        if not id_existe(cursor, id_estudiante, "estudiante"):
            print("ID de estudiante no existe")
            actualizar_estudiante(cursor)
            return
        cursor.execute("DELETE FROM estudiante WHERE id = %s", (id_estudiante,))
        print("Estudiante eliminado con éxito!")
    except ValueError:
        print("Ingrese un ID válido")
        borrar_estudiante(cursor)
    except pymysql.IntegrityError as e:
        print("Datos inválidos")
        borrar_estudiante(cursor)

def buscar_curso_por_estudiante(cursor):
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
    
        cursor.execute("""
        SELECT c.nombre
        FROM estudiante e
        JOIN curso c ON e.id_curso = c.id
        WHERE e.nombre = %s AND e.apellido = %s
        """, (nombre, apellido))
    
        curso = cursor.fetchone()
        if curso:
            print(f"El estudiante {nombre} {apellido} está en el curso {curso[0]}")
        else:
            print("No se encontró al estudiante o el estudiante no está asignado a ningún curso.")
    except pymysql.IntegrityError as e:
        print("Datos invalidos")
        buscar_curso_por_estudiante(cursor)



def crear_curso(cursor):
    nombre_curso = input("Ingrese el nombre del nuevo curso: ")
    cursor.execute("INSERT INTO curso (nombre) VALUES (%s)", (nombre_curso,))
    print("Curso creado con éxito!")

def listar_cursos(cursor):
    cursor.execute("SELECT * FROM curso")
    cursos = cursor.fetchall()
    
    for curso in cursos:
        print(curso)

def actualizar_curso(cursor):
    try:
        id_curso = int(input("Ingrese el ID del curso a actualizar: "))
        if not id_existe(cursor, id_curso, "curso"):
            print("ID de curso no existe")
            actualizar_curso(cursor)
            return
        nuevo_nombre_curso = input("Ingrese el nuevo nombre del curso: ")
    
        cursor.execute("UPDATE curso SET nombre = %s WHERE id = %s", (nuevo_nombre_curso, id_curso))
        print("Curso actualizado con éxito!")
    except ValueError:
        print("Ingrese un ID válido")
        actualizar_curso(cursor)
    except pymysql.IntegrityError as e:
        print("Datos inválidos")
        actualizar_curso(cursor)



def borrar_curso(cursor):
    id_curso = int(input("Ingrese el ID del curso a borrar: "))
    
    try:
        cursor.execute("DELETE FROM curso WHERE id = %s", (id_curso,))
        print("Curso eliminado con éxito!")
    except pymysql.IntegrityError as e:
        print("No se puede borrar el curso porque hay estudiantes asignados a él. Primero, cambie a los estudiantes de curso.")

def main():
    conexion = pymysql.connect(
        host='192.168.40.254',
        user='sextocal',
        password='123456',
        database='grupo_1'
    )
    cursor = conexion.cursor()

    while True:
        print("----- Menú -----")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Borrar estudiante")
        print("5. Buscar curso por estudiante")
        print("6. Crear curso")
        print("7. Listar cursos")
        print("8. Actualizar curso")
        print("9. Borrar curso")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_estudiante(cursor)
        elif opcion == "2":
            listar_estudiantes(cursor)
        elif opcion == "3":
            actualizar_estudiante(cursor)
        elif opcion == "4":
            borrar_estudiante(cursor)
        elif opcion == "5":
            buscar_curso_por_estudiante(cursor)
        elif opcion == "6":
            crear_curso(cursor)
        elif opcion == "7":
            listar_cursos(cursor)
        elif opcion == "8":
            actualizar_curso(cursor)
        elif opcion == "9":
            borrar_curso(cursor)
        elif opcion == "10":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        conexion.commit()

    conexion.close()

if __name__ == "__main__":
    main()
