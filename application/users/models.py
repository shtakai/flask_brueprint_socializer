import datetime
from application import db, flask_bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

__all__ = ['followers', 'user']

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeinKey('user.id'),
              primary_key=True),
    db.Column('user_id', db.Integer, db.ForeinKey('user.id'),
              primary_key=True)
)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True)

    username = db.Column(db.String(40), unique=True)

    _password = db.Column('password', db.String(60))

    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    followed = db.relationship(
        'User',
        secondary=followers,
        primaryjoin=(id==followers.c.follower_id),
        secondaryjoin=(id==followers.c.user_id),
        backref=db.backref('followers', lasy='dynamic'),
        lazy='dynamic'
    )

    @hybriy_property
    def password(self):
        return self._password

    @password_setter
    def password(self, password):
        self._password = flask_bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


    def unfollow(self, user):
        if not self.is_following(user):
            return False
        self.followed.remove(user)
        return self

    def follow(self, user):
        if self.is_following(user):
            return False
        self.followerd.append(user)
        return self

    def is_following(self, user):
        followed = self.followed.filter(followers.c.user_id == user_id)
        return followed.count() > 0
