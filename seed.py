import csv
from models import db, Guest, Episode, Appearance
from app import create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    guest_cache = {}
    episode_cache = {}

    with open('guests.csv', newline='') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=1):
            date = row['Show'].strip()
            occupation = row['GoogleKnowlege_Occupation'].strip() or "Unknown"
            raw_guest_list = row['Raw_Guest_List']

            # Skip if date is missing or malformed
            if not date or date.lower() == "na":
                continue

            # Create episode if not already added
            if date not in episode_cache:
                episode = Episode(date=date, number=i)
                db.session.add(episode)
                db.session.flush()  # Get the ID
                episode_cache[date] = episode
            else:
                episode = episode_cache[date]

            # Create guest(s)
            guest_names = [name.strip() for name in raw_guest_list.split(',')]
            for guest_name in guest_names:
                if guest_name.lower() in ['na', '']:
                    continue
                if guest_name not in guest_cache:
                    guest = Guest(name=guest_name, occupation=occupation)
                    db.session.add(guest)
                    db.session.flush()
                    guest_cache[guest_name] = guest
                else:
                    guest = guest_cache[guest_name]

                # Create appearance
                appearance = Appearance(rating=5, episode_id=episode.id, guest_id=guest.id)
                db.session.add(appearance)

    db.session.commit()
    print("Database seeded successfully")
