from myretail.database.db import db


class Price(db.EmbeddedDocument):
    value = db.FloatField()
    currency_code = db.StringField(required=True, default="USD")


class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    current_price = db.EmbeddedDocumentField(Price)
