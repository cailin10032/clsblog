from flask.ext.wtf import Form
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import Required, Length
from flask.ext.pagedown.fields import PageDownField


class PostForm(Form):
    body = PageDownField("What's on your mind", validators=[Required()])
    submit = SubmitField("Submit")


class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
