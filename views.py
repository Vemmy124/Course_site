from flask_wtf import Form
from wtforms import TextField, FileField, SelectField
import pickle
from datetime import date

def get_sorted_countries_dict():
    with open("countries.txt", "rb") as inp:
        countries = pickle.load(inp)
    sortedc = []
    for key in sorted(countries.keys()):
        sortedc.append((countries[key], key))
    return sortedc

class CourseForm(Form):
    day = SelectField(u'Day',
                      choices=[(str(x), x) for x in range(1, 32)],
                      default=date.today().day)
    month = SelectField(u'Month',
                        choices=[(str(x), x) for x in range(1, 13)],
                        default=date.today().month)
    year = SelectField(u'Year',
                       choices=[(str(x), x) for x in range(2005, date.today().year + 1)],
                       default=date.today().year)
    charcode = SelectField(u'Convert to', choices=get_sorted_countries_dict())