from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    titulo="IDGS-802-Flask"
    lista=["juan","cesar","pedro"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/formularios")
def formularios():
    titulo="formularios"
    return render_template("index.html", titulo=titulo)

@app.route("/reportes")
def reportes():
    titulo="reportes"
    return render_template("index.html", titulo=titulo)

@app.route("/hola")
def about():
    return"hola, hola"

@app.route("/user/<string:user>")
def user(user):
    return f"Hello,{user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"Numero: {n}"

@app.route("/user/<int:id>/<string:username>")
def format(id, username):
    return "ID:{} NOMBRE: {}".format(id,username)

@app.route("/suma/<float:n2>/<float:n1>")
def suma(n1,n2):
    return "la suma es: {}".format(n1+n2)

@app.route("/default/")

@app.route("/default/<string:param>") 
def func(param="juan"):
    return "hola {}".format(param)

@app.route("/operas")
def operas():
    return '''
    <form>
    <label for="name">Name</label>
    <input type="text" id="name" name="name" requiered>
    <label for="name">paterno</label>
    <input type="text" id="name" name="name" required>
    </format>
    '''
@app.route("/operasBas")
def operas1():
    return render_template("operasBAS.html")

@app.route("/resultado", methods=["POST"])
def resultado():
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        op = request.form.get("operacion")
        if op == "suma":
            res = n1 + n2
            mensaje = f"La suma de {n1} + {n2} es: {res}"
        elif op == "resta":
            res = n1 - n2
            mensaje = f"La resta de {n1} - {n2} es: {res}"
        elif op == "multiplicacion":
            res = n1 * n2
            mensaje = f"La multiplicación de {n1} × {n2} es: {res}"
        elif op == "division":
            if n2 == 0:
                return "Error: No se puede dividir entre cero."
            res = n1 / n2
            mensaje = f"La división de {n1} ÷ {n2} es: {res}"
        else:
            return "Operación no válida."
        return mensaje


if __name__ == "__main__":
    app.run(debug=True, port=3333)