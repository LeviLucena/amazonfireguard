import os
from dotenv import load_dotenv
from app.services.firms import fetch_firms_csv
from app.database.models import FireAlert
from app.database.db_utils import db
from app import create_app

load_dotenv()
app = create_app()

def save_to_db(df):
    with app.app_context():
        for _, row in df.iterrows():
            alert = FireAlert(
                latitude=row['latitude'],
                longitude=row['longitude'],
                brightness=row['brightness'],
                acq_date=row['acq_date'],
                satellite=row['satellite']
            )
            db.session.add(alert)
        db.session.commit()

if __name__ == "__main__":
    url = os.getenv("FIRMS_API")
    df = fetch_firms_csv(url)
    save_to_db(df)
