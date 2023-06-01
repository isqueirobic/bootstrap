from flask import Flask, request, render_template, url_for, flash, redirect
from forms import formlogin
from forms import formNovoUsuario
import mysql.connector
from hashlib import sha256

app = Flask(__name__)
Mysql = mysql

app.config['SECRET_KEY'] = 'e97cd713cdda1b9b4b38804c0785716c016eb2cf0923f4'

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@$$w0rd',
    database = 'senac-ead'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SobreEad')
def SobreEad():
    return render_template('SobreEad.html')

@app.route('/Login')
def Login():
    FormLogin = formlogin()
    return render_template('Login.html', FormLogin=FormLogin)

@app.route('/Cursos')
def Cursos():
    return render_template('Cursos.html')

@app.route('/Contato')
def Contato():
    return render_template('Contato.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/Criarconta', methods=['get', 'post'])
def Criarconta():
    senha = request.form.get('senha')
    email = request.form.get('email')
    print(email)
    submitNovo = request.form.get('submitNovo')
    submitLogin = request.form.get('submitLogin')
    FormNovoUsuario = formNovoUsuario()
    FormLogin = formlogin()
    #print(submitNovo, submitLogin)
    if submitLogin == 'Login':
        pass
    if submitNovo == 'Criar conta':
        curso = mydb.cursor
        return redirect(url_for('index'))
    return render_template('Criarconta.html',  FormLogin=FormLogin, FormNovoUsuario=FormNovoUsuario)

if __name__ == '__main__':
    app.run(debug=True)