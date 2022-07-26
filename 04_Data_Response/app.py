# importamos jsonify
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    print("Solicitud al endpoint 'index'")
    return "Hello world!"


mascotas = [
    {"nombre": "Cala", "tipo": "Perro", "edad": 7},
    {"nombre": "Mita", "tipo": "Perro", "edad": 11},
    {"nombre": "Nara", "tipo": "Gato", "edad": 2},
    {"nombre": "Pleistoceno Hegel", "tipo": "Beta", "edad": 3},
]

# Un endpoint puede retornar una estructura de datos, solo hay que
# prepararla para que viaje como objeto serializable. El formato usual
# es JSON
@app.route("/mascotas")
def todas():
    return jsonify(mascotas)

@app.route("/nombres")
def nombres():
    lista_nombres = [m["nombre"] for m in mascotas]
    return jsonify(lista_nombres)

@app.route("/mascota/<nombre>")
def nombres(nombre):
    mascota = {}
    for m in mascotas:
        if m["nombre"] == nombre:
            mascota = m
    return jsonify(mascota)


if __name__ == "__main__":
    app.run(debug=True)
