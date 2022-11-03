from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, IntegerRangeField, validators)
from wtforms.validators import InputRequired, Length


class BurnoutForm(FlaskForm):
    gender = RadioField('Uw geslacht:', choices=['Male', 'Female'],
                        validators=[InputRequired()])
    bedrijfstype = RadioField('Het bedrijfstype waar uw werkzaam bent:', choices=['Productie', 'Service'],
                              validators=[InputRequired()])
    thuiswerken = RadioField('Heeft uw de mogelijkheid om thuis te werken:', choices=['Ja', 'Nee'],
                             validators=[InputRequired()])
    hbw = IntegerRangeField('Hoe belangrijk is uw werk:',
                            [validators.NumberRange(min=0, max=5)],
                            )
    wu = IntegerRangeField('Uw gemiddelde werkuren per dag:',
                           [validators.NumberRange(min=0, max=10)],
                           )
    mo = IntegerRangeField('Op Welke niveau voelt uw mentale moeheid:',
                           [validators.NumberRange(min=0, max=10)],
                           )
