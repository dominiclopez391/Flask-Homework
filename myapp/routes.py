from myapp import myobj, db
from myapp.models import TopCities
from myapp.forms import TopCitiesForm

from flask import render_template


@myobj.route("/Home")
def home():


    #todo: add submit functionality to add to database
    #pull top cities from database

    form = TopCitiesForm()
    return render_template('home.html', form=form, name = "Dominic")
    


