from base import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(120), nullable=True)

    def add(self):
        db.session.add(self)
        db.session.commit()
        if self.id:
            return True
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        if self.id:
            return True
        
    def update(self):
        db.session.commit()
        if self.id:
            return True
        

    def repr(self):
        return f'{self.name}'
        
        
    
        
class Venue(BaseModel):
    __tablename__ = 'Venue'

    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)


class Artist(BaseModel):
    __tablename__ = 'Artist'

    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True)

class Artist_Genre(BaseModel):
    __tablename__ = 'Artist_Genre'

    genre = db.relationship('Genre', backref=db.backref('artists', cascade='all, delete'))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))
    artist = db.relationship('Artist', backref=db.backref('genres', cascade='all, delete'))
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))


class Venue_Genre(BaseModel):
    __tablename__ = 'Venue_Genre'


    genre = db.relationship('Genre', backref=db.backref('venues', cascade='all, delete'))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))
    venue = db.relationship('Venue', backref=db.backref('genres', cascade='all, delete'))
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))

class Genre(BaseModel):
    __tablename__ = 'Genre'

    def __repr__(self):
        return f'{self.name}'



class Show(BaseModel):
    __tablename__ = 'Show'

    start_time = db.Column(db.DateTime)
    artist = db.relationship('Artist', backref=db.backref('shows', cascade='all, delete'))
    venue = db.relationship('Venue', backref=db.backref('shows', cascade='all, delete'))
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
    genre = db.relationship('Genre', backref=db.backref('shows', cascade='all, delete'))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))


    