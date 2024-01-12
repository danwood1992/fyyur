from models import Venue, Artist, Show, Show, Genre, Venue_Genre, Artist_Genre, Area
import faker, random

choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]



def seed_venues():
    for i in range(15):
        fake = faker.Faker()
        # i need the same image size
        venue = Venue(
            name = fake.company(),
            address = fake.address(),
            phone = fake.phone_number(),
            facebook_link = fake.url(),
            image_link = fake.image_url(width=800, height=600),
            website_link = fake.url(),
            seeking_talent = True,
            seeking_description = fake.text(),
            area = Area(city=fake.city(), state=random.choice(choices)
        ))
        venue.add()

        for i in range(3):
            genre = Genre(name=fake.word())
            genre.add()
            venue_genre = Venue_Genre(venue=venue, genre=genre)
            venue_genre.add()
    print("venues seeded")

def seed_artists():
    for i in range(20):
        fake = faker.Faker()
        artist = Artist(
            name = fake.name(),
            phone = fake.phone_number(),
            facebook_link = fake.url(),
            image_link = fake.image_url(),
            website_link = fake.url(),
            seeking_venue = True,
            seeking_description = fake.text()
        )
        artist.add()
        for i in range(3):
            genre = Genre(name=fake.word())
            genre.add()
            artist_genre = Artist_Genre(artist=artist, genre=genre)
            artist_genre.add()
    print("artists seeded")

def seed_shows():
    venues = Venue.query.all()
    artists = Artist.query.all()
    for i in range(20):
        fake = faker.Faker()
        show = Show(
            venue = random.choice(venues),
            artist = random.choice(artists),
            start_time = fake.date_time()
        )
        show.add()
    print("shows seeded")

def seed_database():
    seed_venues()
    seed_artists()
    seed_shows()

            
    
     
    