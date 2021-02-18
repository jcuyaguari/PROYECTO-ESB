from flask import request, render_template
import requests
import urllib.request
import os

from flask import Flask

app = Flask(__name__)
DAT = {'tipo': 2, 'id_usr': 5, "raza": "boxer"}


# DAT = {}

"""
Este metodo nos permite controlar los errores
devolviendonos un diccionario  json con el mensaje.
"""
@app.route('/error')
def error():
    return {"error": "error"}

"""
Obtiene los datos para prueba
"""
@app.route('/get_datos')
def get_datos():
    return DAT

"""
Metodo que nos permite renderizar el index
la vista donde estamos mostrando la informacion. 
"""
@app.route('/')
def home():
    return render_template("index.html")

"""
Recuperamos la imagen desde la url
y mandamos a guardar en el directorio del proyecto.
"""
@app.route('/guardarimagen', methods=['POST'])
def guardar_imagen():
    url = request.json['url']
    # url = "https://images.dog.ceo/breeds/labrador/n02099712_3776.jpg"
    urllib.request.urlretrieve(url, "static/img/perro.jpg")
    return {'path': os.path.abspath("static/img/perro.jpg")}

"""
Enviamos los datos recuperados, a que se renderizen
en la pagina index html, y le pasamos un conjunto
de datos  a la url.
"""
@app.route('/sendDatos', methods=['POST'])
def sendDatos():
    if request.method == 'POST':
        id_usr = request.form['id_usr']
        raza = request.form['raza']
        dat = {'tipo': 1, 'id_usr': id_usr, "raza": raza}
        DAT.update(dat)
        url = "http://localhost:8081"
        r = requests.get(url=url, params=dat)

        js = r.json()
        print(js)
        if js['estado']:
            return render_template("index.html", datos=js)
    return render_template("error.html")

"""
Obtenemos los productos, donde existe la
cantidad, precio y stock disponible.
"""
@app.route('/getProductos', methods=['POST'])
def getProductos():
    if request.method == 'POST':
        cant1 = request.form['cant1']
        cant2 = request.form['cant2']
        stock = request.form['stock']
        dat = {'tipo': 2, 'cant1': cant1, "cant2": cant2, "stock": stock}
        DAT.update(dat)
        url = "http://localhost:8081"
        r = requests.get(url=url)
        js = r.json()
        lista = []
        list_id = list(js.keys())
        for i in list_id:
            lista.append([js[str(i)]['id'], js[str(i)]['nombre'], js[str(i)]['precio'], js[str(i)]['stock']])
        print(js)
        print(lista)
        return render_template("index.html", lista=lista)
