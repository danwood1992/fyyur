from base import db
from datetime import datetime

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
    

class Area(BaseModel):
    __tablename__ = 'Area'

    city = db.Column(db.String(120))
    state = db.Column(db.String(120))

    def add(self):
        self.name = f'{self.city}, {self.state}'
        db.session.add(self)
        db.session.commit()
        if self.id:
            return True
        
         
class Venue(BaseModel):
    __tablename__ = 'Venue'

    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)
    area = db.relationship('Area', backref=db.backref('venues', cascade='all, delete'))
    area_id = db.Column(db.Integer, db.ForeignKey('Area.id'))

    @property
    def past_shows(self):
        return Show.query.filter_by(venue_id=self.id).filter(Show.start_time < datetime.now()).all()
    
    @property
    def upcoming_shows(self):
        return Show.query.filter_by(venue_id=self.id).filter(Show.start_time > datetime.now()).all()
    
    @property
    def past_shows_count(self):
        return len(self.past_shows)
    
    @property
    def upcoming_shows_count(self):
        return len(self.upcoming_shows)
    
    @property
    def genres(self):
        return [genre.genre.name for genre in self.genres]
    


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
 

    @property
    def past_shows(self):
        return Show.query.filter_by(artist_id=self.id).filter(Show.start_time < datetime.now()).all()
    
    @property
    def upcoming_shows(self):
        return Show.query.filter_by(artist_id=self.id).filter(Show.start_time > datetime.now()).all()
    
    @property
    def past_shows_count(self):
        return len(self.past_shows)
    
class Artist_Availability(BaseModel):
    __tablename__ = 'Artist_Availabilty'

    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    artist = db.relationship('Artist', backref=db.backref('availability', cascade='all, delete'))
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))

    def repr(self):
        return f'{self.artist.name} at {self.venue.name}'
    
    @property
    def artist_name(self):
        return self.artist.name
    
    @property
    def start_day(self):
        return self.start_time.strftime("%A")
    
    @property
    def start_month(self):
        return self.start_time.strftime("%B")
    
    @property
    def start_date(self):
        return self.start_time.strftime("%d")
    
    @property
    def start_year(self):
        return self.start_time.strftime("%Y")
    
    @property
    def end_day(self):
        return self.end_time.strftime("%A")
    
    @property
    def end_month(self):
        return self.end_time.strftime("%B")
    
    @property
    def end_date(self):
        return self.end_time.strftime("%d") 
    
    @property
    def end_year(self):
        return self.end_time.strftime("%Y")


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

    def repr(self):
        return f'{self.genre.name}'


class Genre(BaseModel):
    __tablename__ = 'Genre'

    def repr(self):
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

    def create_show(self):

        available_dates = Artist_Availability.query.filter_by(artist_id=self.artist_id)
        print(f"debug available dates: {available_dates}")
        for date in available_dates:
            if self.start_time >= date.start_time and self.start_time <= date.end_time:
              
                db.session.add(self)
                db.session.commit()
                return True
            else:
                print("Artist not available")
                return False
        
    
    @property
    def artist_name(self):
        return self.artist.name
    
    @property
    def venue_name(self):
        return self.venue.name
    
    @property
    def start_time_formatted(self):
        return self.start_time.strftime("%m/%d/%Y, %H:%M:%S")
    
    @property
    def start_day(self):
        return self.start_time.strftime("%A")
    
    @property
    def start_month(self):
        return self.start_time.strftime("%B")
    
    @property
    def start_date(self):
        return self.start_time.strftime("%d")
 


    


    