from db import db


class RunnersModel(db.Model):
    __tablename__ = "runners"
    _id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    half_marathon = db.Column(db.String, nullable=False)
    marathon = db.Column(db.String, nullable=False)
