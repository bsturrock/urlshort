from myproject import db, app

class TinyUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullurl = db.Column(db.String)
    shorturl = db.Column(db.String)

    def __init__(self, fullurl):
        self.fullurl = fullurl

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}