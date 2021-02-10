from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=80)])
    address = TextAreaField('Address', validators=[DataRequired(), Length(min=3, max=300)])
    
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=80)])
    price = FloatField('Price', validators=[DataRequired(), Length(min=1, max=8)])
    category = StringField('Category', validators=[DataRequired(), Length(min=1, max=80)])
    photo_url = StringField('Photo url', validators=[DataRequired(), URL()])
    store = QuerySelectField('store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    
    submit = SubmitField('Submit')
