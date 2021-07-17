from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField, DateField, IntegerField
from wtforms.fields import SelectField

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25, message="El largo del usuario debe de ser mayor que %(min)d y menor que %(max)d")], render_kw={'class':'myclass'})
    email = EmailField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class CategoryForm(Form):
    cat_name = StringField('CatName', [validators.DataRequired(message="Favor ingrese el nombre de la categoría")])
    cat_description = StringField('CatDescription', [validators.DataRequired(message="Favor ingrese la descripcion de la categoría")])
    cat_select = SelectField('CatSelect', choices=[(1, 'Activo'), (0, 'Inactivo')])