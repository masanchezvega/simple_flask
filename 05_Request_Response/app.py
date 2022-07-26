from flask import Flask, request

app = Flask(__name__)

# El objeto que trae la información de la solicitud es 'request'
@app.route("/")
def home():
    print(request)
    print(request.headers)
    print(request.base_url)
    print(request.args)
    print(request.form)
    return "Hello world!"


if __name__ == "__main__":
    app.run(debug=True)
