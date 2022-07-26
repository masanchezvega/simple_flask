#Importamos render_template
from flask import Flask, render_template

app = Flask(__name__)

# Flask puede devolver un resultado estructurado como HTML que 
# el browser sabe identificar y mostrar
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/style")
def home():
    return render_template("index_estilo.html")

if __name__ == "__main__":
    app.run(debug=True)
