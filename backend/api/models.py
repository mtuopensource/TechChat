from mongoengine import Document, EmbeddedDocument, fields

class Board(Document):
    title = fields.StringField(max_length=32, required=True)
    description = fields.StringField(max_length=128, required=True, null=True)
