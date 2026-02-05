from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app=Flask(__name__)
app.secret_key="clave secreta"
csrf = CSRFProtect()

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

@app.route("/distancia", methods=["GET", "POST"])
def calcular_distancia():
    resultado_distancia = None
    
    if request.method == "POST":
            x1 = float(request.form.get("x1", 0))
            x2 = float(request.form.get("x2", 0))
            y1 = float(request.form.get("y1", 0))
            y2 = float(request.form.get("y2", 0))
            
            dx = x2 - x1
            dy = y2 - y1
            resultado_distancia = ((dx**2) + (dy**2))**0.5
            resultado_distancia = round(resultado_distancia, 2)
    return render_template("distancia.html", resultado=resultado_distancia)

@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    mat = 0
    nom=" "
    apa=" "
    ama=" "
    email=" "
    usuarios_class=forms.UserForm(request.form)
    if request.method=="POST" and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data
        messaje = "Bienvenido{}".format(nom)
        flash(messaje)
    return render_template("usuarios.html", form=usuarios_class,
                        mat=mat,nom=nom,apa=apa,ama=ama,email=email)
    
@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    resultado = None
    cinepolis_form = forms.CinepolisForm(request.form)
    
    if request.method == 'POST' and cinepolis_form.validate():
        nombre = cinepolis_form.nombre.data
        personas = cinepolis_form.personas.data
        cantidad = cinepolis_form.cantidad.data
        tarjeta_cineco = cinepolis_form.tarjeta_cineco.data
        
        limite_boletos = 7 * personas
        
        if cantidad > limite_boletos:
            flash(f"Error: Cada persona puede comprar máximo 7 boletos. Para {personas} persona(s) el límite es {limite_boletos} boletos. Intentaste comprar {cantidad} boletos.")
            return render_template('cinepolis.html', form=cinepolis_form, resultado=resultado)
        
        boletos_por_persona = cantidad / personas
        precio_boleta = 12
        subtotal = precio_boleta * cantidad
        
        if boletos_por_persona > 5:
            descuento_cantidad = 0.15
        elif boletos_por_persona >= 3:
            descuento_cantidad = 0.10
        else:
            descuento_cantidad = 0.0
        
        monto_descuento = subtotal * descuento_cantidad
        total = subtotal - monto_descuento
        
        descuento_cineco = 0
        if tarjeta_cineco:
            descuento_cineco = total * 0.10
            total = total - descuento_cineco
        
        resultado = {
            'nombre': nombre,
            'personas': personas,
            'cantidad': cantidad,
            'boletos_por_persona': boletos_por_persona,
            'precio_boleta': precio_boleta,
            'subtotal': subtotal,
            'descuento_cantidad': descuento_cantidad * 100,
            'monto_descuento': monto_descuento,
            'descuento_cineco': descuento_cineco,
            'total': total,
            'tiene_tarjeta': tarjeta_cineco
        }
        
        mensaje = f"Compra procesada para {personas} persona(s). Total: ${total:.2f}"
        flash(mensaje)
    
    return render_template('cinepolis.html', form=cinepolis_form, resultado=resultado)

                        
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3333)