#Importamos render_template
from flask import Flask, render_template

app = Flask(__name__)

# Flask puede devolver un resultado estructurado como HTML que 
# el browser sabe identificar y mostrar
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/autor/<nombre>")
def autor(nombre):
    return render_template("landing.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)
