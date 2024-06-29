import os

class Config:
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://melenetonou:mongodatabasepassword@sauvemoi.h15f2zf.mongodb.net/SauveMoi?retryWrites=true&w=majority'