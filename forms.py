from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms.validators import Email
import email_validator

class formlogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 12)])
    submitLogin = SubmitField('Login')
    nome = StringField('nome', validators=[DataRequired()])

class formNovoUsuario(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    celular = StringField('numero', validators=[DataRequired()])
    cpf = StringField('cpf', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    senhaCOnfirmarção = PasswordField('confirme sua senha', validators=[DataRequired(), EqualTo(senha)])
    submitNovo = SubmitField('Criar conta')