from myapp import myobj, db
from myapp.models import TopCitiesDB
from myapp.forms import TopCities

from flask import render_template, redirect, flash


@myobj.route("/", methods=['GET', 'POST'])
def home():


    #todo: add submit functionality to add to database
    #pull top cities from database

    form = TopCities()
    
    if form.validate_on_submit():

        city = TopCitiesDB(city_name = form.city_name.data, city_rank = form.city_rank.data, is_visited = form.is_visited.data, comments = form.comments.data)
        db.session.add(city)
        db.session.commit()
        flash(f"Added {city.city_name} to database")
        return redirect('/')
    

    cities = TopCitiesDB.query.order_by(TopCitiesDB.city_rank).all()
    title = "Top Cities"
    return render_template('home.html', form=form, cities=cities, title=title, name = "Dominic")
    


