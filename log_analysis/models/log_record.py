from mongoengine import Document, StringField, DateTimeField

class LogRecord(Document):
    ip = StringField(required=True)
    date = DateTimeField(required=True)
    product = StringField(required=True)
    version = StringField()
    id_code = StringField(required=True)
    activity_description = StringField(required=True)
    additional_message = StringField()
