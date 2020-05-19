from myproject import db, app
import hashlib

class TinyUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullurl = db.Column(db.String)
    shorturl = db.Column(db.String, unique = True)
    code = db.Column(db.String)

    def __init__(self, fullurl):
        self.fullurl = fullurl
        self.code =  hashlib.md5(fullurl.encode()).hexdigest()[:7]
        self.shorturl = '127.0.0.1:5000/' + self.code
        print(self.code)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}