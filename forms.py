from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, IntegerRangeField, validators)
from wtforms.validators import InputRequired, Length


class BurnoutForm(FlaskForm):
    gender = RadioField('Gender', choices=['Male', 'Female'],
                        validators=[InputRequired()])
    bedrijfstype = RadioField('Bedrijfstype', choices=['Productie', 'Service'],
                              validators=[InputRequired()])
    thuiswerken = RadioField('Thuis werken?', choices=['Ja', 'Nee'],
                             validators=[InputRequired()])
    hbw = IntegerRangeField('Hoe belangrijk is uw werk?',
                            [validators.NumberRange(min=0, max=5)],
                            )
    wu = IntegerRangeField('Uw gemiddelde werkuren per dag',
                           [validators.NumberRange(min=0, max=10)],
                           )
    mo = IntegerRangeField('Op Welke niveau voelt uw mentale moeheid?',
                           [validators.NumberRange(min=0, max=10)],
                           )
