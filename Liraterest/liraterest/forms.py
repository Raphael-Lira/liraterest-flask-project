from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired, Email, EqualTo, Length, ValidationError
from liraterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmar = SubmitField('Fazer Login')


class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nome = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmar_senha = PasswordField('Cofirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmar = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError('Email já cadastrado')