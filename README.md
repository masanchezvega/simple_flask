# Flask Simplificado

## 5 sesiones

1. Básicos modelo cliente-servidor, introducción a Flask y procesamiento de _requests_ con _response_ de texto plano.
2. _Response_ de datos estructurados, análisis de _request_ y _response_, y _response_ en HTML simple
3. _Response_ en HTML intermedio, navegación, construcción automática de HTML
4. Manejo de variables de sesión, recepción y procesamiento de datos de usuario.
5. Conexión con bases de datos (local, online), CRUD

### _Encore_, vale la pena si da tiempo

a. Deployment en línea
b. _Decorators_
c. _Query Parameters_
d. Errores, excepciones y respuestas HTTP 

---

# I. Intro a web y Flask

Básicos modelo cliente-servidor, introducción a Flask y procesamiento de _requests_ con _response_ de texto plano.

## 0. Modelo cliente-servidor

**El objetivo de esta sección es mostrar y describir lo básico del modelo cliente servidor.**

* El Internet funciona con un modelo de _clientes_ interactuando con _servidores_.

* El _cliente_ solicita información. No es una persona, es un _programa_ pidiendo información a un servidor en nombre de esa persona.

  * El **browser** es un ejemplo de este tipo de programas.

* Con los _servidores_ pasa lo mismo, son programas ejecutándose en algún lugar esperando recibir solicitudes.

* Del lado del _servidor_ no tenemos control de lo que los clientes desarrollan, y vicecersa. Desarrollamos usando estándares, documentación y lineamientos.

* [Flask](http://flask.pocoo.org/) es una herramienta que se puede utilizar para desarrollar la parte del _servidor_.

  * Es una librería relativamente simple e intuitiva para poder distribuir datos.

* Los servidores _escuchan_ for peticiones, _requests_, en lugares particulares conocidos como _URLS_ or **endpoints**.

  * Con Flask simplificamos el proceso de configurar y exponer estos endpoints en muy pocas líneas de código y con un patrón fácil de replicar

## 1. Hello Flask!

**El objetivo de esta sección es mostrar flask y su uso básico.**

* Con estas líneas podemos tener dos enpoints muy simples respondiendo solicitudes de clientes:

  ```python
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

  ```

* Con estas líneas configuramos nuestro programa para escuchar solicitudes en dos endpoints y responder acorde a lo que le pidamos

  * En la _terminal_, vemos el resultado de `print`, pero el `return` lo ve el cliente.

* La línea `if __name__ == "__main__"` le dice a python en qué contexto ejecutar nuestra app.

### Actividad Flask 1.0

Los alumnos deberán desarrollar una aplicación simple con al menos 3 endpoints que respondan diferente información y que impriman su estado en la temrinal.


## 2. Construyendo Endpoints Dinámicos

**El objetivo de esta sección es que los alumnos integren urls dinámicas en su aplicación.**

Las URLs se pueden hacer dinámicas para recibir parámetros simples en texto.

* Ejemplificar urls con disintos patrones

```python
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

```

* Ejemplo
  
### Actividad Flask 2.0

Los alumnos deberán evolucionar su aplicación para que los endpoints reciban parámetros y cambien la forma en que responden.



## 3. Proceso _Behind the Sceens_

**El objetivo de esta sección es hacer evidente que flask es Python y se pueden usar funciones y estructuras de datos.**


### Actividad Flask y Python

Los alumnos deberán evolucionar su aplicación para que use estructuras de datos (diccionarios, listas) y funciones que no sean endpoints

---

# II. _Request_ y _Response_  

_Response_ de datos estructurados, análisis de _request_ y _response_, y _response_ en HTML simple

## 4. Respondiendo Datos

**El objetivo de esta sección es que los alumnos comprendan que la respuesta puede ser una estructura de datos interpretable por otro programa.**


### Actividad Flask y Python

Los alumnos deberán escribir una aplicación que devuelva datos estructurados usando json.


## 5. Análisis de _Request_ y _Response_

**El objetivo de esta sección es ahondar en la fomra de los request y response que se comunican entre clientes y servidores**


### Actividad Flask y Python

Explorar los request-response de algunos sitios y compartir qué les llama la atención

## 6. Respondiendo HTML

**El objetivo de esta sección es que los alumnos comprendan las páginas web son datos estructurados bajo HMTL que el browser sabe interpretar y puede desplegar**


### Actividad Flask y Python

Los alumnos deberán explorar el código HTML de algunos sitios web y cómo es una estructura anidada


---

# III. ¡Página web!

_Response_ en HTML intermedio, navegación, construcción automática de HTML

## 7. HTML

**El objetivo de esta sección es introducir el lenguaje, estructura y elementos de HTML5**


### Actividad Flask y Python

Los alumnos deberán escribir una página HTML simple que incluya tablas, listas, divs e imágenes

## 8. Navegación

**El objetivo de esta sección es ilustrar cómo funciona la navegación en el browser y qué es un hipervínculo**


### Actividad Flask y Python

Los alumnos deberán escribir una segunda página y generar navegación entre ellas

## 9. HTML Dinámico

**El objetivo de esta sección es introducir el concepto de template para dinamizar el html y jinja como motor que interactúa con Flask para poder entregarlos con la función render_template**

### Actividad Flask y Python

Los alumnos deberán convertir sus páginas en templates de Jinja que reciban parámetros desde flask para dinamizar su contenido

## 10. Condicionales en Jinja

**El objetivo de esta sección es introducir los condicionales de Jinja al momento de desplegar un template desde flask**

### Actividad Flask y Python

Los alumnos deberán agregar un condicional a sus páginas a partir de un parámetro

## 11. Iteraciones en Jinja

**El objetivo de esta sección es introducir las iteraciones de Jinja al momento de desplegar un template desde flask**

### Actividad Flask y Python

Los alumnos deberán agregar una iteración a sus páginas a partir de una estructura de datos pasada desde Flask

---

# IV. Sesiones y datos de usuarios

Manejo de variables de sesión, recepción y procesamiento de datos de usuario.

## 12. Cookies

**El objetivo de esta sección es mostrar las cookies como una herramienta para manejar información de sesión**

### Actividad Flask y Python

Los alumnos deberán escribir una aplicación que escriba un valor en una cookie como parte de una respuesta y lo lea en una llamada posterior

## 13. Formas HTML

**El objetivo de esta sección es mostrar la creación de formularios HTML**

### Actividad Flask y Python

Los alumnos deberán escribir una aplicación que responda con distintos códigos de éxito y de error

## 14. Formas Flask

**El objetivo de esta sección es que el alumno pueda recibir información inputada por el usuario y reaccionar acorde a lo solicitado**

### Actividad Flask y Python

Los alumnos deberán escribir templates que incluyan formas y endpoints que reciban esa información y reaccionen con base en lo recibido

---

# V. Conexión con datos

Conexión con bases de datos (local, online), CRUD

## 15. Conexión a base de datos

**El objetivo de esta sección es que el alumno pueda utilizar información almacenada en bases de datos para responder a las solicitudes**

### Actividad Flask y Python

Los alumnos deberán conectar su aplicación a una base de datos y consultarla para llevar a cabo la acción solicitada

## 16. Manipulación y exposición de datos

**El objetivo de esta sección es que el alumno comprenda el flujo completo entre solicitud, consulta de datos, procesamiento, preparación y exposición**

### Actividad Flask y Python

Los alumnos deberán usar todo lo anterior para resolver un problema relativamente complejo


---
