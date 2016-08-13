from application import db
import datetime

__all__ = ['Post']


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(db.Text())

    created_on = db.Column(db.DateTime(),
                           default=datetime.utcnow,
                           index=True)

    user_id = db.Column(db.Integer(), db.ForeinKey('user_id'))

    def __repr__(self):
        return '<Post %r>' % self.body

