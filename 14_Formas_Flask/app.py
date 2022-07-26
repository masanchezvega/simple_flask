#Importamos make_response
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

mascotas = [
    {"nombre": "Cala", "tipo": "Perro", "edad": 7},
    {"nombre": "Mita", "tipo": "Perro", "edad": 11},
    {"nombre": "Nara", "tipo": "Gato", "edad": 2},
    {"nombre": "Pleistoceno Hegel", "tipo": "Beta", "edad": 3},
]

# Flask puede devolver un resultado estructurado como HTML que 
# el browser sabe identificar y mostrar
@app.route("/")
def home():
    lista_nombres = [m["nombre"] for m in mascotas]
    last_seen = request.cookies.get('last_seen', '')
    return render_template("index.html", mascotas=lista_nombres, last_seen=last_seen)

@app.route("/mascota/<nombre>")
def nombres(nombre):
    mascota = {}
    for m in mascotas:
        if m["nombre"] == nombre:
            mascota = m
    found = ("nombre" in mascota)
    resp = make_response(render_template("landing.html", mascota=mascota, found=found))
    if found:
        resp.set_cookie('last_seen', mascota["nombre"])
    return resp

@app.route("/buscar", methods=["GET"])
def buscar_get():
    busqueda = request.args.get("nombre", "")
    return nombres(busqueda)

@app.route("/buscar", methods=["POST"])
def buscar_post():
    busqueda = request.form.get("nombre", "")
    return nombres(busqueda)

if __name__ == "__main__":
    app.run(debug=True)
