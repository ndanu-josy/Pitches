from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm

class PitchesForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    content = TextAreaField('Write a pitch')
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    """
    Class to create a wtf form for adding comments
    """
    opinion = TextAreaField('Add a comment')
    submit = SubmitField('Submit')

class CategoriesForm(FlaskForm):
    """
    Class to create a wtf form for adding pitch categories
    """
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')