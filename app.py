from flask import Flask, request, template_rendered

app = Flask(__name__)

@app.route('/')
def index():
    return template_rendered('index.html')

@app.route('/SobreEad')
def SobreEad():
    return template_rendered('SobreEad.html')

@app.route('/Login')
def Login():
    return template_rendered('Login.html')

@app.route('/Cursos')
def Cursos():
    return template_rendered('Cursos.html')

@app.route('/Contato')
def Contato():
    return template_rendered('Contato.html')




if __name__ == '__main__':
    app.run(debug=True)