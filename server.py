from flask import Flask
import pymongo

app= Flask(__name__)


try:
    mongo = pymongo.MongoClient(
        host='localhost',
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    #this triggers an exception if cannot connect to DDBB
    mongo.server_info()
except:
    print('ERROR - cannot connect to db')
    

@app.route('/users',methods=['POST'])
def create_user():
    return'Ento says this is a POST from users endpoint'

if __name__== '__main__':
    app.run(port=5000,debug=True)
    # app.run(host='0.0.0.0',port=2000,debug=True)

