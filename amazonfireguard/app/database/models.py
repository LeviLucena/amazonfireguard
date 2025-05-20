from app.database.db_utils import db

class FireAlert(db.Model):
    __tablename__ = 'fire_alerts'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    brightness = db.Column(db.Float)
    acq_date = db.Column(db.Date)
    satellite = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "brightness": self.brightness,
            "acq_date": self.acq_date.isoformat(),
            "satellite": self.satellite,
        }
