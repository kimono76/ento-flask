from flask import Flask

app= Flask(__name__)


try:
    pass
except:
    pass

@app.route('/users',methods=['POST'])
def create_user():
    return'POST create user'

if __name__== '__main__':
    app.run(port=3000,debug=True)

