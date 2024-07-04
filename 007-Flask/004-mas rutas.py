# pip install Flask
from flask import Flask

app = Flask(__name__)

cabecera = '''
    <h1>La web de Jose Vicente</h1>
    <a href="/">Inicio</a>
    <a href="/sobremi">Sobre mi</a>
    <a href="/contacto">Contacto</a>
'''

@app.route('/')
def inicio():
    contenido = '<p>Esta es la página de inicio</p>'
    return cabecera+contenido

@app.route('/sobremi')
def sobremi():
    contenido = '<p>Esta es la página de sobre mi</p>'
    return cabecera+contenido

@app.route('/contacto')
def contacto():
    contenido = '<p>Esta es la página de contacto</p>'
    return cabecera+contenido

if __name__ == '__main__':
    app.run(debug=True)
