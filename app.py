from flask import Flask, render_template, request, redirect, url_for
import os
from database import obtener_conexion 

#template_dir = (os.path.dirname(os.path.abspath.dirname(__file__)))
#template_dir = os.path.join(template_dir,'src', 'templates')

app= Flask (__name__)

@app.route('/')
def home():
    try: 
        conexion = obtener_conexion ()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ussers")
        myresult = cursor.fetchall()
        insertObject =[]
        columnNames =[column[0] for column in cursor.description]
        for record in myresult:
            #print(record)
            insertObject.append(dict(zip(columnNames, record)))
        #print ("columnNames=====", columnNames)
        #print ("insertObject=====", insertObject )
        cursor.close()
        return render_template('index.html', data=insertObject)
    except Exception as e: 
        return str(e)
    
'''
@app.route('/agregar_usuario')
def formulario_registro():
    return render_template("registro.html")

@app.route('/usser', methods=['POST'])
def addUser():
    identt=request.form['identt']
    name=request.form['name']
    lasname=request.form['lasname']
    email=request.form['email']
    nacionalidad=request.form['nacionalidad']
    contrasena=request.form['contrasena']

    if identt and name and lasname and email and nacionalidad and contrasena:
        cursor = db.database.cursor()
        sql = "INSERT INTO ussers (identt, name, apellido, email, nacionalidad, contraseña) VALUES (%s, %s, %s, %s, %s, %s)"
        data= (identt, name, lasname, email, nacionalidad, contrasena)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE identt= %s"
    data= (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    identt=request.form['identt']
    name=request.form['name']
    lasname=request.form['lasname']
    email=request.form['email']
    nacionalidad=request.form['nacionalidad']
    contrasena=request.form['contrasena']

    if identt and name and lasname and email and nacionalidad and contrasena:
        cursor = db.database.cursor()
        sql = "UPDATE users SET identt= %s, name =%s, apellido=%s, email=%s, nacionalidad=%s, contraseña=%s WHERE id =%s"
        data= (identt, name, lasname, email, nacionalidad, contrasena, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/editarinf/<int:id>')
def editarinf(id):
    #editarinf=controlador.optenerPorid (id)
    return render_template("editarinf.html")

'''
if __name__=='__main__':
    app.run(debug=True, port=8080)