try:
    from application import db
except ModuleNotFoundError:
    from __init__ import db

GCC = db.Table('GCC',
  db.Column('s1',db.Integer),
    db.Column('s2',db.Integer)
)

COLL = db.Table( 'COLL',
    db.Column('s',db.Integer),
    db.Column('c',db.Integer)
)

class Result(db.Model):
    __tablename__ = 'result'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    total = db.Column(db.Integer)
    gcc = db.Column(db.Integer)
    col = db.Column(db.Integer)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()