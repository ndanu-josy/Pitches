from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm

class PitchForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    pitch_title = StringField('Pitch title',validators=[Required()])
    pitch_category = SelectField('Pitch Category', choices = [('Select category','Select category'),('interview', 'Interview'), ('product', 'Product'),('promotion','Promotion'),('pickup','Pickup Lines')], validators=[Required()])
    pitch_comment = TextAreaField('Your Pitch')
    submit = SubmitField('Submit Pitch')
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