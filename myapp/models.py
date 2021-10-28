from myapp import db

class TopCities(db.Model):
    id = db.Column(db.Integer, primary_key=True) #primary key defines database location
    city_name = db.Column(db.String(64), index=True)
    city_rank = db.Column(db.Integer)
    is_visited = db.Column(db.Boolean)
    comments = db.Column(db.String(128), index=True)

