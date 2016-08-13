from application.users import models


def test_create_user_instance(session):
    email = 'test@example.com'
    username = 'test_user'
    password = 'foobarbaz'

    user = models.User(email, username, password)
    session.add(user)
    session.commit()

    assert user.id is not None
    assert user.followed.count() == 0
    assert user.newsfeed().count() == 0
