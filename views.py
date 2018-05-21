""" script for forms objects """
import pickle
from datetime import date
from flask_wtf import FlaskForm
from wtforms import SelectField


def get_sorted_countries_dict():
    """ returns sorted pairs of id/country """
    with open("countries.txt", "rb") as inp:
        countries = pickle.load(inp)
    sortedc = []
    for key in sorted(countries.keys()):
        sortedc.append((countries[key], key))
    return sortedc


def year():
    """ gets current year """
    return date.today().year


class CourseForm(FlaskForm):
    """ form for getting course """
    day = SelectField(u'Day',
                      choices=[(str(x), x) for x in range(1, 32)],
                      default=date.today().day)
    month = SelectField(u'Month',
                        choices=[(str(x), x) for x in range(1, 13)],
                        default=date.today().month)
    year = SelectField(u'Year',
                       choices=[(str(x), x) for x in range(2005, year()+1)],
                       default=date.today().year)
    charcode = SelectField(u'Convert to', choices=get_sorted_countries_dict())
