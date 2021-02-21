from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # connec = sqlite3.connect('my-data.db')
        # curs = connec.cursor()
        # user = curs.execute("SELECT * from users WHERE username=?", (username,))
        # row = curs.fetchone()
        # connec.close()
        return cls.query.filter_by(username=username).first()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # return user

    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connec = sqlite3.connect('my-data.db')
        # curs = connec.cursor()
        # user = curs.execute("SELECT * from users WHERE id=?", (_id,))
        # row = curs.fetchone()
        # connec.close()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # return user

    def add_user(self):
        db.session.add(self)
        db.session.commit()
        # username = UserModel.find_by_username(params.get('username'))
        # if username is not None:
        #     return "User with this nickname already exists, try again."
        # else:
        #     connec = sqlite3.connect('my-data.db')
        #     curs = connec.cursor()
        #     new_user = "INSERT INTO users (id, username, password) VALUES (?, ?, ?)"
        #     curs.execute(new_user, (*params.values(), ))
        #     connec.commit()
        #     connec.close()
        #     return "New user was registered."
