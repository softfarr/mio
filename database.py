import pymysql
def obtener_conexion():
    return pymysql.connect(
    host='localhost',
    user='root',
    password='$Root123',
    database='ussers'
)