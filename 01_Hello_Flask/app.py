# 1. importar Flask
from flask import Flask

# 2. Crear la app, con el parametro '__name__'
app = Flask(__name__)


# 3. Definimos el 'index' y lo que hará
@app.route("/")
def home():
    print("Solicitud al endpoint 'index'")
    return "Hello world!"


# 4. Un segundo endpoint, de nombre about y URL /about
@app.route("/about")
def about():
    print("Solicitud al endpoint 'About'")
    return "Acerca de... Soy Flask!"

# 5. Boilerplate, necesario para que la app sepa cuando debe correr o no y cómo
# El parámetro debug=True nos simplica el proceso de debugging
if __name__ == "__main__":
    app.run(debug=True)
