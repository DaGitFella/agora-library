from app.models.user import User


def check_integrity(email):
    db_user = User.query.filter_by(email=email).first()
    if db_user:
        return True
    return False


def get_user_by_email(email):
    db_user = User.query.filter_by(email=email).first()
    if db_user:
        return db_user
    return None


def get_all_users():
    users = User.query.all()
    return users
