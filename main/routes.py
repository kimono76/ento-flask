from flask import BluePrint

main = BluePrint('main',__name__)

@main.route('/')
def index():
    return('<h1>Ento</h1>')