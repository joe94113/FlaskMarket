from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError  # 驗證套件
from market.models import User


class RegisterForm(FlaskForm):

    # FlaskForm 會尋找有關 validate_表格名稱 的函示執行驗證，所以才以這樣的方式命名
    # FlaskForm理解將要進行驗證
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists! Please try a different username")

    def validate_email_address(self, email_address_checck):
        email_address = User.query.filter_by(email_address=email_address_checck.data).first()
        if email_address:
            raise ValidationError("Email Address already exists! Please try a different email address")

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])  # 確認是否和密碼一致
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label="User Name", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
