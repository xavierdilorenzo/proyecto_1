import mysql.connector

# Conectar a la base de datos con usuario y contraseña
conn = mysql.connector.connect(
    host="192...",
    user="tu_usuario",
    password="tu_contraseña",
    database="grupo_1"
)

cursor = conn.cursor()

# Solicitar entrada de usuario para nombre y apellido
nombre = input("Ingresa el nombre: ")
apellido = input("Ingresa el apellido: ")

# Insertar los valores en la tabla "estudiantes"
cursor.execute('INSERT INTO estudiantes (nombre, apellido) VALUES (%s, %s)', (nombre, apellido))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos ingresados exitosamente.")
