#Importamos render_template
from flask import Flask, render_template

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
    return render_template("index.html", mascotas=lista_nombres)

@app.route("/mascota/<nombre>")
def nombres(nombre):
    mascota = {}
    for m in mascotas:
        if m["nombre"] == nombre:
            mascota = m
    found = ("nombre" in mascota)
    return render_template("landing.html", mascota=mascota, found=found)

if __name__ == "__main__":
    app.run(debug=True)
