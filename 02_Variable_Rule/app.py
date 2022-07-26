from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Solicitud al endpoint 'index'")
    return "Hello world!"


# El endpoint recibe el parámetro <name> y lo pasa como variable
@app.route("/saluda/<name>")
def say_hi(name):
    print(f"Saludar a {name}")
    return f"¡Hola, {name}!"

# Un mismo endpoint puede recibir más de un parámetro
@app.route("/<lang>/saluda/<name>") ## lang = en, es, jp
def say_hi_lang(lang, name):
    print(f"Saludar a {name} en {lang}")
    if lang == 'jp':
        return f"Konnichiwa, {name}!"
    elif lang == 'en':
        return f"Hi, {name}!"
    else:
        return f"¡Hola, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
