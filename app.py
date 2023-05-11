from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SobreEad')
def SobreEad():
    return render_template('SobreEad.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

@app.route('/Cursos')
def Cursos():
    return render_template('Cursos.html')

@app.route('/Contato')
def Contato():
    return render_template('Contato.html')

@app.route('/base')
def base():
    return render_template('base.html')




if __name__ == '__main__':
    app.run(debug=True)