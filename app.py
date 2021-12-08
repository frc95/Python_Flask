from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

#MySql
import mysql.connector
midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba'
)

cursor = midb.cursor(dictionary=True) #Ahora retornamos diccionarios

#Routes
@app.route('/')
def index():
    return 'hole mundo'

@app.route('/post/<post_id>', methods=['GET', 'POST']) #'/post/int:<post_id>'
def post(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es otro metodo y no GET'

@app.route('/listar', methods=['POST', 'GET'])
def listar():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()

    #abort(403)

    #return redirect(url_for('post', post_id=2)) #indicamos el nombre de la funcion

    #print(request.form)
    #print(request.form['llave1'])
    #print(request.form['llave2'])
    #return 'listar'

    #return render_template('listar.html')

    #return {
        #"username": 'Franco',
        #"email": 'franco@gmail.com'
    #}

    return render_template('listar.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola mundo')

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']

        sql = "insert into Usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()

        return redirect(url_for('listar'))
        
    return render_template('crear.html')