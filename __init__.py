from flask import Flask
from .extensions import mongo

def create_app():
    app=Flask(__name__)
    
    app.config['MONGO_URI'] = 'mongodb+srv://qimono:Secret-Ento-76@cluster0.jlga6l0.mongodb.net/DbEnto?retryWrites=true&w=majority'
    
    mongo.init_app(app)

    return app