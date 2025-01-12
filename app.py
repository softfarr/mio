from flask import Flask, render_template, request, redirect, url_for
import os
from database import obtener_conexion 

def insertar_usuario(nombre, apellido, correo, nacionalidad, password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO ussers(nombre, apellido, correo, nacionalidad, password) VALUES (%s, %s, %s, %s, %s)",
                        (nombre, apellido, correo, nacionalidad, password))
        conexion.commit()
        conexion.close()
    except Exception as e: 
        print(str(e))


def obtener_usuarios():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellido, correo, nacionalidad, password FROM ussers")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def eliminar_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM ussers WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, apellido, correo, nacionalidad, password FROM ussers WHERE id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_usuario(nombre, apellido, correo, nacionalidad, password, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE ussers SET nombre = %s, apellido = %s, correo = %s , nacionalidad = %s, password = %s WHERE id = %s",
                       (nombre, apellido, correo, nacionalidad, password, id))
    conexion.commit()
    conexion.close()

app= Flask (__name__)

@app.route('/')
def home():
    usuarios = obtener_usuarios()
    return render_template("index.html", usuarios=usuarios)
    
@app.route('/agregar_usuario')
def mostrar_form_agregar_usuario():
    return render_template("agregar_usuario.html")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    nacionalidad = request.form["nacionalidad"]
    password = request.form["password"]
    insertar_usuario(nombre, apellido, correo, nacionalidad, password)
    return redirect(url_for("home"))

@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usrio():
    eliminar_usuario(request.form["id"])
    return redirect(url_for("home"))

@app.route('/editar_usuario/<string:id>', methods=['GET', 'POST'])
def mostrar_form_editar_usuario(id):
    usuario = obtener_usuario_por_id(id)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/actualizar_usuario", methods=["POST"])
def validar_actualizar_usuario():
    id = request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    nacionalidad = request.form["nacionalidad"]
    password = request.form["password"]
    actualizar_usuario(nombre, apellido, correo, nacionalidad, password, id)
    return redirect("/")


if __name__=='__main__':
    #app.run(debug=True, port=8080)
    app.run(debug=True, port=4321)