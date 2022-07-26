from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Solicitud al endpoint 'index'")
    return "Hello world!"


# Un endpoint es una función Python y puede llamar a otras (como print) 
# tanto como necesario
@app.route("/suma/<a>/<b>")
def sumar(a, b):
    num_a = int(a)
    num_b = int(b)
    res = suma(num_a, num_b)
    return res

def suma(a,b):
    return a+b

if __name__ == "__main__":
    app.run(debug=True)
