from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm

class PitchForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    content = TextAreaField('Write a pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    """
    Class to create a wtf form for adding comments
    """
    opinion = TextAreaField('Add a comment')
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    """
    Class to create a wtf form for adding pitch categories
    """
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')