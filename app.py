from flask import Flask, request, render_template
from forms import formlogin
from forms import formNovoUsuario

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e97cd713cdda1b9b4b38804c0785716c016eb2cf0923f4'

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
    FormNovoUsuario = formNovoUsuario()
    FormLogin = formlogin()
    return render_template('Criarconta.html',  FormLogin=FormLogin, FormNovoUsuario=FormNovoUsuario)

if __name__ == '__main__':
    app.run(debug=True)