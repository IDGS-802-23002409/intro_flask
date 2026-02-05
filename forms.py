from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, BooleanField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula", [validators.DataRequired("El campo es requerido"),
                                        validators.NumberRange(min=100, max=1000, message="Ingrese un valor valido")])
    nombre=StringField("Nombre", [validators.DataRequired("El campo es requerido"),
                                validators.length(min=3, max=10, message="ingrese un nombre netre 2 y 10 caracteres")])
    apaterno=StringField("Apaterno", [validators.DataRequired("El campo es requerido")])
    amaterno=StringField("Amaterno", [validators.DataRequired("El campo es requerido")])
    correo=EmailField("Correo", [validators.email("El email es requerido")])

class CinepolisForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired("Por favor escribe tu nombre"),
        validators.length(min=3, max=50, message="El nombre debe tener entre 3 y 50 caracteres")
    ])
    personas = IntegerField("Número de Personas", [
        validators.DataRequired("Por favor escribe cuántas personas van a comprar"),
        validators.NumberRange(min=1, max=10, message="Debe haber entre 1 y 10 personas")
    ])
    cantidad = IntegerField("Cantidad de Boletas", [
        validators.DataRequired("Por favor escribe cuántas boletas quieres"),
        validators.NumberRange(min=1, message="Debes comprar entre 1 y 7 boletas")
    ])
    tarjeta_cineco = BooleanField("Tarjeta CINECO")

