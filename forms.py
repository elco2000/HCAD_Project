from flask_wtf import FlaskForm
from wtforms import (SelectField,
                     RadioField, IntegerRangeField, validators)
from wtforms.validators import InputRequired, Length

#

class BurnoutForm(FlaskForm):
    gender = RadioField('Uw geslacht:', choices=['Male', 'Female'],
                        validators=[InputRequired()])
    bedrijfstype = RadioField('Het bedrijfstype waar uw werkzaam bent:', choices=['Productie', 'Service'],
                              validators=[InputRequired()])
    thuiswerken = RadioField('Heeft uw de mogelijkheid om thuis te werken:', choices=['Ja', 'Nee'],
                             validators=[InputRequired()])
    hbw = SelectField('Hoe belangrijk is uw werk:',
                      choices=[(0.0, 0), (1.0, 1), (2.0, 2), (3.0, 3), (4.0, 4), (5.0, 5)]
                      )
    wu = SelectField('Uw gemiddelde werkuren per dag:',
                     choices=[(1.0, 1), (2.0, 2), (3.0, 3), (4.0, 4), (5.0, 5), (6.0, 6), (7.0, 7), (8.0, 8),
                              (9.0, 9), (10.0, 10)]
                     )
    mo = SelectField('Op Welke niveau voelt uw mentale moeheid:',
                     choices=[(0.0, 0), (0.5, 0.5), (1.0, 1), (1.5, 1.5), (2.0, 2), (2.5, 2.5), (3.0, 3), (3.5, 3.5),
                              (4.0, 4), (4.5, 4.5), (5.0, 5), (5.5, 5.5), (6.0, 6), (6.5, 6.5),
                              (7.0, 7), (7.5, 7.5), (8.0, 8), (8.5, 8.5),
                              (9.0, 9), (9.5, 9.5), (10.0, 10)]
                     )
