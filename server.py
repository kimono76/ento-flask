from flask import Flask
import pymongo

app= Flask(__name__)


try:
    pass
except:
    pass

@app.route('/users',methods=['POST'])
def create_user():
    return'Ento says this is a POST from users endpoint'

if __name__== '__main__':
    app.run(port=5000,debug=True)
    # app.run(host='0.0.0.0',port=2000,debug=True)

